# Planar GHZ Bell amplification: consolidated theorem checkpoint

Start with **THEOREM.md** for the self-contained statement and proof, then **ASSESSMENT.md** for inherited results, the proposed contribution and the stopping boundary. This is not an initialized repository.

The result covers fixed finite unbiased binary coplanar qubit measurement families, repeated at all sites. A constructive GHZ value has the same exponential full-correlation Bell scale as the all-state optimum. Compatibility geometry and its explicit dual certificate are attributed to Yoshino et al. The general activation, compatibility-norm and GHZ literature is distinguished inside the account.

The current pass sharpens the finite-N upper bound from nu^N to r nu^(N-1), using the standard N-1-compatible-sites locality fact, and adds scope controls. The asymptotic theorem is unchanged. No new physical model or experiment is introduced.

## Reproduce

With NumPy and SciPy in the recorded environment, run:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python check_consolidation.py --output NEW.json

The script refuses an existing output. Five groups check the source-to-Bell dictionary and refined bound, an explicit N-1-parent hidden-variable model, exact finite-margin certificates, state-optimality/homogeneity scope controls, and the normalized full behavior with its parity twirl. They use at most a 16-by-16 quantum matrix. No large-state optimization is performed.

The final and repeated reports are byte-identical. The earlier source-dictionary (3), audit/rate (5), and initial-scout (5) suites were rerun unchanged and each reproduced its original report byte-for-byte. They remain separately counted and preserved under prior/.

An initial launch exceeded 45 seconds while enumerating a deterministic local maximum with Python loops. Its partial log and script are preserved. Vectorized axiswise contraction computes the same maximum; independently enumerated smaller cases check the identity. The settings, objective, scientific assertions and tolerances were not relaxed. See development/RECORD.md.

The original 54 archive members and user-supplied paper are verified unchanged. The paper itself is not redistributed. No protected repository or unrelated scientific material was used.

**Decision:** retain the bounded theorem and move toward a separate versioned record only after an owner-authorized destination. No repository, manuscript submission, external contact or release is claimed.
