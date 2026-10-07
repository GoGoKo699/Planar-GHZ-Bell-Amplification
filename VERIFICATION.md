# Verification policy

## Run the source, not a rewritten test

Use Python 3.13.5 with `requirements.txt`. Run:

```bash
python -m unittest discover -s tests -v
python tools/verify.py --output .artifacts/local-01
```

The output path must not exist and cannot be inside the protected archive. The science runs in separate processes with one BLAS/OpenMP thread and bytecode writing disabled. No network call is made by the verification runner.

| Original suite, relative to the protected snapshot | Groups | Canonical reference |
|---|---:|---|
| `check_consolidation.py` | 5 | `evidence/repeat.json` |
| `prior/check_source_dictionary.py` | 3 | `prior/evidence/repeat.json` |
| `prior/prior/check_audit_and_rate.py` | 5 | `prior/prior/evidence/repeat.json` |
| `prior/prior/prior/check_planar_bell.py` | 5 | `prior/prior/prior/evidence/repeat.json` |

The sum is 18. Infrastructure tests are counted separately and do not add scientific claims. Old packaging scripts and deliberately failed developmental scripts are preserved but not executed in the success suite.

## Exact preservation

The runner checks the imported top manifest against its independently pinned SHA-256 in `provenance/IMPORT.json`, then checks all 80 listed members and the exact 81-file set. Nested manifests are covered as immutable members. It verifies the original license and the permitted active-document derivations. No reference, historical failure, code or scientific tolerance may be changed to make a run pass.

The uploaded compatibility PDF is recorded by SHA-256 but intentionally absent from the repository. It is not a runtime dependency. No publisher PDF, unrelated attachment or font is redistributed.

## Cross-environment numerical comparison

Original assertions execute unchanged. Independently, reports must have identical structure, strings, integer counts, Boolean values and exact rational certificates. Finite floating-point fields are compared with `abs(actual-reference) <= 1e-13 + 1e-12*abs(reference)`. NaNs and infinities fail. This narrow report-drift policy is not a relaxation of any scientific assertion. Every changed field, both values and absolute difference are saved; exact report-byte equality is recorded separately. A reviewer must inspect those differences before merging.

Numerical equivalence must never be called byte equality unless the downloaded report bytes actually agree. An unsupported platform or failed optimizer is a failed run, not permission to alter the source.

## Interpreting the archived rational witness

This interpretation applies to the [initial-scout checker](archive/consolidation-2026-10-07/prior/prior/prior/check_planar_bell.py) and [its canonical report](archive/consolidation-2026-10-07/prior/prior/prior/evidence/repeat.json).

The definition of $`\mathcal R_N`$ uses the exact local absolute bound $`L(\beta)`$. The constructive proof only needs $`L(\beta)\le1`$; it never requires equality. Its positive quantum value ensures the Bell tensor is nonzero, and local sign strategies span the tensor space, so $`L(\beta)>0`$.

The original rational witness report's field `local_absolute_bound = 1` denotes the certified conservative bound used by that checker. It is not an assertion that the exact local maximum equals one. Indeed its rounded one-site coefficients satisfy

```math
\max_s\left|\sum_xc_xs_x\right|^2
=\frac{499999562849}{500000000000}<1.
```

Their $`N`$-site local bound is therefore strictly below one. Dividing by its exact value can only improve the archived sufficient violations. The rational coefficients, the geometric coefficients used for the all-$`N`$ identity, and their corresponding values remain distinct. No archived script, report, or certificate is corrected or replaced by this explanation.


## Reading-page presentation

The protected scientific theorem retains its original bytes and hash. `python tools/render_docs.py` generates [its reading view](docs/THEOREM.md), using portable math formatting and exact editorial substitutions that remove historical workflow notices and make their surrounding prose self-contained. Each editorial anchor must occur exactly once; unexpected source drift fails the transformation. The seven equation numbers use ordinary math text instead of the renderer-incompatible numbered-table macro. Infrastructure tests compare all 24 theorem equations after these declared typography changes and its unchanged bibliography with the preserved source, retain the scientific scope statements, and check its pinned hash.

Displayed equations use fenced `math` blocks to preserve literal TeX backslashes before set braces. The checker rejects bare double-dollar display delimiters on current reading pages; ordinary code examples and protected historical sources are exempt. Prose uses GitHub's dollar-backtick inline math syntax for Greek letters, subscripts, powers and inequalities. `python tools/render_docs.py --check` checks synchronization without rewriting. The verification runner also checks inline delimiters, detects common mathematical expressions left as code or ASCII text, and rejects the renderer-incompatible operator and equation-tag macros in current reading-page equations. These presentation checks are infrastructure, separate from the 18 scientific groups.

## Hosted workflow and review

The workflow checks out the actual PR head SHA for pull-request runs and the actual pushed SHA for main runs. It pins Python, scientific dependencies and action commit IDs. It has read-only repository permissions, contains no secrets and does not write back to the repository.

Each run uploads raw execution logs, fresh reports, environment information, the comparison results and SHA-256 values of all tracked source files. The workflow job summary gives a compact receipt. Review the exact PR diff and source-matched artifact before merge; inspect the separate actual merged-main workflow after merge. Use the expected PR-head SHA when merging.

The finite suites check witnesses, examples and source preservation. The all-party result rests on the analytical theorem; [MODEL_AND_CLAIMS](research/MODEL_AND_CLAIMS.md) specifies the limits of the evidence.
