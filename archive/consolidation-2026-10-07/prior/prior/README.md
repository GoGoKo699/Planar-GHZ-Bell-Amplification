# Planar GHZ audit and optimal full-correlation amplification

**7 October 2026.** Read `AUDIT_AND_RATE.md` first. The original constructive planar-measurement result survives. The added upper bound gives

`nu^N/2 <= R_N^GHZ <= R_N <= nu^N`,

so the optimal exponential Bell-value amplification per party is exactly the planar compatibility norm `nu`. This refers to full-correlation Bell expressions, not arbitrary marginal terms or a statistical confidence exponent.

The all-state upper bound, exact GHZ eigenstate check, fixed-margin party-count scaling, and scope controls are proved in the note. The construction and its underlying geometry remain tightly attributed. A recent primary abstract establishes the planar compatibility criterion, but its full article remains unavailable here, so exact overlap is still unresolved. There is no claim of exhaustive priority, independent scientific review, or readiness for a journal.

## Reproduce

Run with a new output filename:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
  python check_audit_and_rate.py --output NEW_REPORT.json
```

The recorded environment is in `environment.json`. The final five groups passed twice with identical reports. `prior/check_planar_bell.py` also ran unchanged and reproduced its stored five-group report. The proof of the asymptotic rate is analytical; the finite optimizer is only a diagnostic. The largest new dense quantum operator has dimension 32. Exact high-party examples use rational scalar powers.

## Preserved failure

The first new run stopped one group on the optimizer's unsuccessful termination under squared-norm constraints. The implementation was reformulated with equivalent norm constraints and an analytical Jacobian, eliminating duplicate opposite-sign constraints. Original acceptance thresholds, optimizer tolerance, iteration limit, and the success assertion remain unchanged. All full original sign constraints are still verified after optimization. `development/` contains the original checker, diagnostics, and patch; `evidence/first.*` retains the failed run.

The 12 members of the original scout archive are preserved byte-for-byte in `prior/`. No old monitoring project, electronic-decoherence paper, repository, third-party PDF, or font is included. `MANIFEST.json` hashes all package members other than itself.
