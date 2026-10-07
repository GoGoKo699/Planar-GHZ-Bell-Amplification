#!/usr/bin/env python3
"""Bounded checks for a constructive planar-measurement GHZ Bell witness.

Run: python check_planar_bell.py --output NEW.json
No old scientific code, Bell experiment, or many-body simulation is imported.
The irregular 13-party inequality is certified in exact rational arithmetic.
The general theorem is proved in SCOUT.md, not by the finite checks.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from itertools import combinations, product
import json
import math
from pathlib import Path
import unittest

import numpy as np
from scipy.optimize import linprog
from scipy.spatial import ConvexHull

REPORT: dict[str, object] = {}
X = np.array([[0,1],[1,0]], complex)
Y = np.array([[0,-1j],[1j,0]], complex)
I = np.eye(2, dtype=complex)
A_RAT = [(F(7,10),F(0)),(F(-21,50),F(14,25)),(F(-7,25),F(-33,50))]
H_RAT = [(F(492044,10**6),F(25383,10**6)),
         (F(-271368,10**6),F(376503,10**6)),
         (F(-226537,10**6),F(-492541,10**6))]


def cmul(a: tuple[F,F], b: tuple[F,F]) -> tuple[F,F]:
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def cpow(a: tuple[F,F], n: int) -> tuple[F,F]:
    out=(F(1),F(0))
    for _ in range(n): out=cmul(out,a)
    return out


def conj(a: tuple[F,F]) -> tuple[F,F]:
    return a[0],-a[1]


def csum(terms) -> tuple[F,F]:
    terms=list(terms)
    return sum((v[0] for v in terms),F()),sum((v[1] for v in terms),F())


def arr(vs):
    return np.array([[float(x),float(y)]for x,y in vs])


def polygon_data(a: np.ndarray):
    """Geometric witness and zonotope generators; numerical diagnostic only."""
    a=np.asarray(a,float)
    if a.ndim!=2 or a.shape[1]!=2 or len(a)<2:
        raise ValueError('Need a finite list of two-component Bloch vectors.')
    if np.max(np.linalg.norm(a,axis=1))>1+1e-12:
        raise ValueError('Unphysical Bloch vector.')
    points=np.r_[a,-a]
    hull=ConvexHull(points)
    vertices=points[hull.vertices]
    edges=np.roll(vertices,-1,axis=0)-vertices
    lengths=np.linalg.norm(edges,axis=1)
    tangents=edges/lengths[:,None]
    h=np.zeros_like(a)
    for i,index in enumerate(hull.vertices):
        gradient=(tangents[i-1]-tangents[i])/4
        h[index%len(a)]+=gradient*(1 if index<len(a) else -1)
    return h, float(lengths.sum()/4), edges[:len(edges)//2]/2


def observable(a): return a[0]*X+a[1]*Y


def kron_all(items):
    out=np.array([[1]],complex)
    for x in items:out=np.kron(out,x)
    return out


class PlanarBellChecks(unittest.TestCase):
    def test_geometric_parent_and_dual_witness(self):
        # Includes irregular directions, unequal radii and a redundant inner vector.
        cases=[arr(A_RAT), np.array([[.7,0],[-.35,.7*np.sqrt(3)/2],[-.35,-.7*np.sqrt(3)/2]]),
               np.array([[.81,.1],[-.2,.65],[-.41,-.54],[.11,-.72],[.06,.02]])]
        rows=[]
        for a in cases:
            h,nu,gens=polygon_data(a)
            signs=np.array(list(product((-1,1),repeat=len(a))))
            support=np.max(np.linalg.norm(signs@h,axis=1))
            self.assertLessEqual(support,1+3e-15)
            self.assertLess(abs(np.sum(a*h)-nu),3e-15)
            self.assertLess(abs(np.linalg.norm(gens,axis=1).sum()-nu),3e-15)
            # Joint parent for the uniformly rescaled family a/nu.
            parent=[]
            for g in gens:
                for sign in (1,-1):parent.append((np.linalg.norm(g)*I+sign*observable(g))/(2*nu))
            self.assertLess(np.linalg.norm(sum(parent)-I),3e-15)
            self.assertGreater(min(np.linalg.eigvalsh(p).min()for p in parent),-2e-15)
            for point in a:
                # K = sum_i [-g_i,g_i]. Obtain postprocessing coefficients in [-1,1].
                sol=linprog(np.zeros(len(gens)),A_eq=gens.T,b_eq=point,bounds=[(-1,1)]*len(gens),method='highs')
                self.assertTrue(sol.success)
                out=np.zeros((2,2),complex)
                for j,t in enumerate(sol.x):out+=t*(parent[2*j]-parent[2*j+1])
                self.assertLess(np.linalg.norm(out-observable(point/nu)),3e-14)
            rows.append({'settings':len(a),'perimeter_over_four':nu,
                         'dual_pairing':float(np.sum(a*h)),'largest_sign_sum_norm':float(support),
                         'parent_outcomes':len(parent)})
        REPORT['parent_and_dual']={'cases':rows,'scope':'Finite numerical checks of the independently proved norm/perimeter identity and a joint parent after uniform rescaling. Linear programming is only used to find postprocessing coefficients.'}

    def test_exact_irregular_thirteen_party_certificate(self):
        self.assertTrue(all(x*x+y*y<=1 for x,y in A_RAT))
        norm2=[]
        for signs in product((-1,1),repeat=3):
            totals=[sum((signs[i]*H_RAT[i][j] for i in range(3)),F())for j in range(2)]
            n2=sum(t*t for t in totals)
            self.assertLessEqual(n2,1)
            norm2.append(n2)
        pair_margins=[]
        for i,j in combinations(range(3),2):
            a,b=A_RAT[i],A_RAT[j]
            aa=sum(t*t for t in a);bb=sum(t*t for t in b);ab=sum(a[k]*b[k]for k in range(2))
            margin=1+ab*ab-aa-bb
            self.assertGreaterEqual(margin,0)
            pair_margins.append({'pair':[i+1,j+1],'compatibility_margin':str(margin)})
        # Complex u is the upper-right matrix element of K=sum c_x A_x.
        u=csum(cmul(h,conj(a))for h,a in zip(H_RAT,A_RAT))
        v=csum(cmul(h,a)for h,a in zip(H_RAT,A_RAT))
        self.assertGreater(u[0],1)
        n=13
        up=cpow(u,n);vp=cpow(v,n)
        # gamma=0 and the ordinary real GHZ state, with no fitted state phase.
        expectation=(up[0]+vp[0])/2
        self.assertGreater(expectation,1)
        self.assertGreater(F(49,50)*expectation,1)
        REPORT['exact_irregular_example']={
          'bloch_vectors':[[str(x),str(y)]for x,y in A_RAT],
          'witness_vectors':[[str(x),str(y)]for x,y in H_RAT],
          'all_eight_sign_bounds_squared':list(map(str,norm2)),
          'pairwise_joint_measurability':pair_margins,
          'u':[str(x)for x in u],'v':[str(x)for x in v],
          'number_of_parties':n,'bell_phase':0,'state':'(|0>^13+|1>^13)/sqrt(2)',
          'local_absolute_bound':1,'quantum_value_exact':str(expectation),
          'quantum_value_decimal':float(expectation),'two_percent_white_noise_value':float(F(49,50)*expectation),
          'scope':'Exact rational certificate, not minimum party count, sample complexity, device calibration or experimental verification.'}

    def test_direct_bell_operator_and_local_strategies(self):
        a=arr(A_RAT);h=arr(H_RAT);cs=h[:,0]+1j*h[:,1]
        ops=[observable(v)for v in a];K=sum(c*op for c,op in zip(cs,ops))
        u,v=K[0,1],K[1,0]
        phase_v=np.angle(v);rows=[]
        local_values=np.array([sum(s*c for s,c in zip(signs,cs))for signs in product((-1,1),repeat=3)])
        for n in (2,3,4):
            gamma=-(n*(np.angle(u)+phase_v))/2
            direct=np.zeros((2**n,2**n),complex)
            for settings in product(range(3),repeat=n):
                coeff=np.real(np.exp(1j*gamma)*np.prod(cs[list(settings)]))
                direct+=coeff*kron_all([ops[x]for x in settings])
            tensor=kron_all([K]*n)
            compact=(np.exp(1j*gamma)*tensor+np.exp(-1j*gamma)*tensor.conj().T)/2
            self.assertLess(np.linalg.norm(direct-compact),3e-14)
            b=compact[0,-1]
            ghz=np.zeros(2**n,complex);ghz[0]=1/np.sqrt(2);ghz[-1]=np.exp(-1j*np.angle(b))/np.sqrt(2)
            observed=float(np.real(np.vdot(ghz,compact@ghz)))
            analytic=(abs(u)**n+abs(v)**n)/2
            self.assertLess(abs(observed-analytic),3e-14)
            local=max(abs(np.real(np.exp(1j*gamma)*np.prod(vals)))for vals in product(local_values,repeat=n))
            self.assertLessEqual(local,1+1e-13)
            rows.append({'parties':n,'local_deterministic_strategies':8**n,'local_maximum_abs':float(local),
                         'GHZ_expectation':observed,'closed_form':float(analytic),'dimension':2**n})
        REPORT['direct_operator']=rows

    def test_known_trine_family_and_constructive_party_bounds(self):
        # A regular-polygon control, NOT claimed as an original inequality family.
        cs=.5*np.exp(2j*np.pi*np.arange(3)/3)
        vertices=np.array([sum(s*c for s,c in zip(sign,cs))for sign in product((-1,1),repeat=3)])
        for n in (2,3,4):
            local=max(abs(np.real(np.exp(1j*np.pi/6)*np.prod(v)))for v in product(vertices,repeat=n))
            self.assertLess(abs(local-np.sqrt(3)/2),5e-14)
        rows=[]
        for eta in (F(67,100),F(7,10),F(4,5)):
            amplification=3*eta/2;n=2
            while amplification**(2*n)<=3:n+=1
            self.assertGreater(amplification**(2*n),3)
            if n>2:self.assertLessEqual(amplification**(2*(n-1)),3)
            rows.append({'visibility':str(eta),'parties_sufficient_for_this_inequality':n,
                         'violation_ratio':float(amplification)**n/np.sqrt(3)})
        self.assertEqual(rows[0]['parties_sufficient_for_this_inequality'],111)
        # An incompatible family can approach compatibility, making this bound diverge.
        bounds=[]
        for eps in (F(1,10),F(1,100),F(1,1000)):
            nu=1+eps;n=2
            while nu**n<=2:n+=1
            self.assertGreater(nu**n,2)
            bounds.append({'nu_minus_one':str(eps),'sufficient_N':n})
        REPORT['known_trine_control']={'examples':rows,'general_norm_bound':bounds,
            'scope':'Sufficient counts for the explicit chosen Bell witnesses only, not globally optimal Bell inequalities or minimum quantum resources.'}

    def test_scaling_parent_locality_and_noise_boundaries(self):
        a=arr(A_RAT);h,nu,gens=polygon_data(a)
        # Convex mixtures of fully local deterministic response tables stay local.
        parent=[]
        mus=np.linalg.norm(gens,axis=1)/nu
        for g,mu in zip(gens/nu,mus):
            parent.extend([(mu*I+observable(g))/2,(mu*I-observable(g))/2])
        responses=[]
        for p in a/nu:
            sol=linprog(np.zeros(len(gens)),A_eq=(gens/nu).T,b_eq=p,bounds=[(-1,1)]*len(gens),method='highs')
            self.assertTrue(sol.success)
            responses.append(np.array([s*t for t in sol.x for s in (1,-1)]))
        rho=np.zeros((4,4),complex);state=np.array([1,0,0,1])/np.sqrt(2);rho=np.outer(state,state)
        joint=np.array([[np.real(np.trace(rho@np.kron(g,k)))for k in parent]for g in parent])
        self.assertGreater(joint.min(),-1e-14);self.assertLess(abs(joint.sum()-1),2e-14)
        for i,j in product(range(3),repeat=2):
            q=float(np.real(np.trace(rho@np.kron(observable(a[i]/nu),observable(a[j]/nu)))))
            l=float(responses[i]@joint@responses[j])
            self.assertLess(abs(q-l),3e-14)
        # White state noise is not detector sharpness; local noise compounds with N.
        ex=REPORT['exact_irregular_example']['quantum_value_decimal']
        self.assertGreater(.98*ex,1)
        self.assertLess(.95*ex,1)
        self.assertLess(.99**13*ex,1)
        REPORT['scope_controls']={'uniformly_rescaled_compatible_family_verified':True,
              'white_state_noise_threshold_for_selected_bound':1-1/ex,
              'two_percent_global_white_noise_still_violates':True,
              'one_percent_extra_independent_detector_shrinkage_not_certified_by_this_witness':True,
              'counterfactual_resources_excluded':['postselection','helper communication during a trial','additional measurement settings','noncoplanar/bias generalization','experiment or optimized sample bound']}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():parser.error(f'Refusing existing report: {args.output}')
    # The fifth test uses the explicitly generated rational-certificate scalar.
    names=['test_geometric_parent_and_dual_witness','test_exact_irregular_thirteen_party_certificate',
           'test_direct_bell_operator_and_local_strategies','test_known_trine_family_and_constructive_party_bounds',
           'test_scaling_parent_locality_and_noise_boundaries']
    result=unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(PlanarBellChecks(n)for n in names))
    REPORT.update(status='PASS'if result.wasSuccessful()else'FAIL',tests_run=result.testsRun,
                  scope='Author-side finite identities and an exact rational Bell certificate. No general-proof, priority or apparatus certificate is inferred from test counts.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x',encoding='utf-8')as f:json.dump(REPORT,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
    raise SystemExit(0 if result.wasSuccessful()else 1)

if __name__=='__main__':main()
