# Repository instructions

## Identity and scope

Work only in `GoGoKo699/Planar-GHZ-Bell-Amplification`. This is the planar GHZ/Bell project, not Partial-Monitoring-Capacity or an electron-preparation project. Repository membership in a broader chat project does not authorize edits to other repositories.

The science is the frozen claim in `research/THEOREM.md`: fixed, unbiased, binary, coplanar qubit POVMs; full correlations; explicit GHZ lower bound; all-state upper bound; optimal exponential factor. Preserve every limitation in `research/MODEL_AND_CLAIMS.md` and the attribution in `literature/ATTRIBUTION.md`. Do not imply exact finite-N optimality or experimental/statistical efficiency.

## Source hierarchy

1. `research/THEOREM.md` and `research/MODEL_AND_CLAIMS.md` define the current claim.
2. `research/ASSESSMENT.md` and `literature/ATTRIBUTION.md` define the bounded contribution and source comparison.
3. `archive/consolidation-2026-10-07/` is immutable historical input. Its final theorem predates repository routing changes; nested earlier notes can be superseded.
4. `work_orders/CURRENT.md` defines the next task. Operational claims require live exact-revision evidence.

## Verification

Run `python -m unittest discover -s tests -v` and `python tools/verify.py --output .artifacts/NEW_RUN`. Never reuse an output directory. The four original science scripts, all reports, failed attempts and archive manifest must remain byte-identical. Scientific assertions and tolerances are not configurable. Cross-environment report comparison is separate: exact non-float values, finite floats under the documented narrow tolerance, with every change recorded.

A passing finite checker does not prove the asymptotic theorem or novelty. Do not update a reference to mask drift or describe numerically matching reports as byte-identical. Inspect source hashes and reports from the actual PR head before merging, and then inspect the separate merged-main run. Use expected-head verification and no forced ref updates.

## Reader-facing material

The single teaching anchor is Gühne et al., *Incompatible measurements in quantum information science*, arXiv:2112.06784v3 (2023). `docs/README.md` maps its PDF section labels to `REVIEW.md`, which teaches the remaining steps locally. The bridge is subordinate to the frozen theorem, not a new scientific claim. Keep Yoshino's 2026 planar geometry and all research-paper attributions distinct from the tutorial background. Keep `llms.txt` aligned with the relevance, scope and authoritative reading order.

Use GitHub-supported displayed math with readable spacing. Distinguish mathematical comparison measurements from supplied experimental resources. Preserve authorship and the owner's MIT license. Use the established Purpose and contact wording; do not add target-journal or publication-plan notices. Do not redistribute third-party articles, fonts, unrelated attachments or protected-project code.

The owner permits repository changes and merging after checks. This does not authorize external contact, release, submission, sharing with collaborators, or changes to visibility/permissions. Stop scope expansion while the contribution is under review.
