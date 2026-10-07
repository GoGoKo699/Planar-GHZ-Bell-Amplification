#!/usr/bin/env python3
"""Five bounded checks of the planar GHZ audit and full-correlation rate bound.

python check_audit_and_rate.py --output NEW.json

The continuum proofs are in AUDIT_AND_RATE.md. Numerical optimizations here
are diagnostic comparisons, not proof of the general theorem or of priority.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from itertools import product
import json
import math
from pathlib import Path
import unittest
import numpy as np
from scipy.optimize import minimize, linprog

X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
I=np.eye(2,dtype=complex)
A_RAT=[(F(7,10),F(0)),(F(-21,50),F(14,25)),(F(-7,25),F(-33,50))]
H_RAT=[(F(492044,10**6),F(25383,10**6)),(F(-271368,10**6),F(376503,10**6)),(F(-226537,10**6),F(-492541,10**6))]
REPORT={}

def obs(v):return v[0]*X+v[1]*Y

def tensor(items):
    out=np.ones((1,1),complex)
    for a in items:out=np.kron(out,a)
    return out

def hull_indices(points):
    """Monotone-chain hull, independent of the old Qhull implementation."""
    canonical={}
    for i,p in enumerate(points):canonical.setdefault(tuple(p),i)
    ids=sorted(canonical.values(),key=lambda i:tuple(points[i]))
    def cross(i,j,k):
        u=points[j]-points[i];v=points[k]-points[i]
        return u[0]*v[1]-u[1]*v[0]
    if len(ids)<=1:return ids
    def half(seq):
        stack=[]
        for i in seq:
            while len(stack)>=2 and cross(stack[-2],stack[-1],i)<=0:stack.pop()
            stack.append(i)
        return stack
    return half(ids)[:-1]+half(ids[::-1])[:-1]

def geometry(a):
    a=np.asarray(a,float);m=len(a);pts=np.r_[a,-a]
    ids=hull_indices(pts)
    h=np.zeros_like(a)
    if len(ids)<3:
        j=int(np.argmax(np.linalg.norm(a,axis=1)));nu=float(np.linalg.norm(a[j]))
        if nu:h[j]=a[j]/nu
        return h,nu,([a[j]] if nu else [])
    vertices=pts[ids];edges=np.roll(vertices,-1,axis=0)-vertices
    lengths=np.linalg.norm(edges,axis=1);tangents=edges/lengths[:,None]
    for j,i in enumerate(ids):
        h[i%m]+=(1 if i<m else -1)*(tangents[j-1]-tangents[j])/4
    return h,float(sum(lengths)/4),list(edges[:len(edges)//2]/2)

def cases():
    return [np.array(A_RAT,float),np.array([[.8,0],[0,.6]]),
       np.array([[.76,0],[-.38,.76*np.sqrt(3)/2],[-.38,-.76*np.sqrt(3)/2]]),
       np.array([[.84,.05],[.05,.77],[-.61,.38],[-.5,-.55],[.1,.07]]),
       np.array([[.7,0],[.2,0],[-.7,0],[0,0]]),
       np.array([[0,0],[0,0]]),np.array([[.8,0],[0,.6],[.8,0],[0,0]])]

def local_bound(beta):
    m=beta.shape[0];n=beta.ndim
    tables=np.array(list(product((-1,1),repeat=m)),float)
    best=0.
    for choices in product(tables,repeat=n):
        d=choices[0]
        for v in choices[1:]:d=np.multiply.outer(d,v)
        best=max(best,abs(float(np.sum(beta*d))))
    return best

def bell_operator(a,beta):
    m=len(a);n=beta.ndim;ops=[obs(p)for p in a]
    out=np.zeros((2**n,2**n),complex)
    for settings in product(range(m),repeat=n):out+=beta[settings]*tensor([ops[j]for j in settings])
    return out

def witness(a,n):
    h,nu,_=geometry(a);c=h[:,0]+1j*h[:,1];T=sum(z*obs(v)for z,v in zip(c,a))
    u,v=T[0,1],T[1,0]
    gamma=-n*(np.angle(u)+np.angle(v))/2 if abs(v)>1e-14 else -n*np.angle(u)
    TN=tensor([T]*n);B=(np.exp(1j*gamma)*TN+np.exp(-1j*gamma)*TN.conj().T)/2
    phase=-np.angle(B[0,-1]);psi=np.zeros(2**n,complex);psi[0]=1/np.sqrt(2);psi[-1]=np.exp(1j*phase)/np.sqrt(2)
    return B,psi,nu,u,v,gamma

def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cpow(a,n):
    z=(F(1),F(0))
    for _ in range(n):z=mul(z,a)
    return z

def sqrt_interval(q,digits=30):
    scale=10**digits;k=math.isqrt(q.numerator*scale*scale//q.denominator)
    lo=F(k,scale);hi=F(k+1,scale)
    assert lo*lo<=q<hi*hi
    return lo,hi

class Checks(unittest.TestCase):
    def test_01_geometry_duality_independent_optimization_and_degeneracies(self):
        rows=[]
        for a in cases():
            h,nu,gens=geometry(a);signs=np.array(list(product((-1,1),repeat=len(a))),float)
            self.assertLessEqual(np.max(np.linalg.norm(signs@h,axis=1)),1+2e-14)
            self.assertAlmostEqual(float(np.sum(a*h)),nu,places=13)
            if not nu:
                rows.append({'settings':len(a),'nu':0.,'zero_case':True});continue
            # Maximize the dual directly from a strictly feasible point; no hull constraint.
            # Use the equivalent unsquared norm constraints and remove the
            # exact duplication between s and -s. Keep the old full squared
            # residual check below as an independent acceptance criterion.
            reduced=np.array([(1,)+s for s in product((-1,1),repeat=len(a)-1)],float)
            def cons(x):return 1-np.linalg.norm(reduced@x.reshape(a.shape),axis=1)
            def jac(x):
                v=reduced@x.reshape(a.shape)
                v=v/np.maximum(np.linalg.norm(v,axis=1),1e-30)[:,None]
                return -np.einsum('sm,sd->smd',reduced,v).reshape(len(reduced),-1)
            x0=(.3*a/np.sum(np.linalg.norm(a,axis=1))).ravel()
            sol=minimize(lambda x:-float(np.dot(x,a.ravel())),x0,jac=lambda x:-a.ravel(),method='SLSQP',
                constraints=[{'type':'ineq','fun':cons,'jac':jac}],options={'ftol':1e-12,'maxiter':500})
            self.assertTrue(sol.success,sol.message)
            self.assertLess(abs(-sol.fun-nu),2e-8)
            self.assertGreaterEqual(min(1-np.sum((signs@sol.x.reshape(a.shape))**2,axis=1)),-2e-8)
            # Parent reconstruction by independent bounded-coefficient feasibility.
            gs=np.array(gens);parent=[]
            for g in gs:
                mu=np.linalg.norm(g)/nu
                parent.extend([(mu*I+obs(g/nu))/2,(mu*I-obs(g/nu))/2])
            self.assertLess(np.linalg.norm(sum(parent)-I),2e-14)
            self.assertGreaterEqual(min(np.linalg.eigvalsh(p).min()for p in parent),-2e-14)
            for v0 in a:
                fit=linprog(np.zeros(len(gs)),A_eq=gs.T,b_eq=v0,bounds=[(-1,1)]*len(gs),method='highs')
                self.assertTrue(fit.success)
                reconstructed=sum(t*(parent[2*j]-parent[2*j+1])for j,t in enumerate(fit.x))
                self.assertLess(np.linalg.norm(reconstructed-obs(v0/nu)),4e-13)
            rows.append({'settings':len(a),'nu':nu,'independent_dual_value':-float(sol.fun),'parent_outcomes':len(parent)})
        REPORT['geometry_audit']=rows

    def test_02_full_operator_upper_bound_and_parent_hidden_variables(self):
        rng=np.random.default_rng(7317);rows=[]
        for a in cases()[:3]:
            _,nu,gs=geometry(a);m=len(a)
            for n in (2,3):
                for trial in range(4):
                    beta=rng.integers(-3,4,size=(m,)*n).astype(float)
                    L=local_bound(beta)
                    if L==0:continue
                    beta/=L;B=bell_operator(a,beta)
                    norm=float(np.max(abs(np.linalg.eigvalsh(B))))
                    self.assertLessEqual(norm,nu**n+2e-12)
                    # All-state bound is checked through the entire spectrum, not random states.
                    rows.append({'settings':m,'parties':n,'trial':trial,'operator_norm':norm,'upper':nu**n})
            # Actual joint parent probabilities for an arbitrary entangled input, N=2.
            ps=[]
            for g in gs:ps.extend([(np.linalg.norm(g)*I+obs(g))/(2*nu),(np.linalg.norm(g)*I-obs(g))/(2*nu)])
            z=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4));rho=z@z.conj().T;rho/=np.trace(rho)
            joint=np.array([[np.trace(rho@np.kron(p,q)).real for q in ps]for p in ps])
            self.assertGreaterEqual(joint.min(),-1e-13);self.assertAlmostEqual(float(joint.sum()),1.,places=12)
            response=[]
            for v0 in a:
                fit=linprog(np.zeros(len(gs)),A_eq=np.array(gs).T,b_eq=v0,bounds=[(-1,1)]*len(gs),method='highs')
                response.append(np.array([s*t for t in fit.x for s in (1,-1)]))
            for i,j in product(range(m),repeat=2):
                actual=np.trace(rho@np.kron(obs(a[i]/nu),obs(a[j]/nu))).real
                self.assertAlmostEqual(float(response[i]@joint@response[j]),float(actual),places=12)
        REPORT['all_state_upper_checks']=rows

    def test_03_ghz_is_exact_top_state_of_constructed_witness(self):
        rows=[]
        for a in cases()[:5]:
            for n in (2,3,4,5):
                B,psi,nu,u,v,gamma=witness(a,n)
                value=(abs(u)**n+abs(v)**n)/2
                self.assertLess(abs(u.imag),2e-14);self.assertLess(abs(u.real-nu),2e-14)
                self.assertLessEqual(abs(v),nu+2e-14)
                self.assertLess(np.linalg.norm(B@psi-value*psi),8e-13)
                opnorm=float(np.max(abs(np.linalg.eigvalsh(B))))
                self.assertLess(abs(opnorm-value),8e-13)
                self.assertLessEqual(nu**n/2,value+8e-13)
                self.assertLessEqual(value,nu**n+8e-13)
                for k in range(n+1):
                    bound=(abs(u)**(n-k)*abs(v)**k+abs(v)**(n-k)*abs(u)**k)/2
                    self.assertLessEqual(bound,value+8e-13)
                if n<=3:
                    h,_,_=geometry(a);cs=h[:,0]+1j*h[:,1]
                    beta=np.array([np.real(np.exp(1j*gamma)*np.prod([cs[x]for x in settings]))for settings in product(range(len(a)),repeat=n)]).reshape((len(a),)*n)
                    self.assertLessEqual(local_bound(beta),1+2e-12)
                    self.assertLess(np.linalg.norm(bell_operator(a,beta)-B),8e-13)
                rows.append({'settings':len(a),'parties':n,'nu':nu,'ghz_value':float(value),'full_operator_norm':opnorm,'dimension':2**n})
        REPORT['optimal_state_for_constructed_inequality']=rows

    def test_04_exact_margin_and_local_noise_controls(self):
        pts=[tuple(p)for p in A_RAT]+[tuple(-x for x in p)for p in A_RAT]
        ids=hull_indices(np.array(pts,object));lo=F();hi=F()
        for j,i in enumerate(ids):
            v=pts[ids[(j+1)%len(ids)]];q=sum((v[k]-pts[i][k])**2 for k in range(2))
            l,h=sqrt_interval(q);lo+=l/4;hi+=h/4
        self.assertGreater(lo,1);self.assertLess(hi-lo,F(1,10**29))
        u=(F(),F());v=(F(),F())
        for h,a in zip(H_RAT,A_RAT):
            x=mul(h,(a[0],-a[1]));y=mul(h,a)
            u=(u[0]+x[0],u[1]+x[1]);v=(v[0]+y[0],v[1]+y[1])
        for signs in product((-1,1),repeat=3):
            s=tuple(sum(signs[j]*H_RAT[j][k] for j in range(3))for k in range(2))
            self.assertLessEqual(s[0]**2+s[1]**2,1)
        def value(n,t=F(1)):
            a=cpow((t*u[0],t*u[1]),n);b=cpow((t*v[0],t*v[1]),n)
            return (a[0]+b[0])/2
        e13=value(13);noisy13=value(13,F(99,100));noisy16=value(16,F(99,100))
        self.assertGreater(e13,1);self.assertLess(noisy13,1);self.assertGreater(noisy16,1)
        self.assertLess(F(94,100)*hi,1)
        self.assertLess(hi**12,2) # No state/full-correlation inequality reaches factor 2 for N<=12.
        self.assertGreater(value(25),2) # This explicit GHZ witness reaches it at N=25.
        self.assertGreater(lo**25/2,2)
        REPORT['exact_new_controls']={'nu_lower':str(lo),'nu_upper':str(hi),'nu_display':float((lo+hi)/2),
           'unshrunk_13_exact':str(e13),'one_percent_shrink_13_value':float(noisy13),'one_percent_shrink_16_value':float(noisy16),
           'one_percent_shrink_16_exact':str(noisy16),'six_percent_shrink_compatible_upper':float(F(94,100)*hi),
           'factor_two_any_state_requires_at_least_parties':13,'factor_two_explicit_ghz_sufficient_parties':25,
           'factor_two_ghz_value':float(value(25)),'asymptotic_rate':'lim R_N^(1/N)=nu; analytical squeeze, not numerical extrapolation.'}

    def test_05_restriction_checks_and_near_compatibility_scaling(self):
        # Full-correlation qualification is essential: a one-party marginal is
        # of degree one, not degree N, in local measurement sharpness.
        nu=F(1,2);N=3;marginal=nu
        self.assertGreater(marginal,nu**N)
        # A compatible collinear family reaches nu^N exactly, never violates.
        a=np.array([[.5,0],[-.2,0],[0,0]])
        for n in (2,3,5):
            B,psi,norm,u,v,gamma=witness(a,n)
            self.assertAlmostEqual(float(np.vdot(psi,B@psi).real),.5**n,places=13)
        # Fixed factor-two targets require Theta(1/(nu-1)), not a proof that any
        # arbitrarily small violation requires that many parties.
        rows=[]
        for eps in (F(1,10),F(1,100),F(1,1000)):
            q=1+eps;nlo=2
            while q**nlo<2:nlo+=1
            nhi=2
            while q**nhi<=4:nhi+=1
            self.assertLess(q**(nlo-1),2);self.assertGreater(q**nhi/2,2)
            rows.append({'nu_minus_one':str(eps),'necessary_parties_for_factor_two':nlo,'sufficient_from_strict_bound':nhi})
        REPORT['scope_controls']={'marginal_counterexample':{'N':3,'nu':'.5','marginal_quantum_value':'.5','nu_power_N':'.125'},
            'all_full_correlation_scope':True,'near_boundary_counts':rows,
            'not_claimed':['optimal finite-N party count','arbitrary marginal-containing Bell functionals','efficient sampling','genuine multipartite nonlocality','biased or noncoplanar extension']}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True,type=Path);a=p.parse_args()
    if a.output.exists():p.error('Refusing to overwrite an existing report')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    REPORT.update(status='PASS'if result.wasSuccessful()else'FAIL',tests_run=result.testsRun,
       scope='Author-side finite algebraic and numerical checks; theorem rests on analytical proofs and no priority is inferred.')
    a.output.parent.mkdir(parents=True,exist_ok=True)
    with a.output.open('x')as f:json.dump(REPORT,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
    raise SystemExit(0 if result.wasSuccessful()else 1)

if __name__=='__main__':main()
