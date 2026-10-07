#!/usr/bin/env python3
"""Five finite checks supporting a compact planar-GHZ theorem account.

This is an author-side check, not a many-party simulation or priority proof.
Original source-dictionary and earlier scientific checks are imported unchanged.
Run with a fresh output file: python check_consolidation.py --output NEW.json
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import importlib.util
from itertools import product, combinations
import json
import math
from pathlib import Path
import unittest
import numpy as np

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('source_dictionary',ROOT/'prior/check_source_dictionary.py')
assert spec and spec.loader
source=importlib.util.module_from_spec(spec);spec.loader.exec_module(source)
old=source.old
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
I=np.eye(2,dtype=complex)
REPORT={}


def ghz(n: int, phase: float=0., first: int=0):
    state=np.zeros(2**n,complex)
    state[first]=1/np.sqrt(2)
    state[first^((1<<n)-1)]=np.exp(1j*phase)/np.sqrt(2)
    return state


def sqrt_enclosure(x:F, digits:int=35):
    if x<0:raise ValueError('Negative radicand')
    d=10**digits
    k=math.isqrt((x.numerator*d*d)//x.denominator)
    lo=F(k,d)
    hi=lo if lo*lo==x else F(k+1,d)
    assert lo*lo<=x<=hi*hi
    return lo,hi


def qmul(z,w):return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def qpow(z,n):
    out=(F(1),F(0))
    for _ in range(n):out=qmul(out,z)
    return out


def local_bound(beta):
    """Same full deterministic maximum, with axiswise vectorized contraction.

    Fixing the first setting's sign to +1 at each site loses only an
    overall output sign, immaterial for an absolute full-correlation bound.
    """
    m=beta.shape[0]
    signs=np.array([(1,)+s for s in product((-1,1),repeat=m-1)],float)
    values=np.array(beta,dtype=float)
    for axis in range(beta.ndim):
        values=np.moveaxis(np.tensordot(signs,values,axes=(1,axis)),0,axis)
    return float(np.max(np.abs(values)))


class ConsolidationChecks(unittest.TestCase):
    def test_01_compact_bridge_and_sharpened_all_state_bound(self):
        rng=np.random.default_rng(707)
        for shape in ((2,2),(3,3),(2,2,2),(3,3,3)):
            beta=rng.integers(-3,4,size=shape).astype(float)
            self.assertEqual(local_bound(beta),old.local_bound(beta))
        rows=[]
        for a in source.examples()[:4]:
            d=source.source_construct(a)
            nu=d['nu'];radius=float(np.linalg.norm(a,axis=1).max())
            self.assertLessEqual(radius,nu+2e-14)
            self.assertLessEqual(nu,np.pi*radius/2+2e-14)
            c=d['coeff'][:,0]+1j*d['coeff'][:,1]
            k=d['K'][0]+1j*d['K'][1]
            v=.5*np.sum(k*k/d['lengths'])
            self.assertAlmostEqual(float(np.dot(c,(a[:,0]+1j*a[:,1]).conj()).real),nu,places=13)
            for n in (2,3,4):
                gamma=-n*np.angle(v)/2 if abs(v)>1e-14 else 0.
                beta=np.array([np.real(np.exp(1j*gamma)*np.prod(c[list(ind)]))
                               for ind in product(range(len(a)),repeat=n)]).reshape((len(a),)*n)
                op=old.bell_operator(a,beta)
                L=local_bound(beta)
                state=ghz(n,-np.angle(op[0,-1]))
                val=float(np.vdot(state,op@state).real)
                target=(nu**n+abs(v)**n)/2
                self.assertLess(abs(val-target),3e-13)
                self.assertLess(abs(np.linalg.norm(op,2)-target),3e-13)
                self.assertLessEqual(L,1+3e-14)
                self.assertLessEqual(target/L,radius*nu**(n-1)+4e-13)
                for _ in range(3):
                    b=rng.integers(-3,4,size=(len(a),)*n).astype(float)
                    if not np.any(b):b.flat[0]=1
                    bound=local_bound(b)
                    norm=float(np.linalg.norm(old.bell_operator(a,b),2))
                    self.assertLessEqual(norm,radius*nu**(n-1)*bound+2e-11)
                rows.append(dict(settings=len(a),parties=n,nu=nu,radius=radius,
                                 constructed_value=val,exact_local_bound_numeric=L,
                                 sharpened_ratio_ceiling=radius*nu**(n-1)))
        REPORT['compact_theorem_checks']=rows

    def test_02_explicit_n_minus_one_parent_local_model(self):
        # Literal source parent for its signed/reordered half-hull representatives.
        d=source.source_construct(source.examples()[0]);a=d['V'].T
        nu=d['nu'];radius=float(np.linalg.norm(a,axis=1).max())
        parent=[];signs=[]
        for j,vec in enumerate(d['X'].T):
            size=np.linalg.norm(vec)
            if size<1e-15:continue
            for sign in (1,-1):
                parent.append((size*I+sign*old.obs(vec))/(2*nu))
                signs.append(sign*d['B'][j])
        self.assertLess(np.linalg.norm(sum(parent)-I),3e-14)
        for x in range(len(a)):
            self.assertLess(np.linalg.norm(sum(s[x]*g for s,g in zip(signs,parent))-old.obs(a[x])/nu),3e-14)
        rng=np.random.default_rng(71);rows=[]
        for n in (2,3):
            raw=rng.normal(size=(2**n,2**n))+1j*rng.normal(size=(2**n,2**n))
            rho=raw@raw.conj().T;rho/=np.trace(rho)
            hidden=[]
            for labels in product(range(len(parent)),repeat=n-1):
                g=old.tensor([parent[k]for k in labels])
                contracted=(np.kron(g,I)@rho).reshape(2**(n-1),2,2**(n-1),2)
                sigma=np.einsum('abad->bd',contracted)
                weight=float(np.trace(sigma).real)
                self.assertGreaterEqual(np.linalg.eigvalsh((sigma+sigma.conj().T)/2).min(),-2e-14)
                hidden.append((labels,sigma,weight))
            self.assertAlmostEqual(sum(z[2]for z in hidden),1.,places=13)
            max_error=0.
            for settings in product(range(len(a)),repeat=n):
                direct=np.trace(rho@old.tensor([old.obs(a[x])/nu for x in settings[:-1]]+[old.obs(a[settings[-1]])/radius])).real
                local=sum(np.prod([signs[k][settings[j]]for j,k in enumerate(labels)])*
                          np.trace(sigma@old.obs(a[settings[-1]])/radius).real for labels,sigma,_ in hidden)
                max_error=max(max_error,abs(local-direct))
            self.assertLess(max_error,3e-14)
            rows.append(dict(parties=n,hidden_values=len(hidden),largest_correlation_difference=max_error))
        REPORT['explicit_local_model']=rows

    def test_03_exact_margin_with_existing_irregular_witness(self):
        # Edge lengths are sqrt(6120), sqrt(5000), sqrt(3920), all divided by 100.
        lengths=[sqrt_enclosure(F(x,10000))for x in (6120,5000,3920)]
        nu_lo=sum(x[0]for x in lengths)/2;nu_hi=sum(x[1]for x in lengths)/2
        radius_lo,radius_hi=sqrt_enclosure(F(5140,10000))
        self.assertLess(radius_hi*nu_hi**5,1) # No full-correlation violation for N <= 6.
        self.assertLess(radius_hi*nu_hi**18,2) # No ratio 2 for N <= 19.
        self.assertGreater(radius_lo*nu_lo**19,2) # This ceiling ceases to exclude N=20.
        a=[(F('0.70'),F(0)),(F('-0.42'),F('0.56')),(F('-0.28'),F('-0.66'))]
        c=[(F('.492044'),F('.025383')),(F('-.271368'),F('.376503')),(F('-.226537'),F('-.492541'))]
        sign_norms=[]
        for s in product((-1,1),repeat=3):
            z=(sum(sj*z[0]for sj,z in zip(s,c)),sum(sj*z[1]for sj,z in zip(s,c)))
            sign_norms.append(z[0]**2+z[1]**2)
        self.assertLess(max(sign_norms),1)
        u=(sum(qmul(w,(z[0],-z[1]))[0]for w,z in zip(c,a)),
           sum(qmul(w,(z[0],-z[1]))[1]for w,z in zip(c,a)))
        v=(sum(qmul(w,z)[0]for w,z in zip(c,a)),sum(qmul(w,z)[1]for w,z in zip(c,a)))
        b13=(qpow(u,13)[0]+qpow(v,13)[0])/2
        b25=(qpow(u,25)[0]+qpow(v,25)[0])/2
        self.assertGreater(b13,1);self.assertGreater(b25,2)
        REPORT['exact_margin']={'nu_interval':[str(nu_lo),str(nu_hi)],
            'radius_interval':[str(radius_lo),str(radius_hi)],
            'six_party_ceiling_upper_decimal':float(radius_hi*nu_hi**5),
            'nineteen_party_ceiling_upper_decimal':float(radius_hi*nu_hi**18),
            'necessary_parties_for_ratio_two':20,
            'existing_witness_sufficient_parties_for_ratio_two':25,
            'existing_B13_decimal':float(b13),'existing_B25_decimal':float(b25),
            'all_threshold_comparisons_exact_rational':True,
            'claim':'20 is a necessary count for ratio >=2, not the exact minimum; 25 remains a sufficient count.'}

    def test_04_optimal_state_and_marginal_scope_controls(self):
        # A planar CHSH operator may live entirely in the odd-parity GHZ block.
        coeff=np.array([[1,1],[-1,1]],float)
        a=np.array([[1,0],[0,1]],float)
        B=old.bell_operator(a,coeff)
        self.assertAlmostEqual(local_bound(coeff),2)
        self.assertLess(abs(B[0,-1]),1e-14)
        best=ghz(2,-np.angle(B[1,2]),1)
        val=float(np.vdot(best,B@best).real)
        self.assertLess(abs(val-2*np.sqrt(2)),3e-14)
        self.assertLess(abs(np.linalg.norm(B,2)-val),3e-14)
        # The N-fold bound cannot be applied to a one-site marginal term.
        marginal=np.kron(.5*X,I)
        self.assertAlmostEqual(np.linalg.norm(marginal,2),.5)
        self.assertGreater(np.linalg.norm(marginal,2),.5**2)
        # Fixed-axis, zero, and boundary cases must not be fed into polygon inverses.
        for n in (2,3,4):
            collinear=old.tensor([.4*X]*n)
            self.assertAlmostEqual(float(np.linalg.norm(collinear,2)),.4**n)
            self.assertAlmostEqual(float(np.vdot(ghz(n),collinear@ghz(n)).real),.4**n)
        REPORT['scope_controls']={'planar_CHSH_local_bound':2,'operator_norm':val,
            'canonical_even_GHZ_value_every_phase':0,
            'maximizer':'(|01> + exp(i phase)|10>)/sqrt(2)',
            'one_site_marginal_value':.5,'incorrect_N_fold_ceiling':.25,
            'interpretation':'GHZ-type block diagonalization alone does not build a violating inequality for an arbitrary incompatible family.'}

    def test_05_full_probability_distribution_and_even_parity_twirl(self):
        a=source.examples()[0];rows=[]
        for n in (2,3,4):
            psi=ghz(n,.37);rho=np.outer(psi,psi.conj())
            settings=tuple(j%len(a)for j in range(n))
            operators=[old.obs(a[j])for j in settings]
            E=float(np.vdot(psi,old.tensor(operators)@psi).real)
            maxerr=0.
            for signs in product((-1,1),repeat=n):
                prob=float(np.trace(rho@old.tensor([(I+s*A)/2 for s,A in zip(signs,operators)])).real)
                formula=(1+np.prod(signs)*E)/2**n
                maxerr=max(maxerr,abs(prob-formula))
                self.assertGreaterEqual(prob,-1e-14)
            self.assertLess(maxerr,3e-14)
            even=[s for s in product((-1,1),repeat=n)if np.prod(s)==1]
            for k in range(n+1):
                for inds in combinations(range(n),k):
                    average=sum(math.prod(s[i]for i in inds)for s in even)
                    self.assertEqual(average,len(even)if k in (0,n)else 0)
            rows.append({'parties':n,'probability_formula_error':maxerr,
                         'even_parity_patterns':len(even),'twirl_integer_check':True})
        REPORT['full_behavior_not_postselected']=rows


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():parser.error('Refusing to overwrite an existing report')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ConsolidationChecks))
    REPORT.update(status='PASS'if result.wasSuccessful()else'FAIL',tests_run=result.testsRun,
                  scope='Finite identity and scope checks; arbitrary-N conclusions are analytical, not inferred from these tests.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x')as f:json.dump(REPORT,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
    raise SystemExit(0 if result.wasSuccessful()else 1)
if __name__=='__main__':main()
