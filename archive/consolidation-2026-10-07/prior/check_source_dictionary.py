#!/usr/bin/env python3
"""Three checks of the dictionary from Yoshino et al. v1 to the existing Bell proof.

Run with a fresh output: python check_source_dictionary.py --output NEW.json
The source identities are attributed to the uploaded paper. These tests do not
establish novelty or independent proof review. No detector family is enlarged.
"""
from __future__ import annotations
import argparse
import importlib.util
from itertools import product
import json
from pathlib import Path
import unittest
import numpy as np
from scipy.spatial import ConvexHull

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('old_audit',ROOT/'prior/check_audit_and_rate.py')
assert spec and spec.loader
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
REPORT={}


def sign_matrices(m: int):
    """Paper B, P, C; used only for nondegenerate polygons, m >= 2."""
    if m<2: raise ValueError('Handle the collinear one-setting case separately.')
    signs=np.array([(1,)+s for s in product((1,-1),repeat=m-1)],dtype=np.int64)
    P=np.zeros((2**(m-1),m),dtype=np.int64)
    for i in range(m):P[2**(m-1-i)-1,i]=1
    C=np.eye(m,dtype=np.int64)
    for i in range(1,m):C[i,i-1]=-1
    C[0,-1]=1
    return signs,P,C


def source_construct(a):
    """Literal nondegenerate X,Y construction after the paper's hull reduction.

    Qhull supplies only the ordering of the polygon. The formulas for X,Y
    use Definitions 3.3--3.7. Old geometry uses a separate monotone-chain hull.
    """
    a=np.asarray(a,dtype=float)
    if a.ndim!=2 or a.shape[1]!=2 or len(a)==0:raise ValueError('Use m by 2 vectors.')
    points=[]; labels=[];seen=set()
    for sign in (1,-1):
        for i,v in enumerate(a):
            key=tuple(sign*v)
            if key not in seen:
                seen.add(key);points.append(sign*v);labels.append((i,sign))
    points=np.array(points)
    if np.linalg.matrix_rank(a)<2:
        raise ValueError('Source matrix test is nondegenerate; segment treated in note.')
    hull=ConvexHull(points);ids=list(hull.vertices)
    assert len(ids)%2==0
    h=len(ids)//2; ids=ids[:h]
    V=points[ids].T
    B,P,C=sign_matrices(h)
    K=V@C
    lengths=np.linalg.norm(K,axis=0)
    Khat=K/lengths
    X=.5*K@P.T;Y=.5*Khat@C.T
    coeff=np.zeros_like(a)
    for j,pid in enumerate(ids):
        i,sign=labels[pid];coeff[i]+=sign*Y[:,j]
    return dict(V=V,B=B,P=P,C=C,K=K,X=X,Y=Y,coeff=coeff,
                lengths=lengths,nu=float(np.sum(lengths)/2),vertices=h,labels=[labels[i]for i in ids])


def examples():
    return [
        np.array([[.70,0],[-.42,.56],[-.28,-.66]]),
        np.array([[.8,0],[0,.6]]),
        np.array([[.76,0],[-.38,.76*np.sqrt(3)/2],[-.38,-.76*np.sqrt(3)/2]]),
        np.array([[.84,.05],[.05,.77],[-.61,.38],[-.5,-.55],[.1,.07]]),
        np.array([[.7,0],[.8,.4],[.3,.4],[.1,.2]]),
        np.array([[.70,0],[-.42,.56],[-.28,-.66],[.70,0],[0,0],[.1,.02]])
    ]


class SourceChecks(unittest.TestCase):
    def test_01_source_sign_matrix_identities(self):
        rows=[]
        for m in range(2,9):
            B,P,C=sign_matrices(m)
            self.assertTrue(np.array_equal(C@P.T@B,2*np.eye(m,dtype=np.int64)))
            self.assertTrue(np.array_equal(P.T@P,np.eye(m,dtype=np.int64)))
            # Twice the coefficient in Section 3.6: alternating 1,-1,...,1.
            twice=C.T@B.T
            self.assertTrue(np.all(twice%2==0))
            Z=twice//2
            self.assertTrue(np.all(np.isin(np.cumsum(Z,axis=0),(0,1))))
            self.assertTrue(np.all(np.sum(Z,axis=0)==1))
            rows.append({'half_hull_vertices':m,'sign_rows':len(B),'identity_exact_integer':True})
        REPORT['source_sign_matrices']=rows

    def test_02_source_primal_dual_equals_previous_geometry(self):
        rows=[]
        for a in examples():
            d=source_construct(a);V,B,X,Y=d['V'],d['B'],d['X'],d['Y']
            old_h,old_nu,_=old.geometry(a)
            self.assertLess(np.linalg.norm(X@B-V),3e-14)
            self.assertAlmostEqual(float(np.sum(np.linalg.norm(X,axis=0))),d['nu'],places=13)
            self.assertLessEqual(np.linalg.norm(Y@B.T,axis=0).max(),1+3e-14)
            for j in np.flatnonzero(np.linalg.norm(X,axis=0)>0):
                self.assertLess(np.linalg.norm((Y@B.T)[:,j]-X[:,j]/np.linalg.norm(X[:,j])),3e-14)
            self.assertLess(np.linalg.norm(d['coeff']-old_h),3e-14)
            self.assertAlmostEqual(d['nu'],old_nu,places=13)
            self.assertAlmostEqual(float(np.sum(a*d['coeff'])),d['nu'],places=13)
            # The normalized source X is an actual joint parent of the scaled vectors.
            parent=[]
            for x in X.T:
                if np.linalg.norm(x)==0:continue
                parent += [(np.linalg.norm(x)*np.eye(2)+old.obs(x))/(2*d['nu']),
                           (np.linalg.norm(x)*np.eye(2)-old.obs(x))/(2*d['nu'])]
            self.assertLess(np.linalg.norm(sum(parent)-np.eye(2)),3e-14)
            self.assertGreaterEqual(min(np.linalg.eigvalsh(p).min()for p in parent),-3e-14)
            rows.append({'input_settings':len(a),'half_hull_vertices':d['vertices'],
                         'source_nu':d['nu'],'previous_nu':old_nu,
                         'dual_dictionary_error':float(np.linalg.norm(d['coeff']-old_h)),
                         'source_sign_bound':float(np.linalg.norm(Y@B.T,axis=0).max())})
        REPORT['source_dictionary']=rows

    def test_03_bell_bridge_from_source_columns(self):
        rows=[]
        for a in examples()[:5]:
            d=source_construct(a);c=d['coeff'][:,0]+1j*d['coeff'][:,1]
            z=a[:,0]+1j*a[:,1];k=d['K'][0]+1j*d['K'][1]
            u=np.dot(c,z.conj());v=np.dot(c,z)
            edge_u=.5*np.sum(d['lengths']);edge_v=.5*np.sum(k*k/d['lengths'])
            self.assertLess(abs(u-edge_u),3e-14)
            self.assertLess(abs(v-edge_v),3e-14)
            self.assertLessEqual(abs(v),d['nu']+3e-14)
            sums=np.array([np.dot(c,s)for s in product((-1,1),repeat=len(a))])
            self.assertLessEqual(max(abs(sums)),1+3e-14)
            T=sum(ci*old.obs(ai)for ci,ai in zip(c,a))
            for n in (2,3,4,5):
                gamma=-n*np.angle(v)/2 if abs(v)>1e-14 else 0.
                TN=old.tensor([T]*n)
                op=(np.exp(1j*gamma)*TN+np.exp(-1j*gamma)*TN.conj().T)/2
                psi=np.zeros(2**n,complex);psi[0]=1/np.sqrt(2)
                psi[-1]=np.exp(-1j*np.angle(op[0,-1]))/np.sqrt(2)
                value=(d['nu']**n+abs(v)**n)/2
                self.assertLess(np.linalg.norm(op@psi-value*psi),2e-12)
                self.assertLess(abs(np.max(abs(np.linalg.eigvalsh(op)))-value),2e-12)
                self.assertLessEqual(d['nu']**n/2,value+2e-12)
                self.assertLessEqual(value,d['nu']**n+2e-12)
                if len(a)<=3 and n<=3:
                    beta=np.array([np.real(np.exp(1j*gamma)*np.prod([c[i]for i in ix]))
                                   for ix in product(range(len(a)),repeat=n)]).reshape((len(a),)*n)
                    self.assertLess(np.linalg.norm(old.bell_operator(a,beta)-op),2e-12)
                    self.assertLessEqual(old.local_bound(beta),1+2e-12)
                rows.append({'settings':len(a),'parties':n,'dimension':len(op),
                             'source_dual_ghz_value':float(value)})
        REPORT['bell_bridge']=rows


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    if args.output.exists():p.error('Refusing to overwrite an existing evidence report.')
    run=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(SourceChecks))
    REPORT.update(status='PASS'if run.wasSuccessful()else'FAIL',tests_run=run.testsRun,
        scope='Dictionary/normalization checks; no new compatibility criterion, no new Bell theorem, no priority proof.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x')as f:json.dump(REPORT,f,sort_keys=True,indent=2,allow_nan=False);f.write('\n')
    raise SystemExit(0 if run.wasSuccessful()else 1)

if __name__=='__main__':main()
