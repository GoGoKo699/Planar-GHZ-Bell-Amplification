# Execution record

The first launch of check_consolidation.py hit the explicit 45-second execution limit during its first group. It was calling the earlier checker’s intentionally simple exhaustive local-bound routine on a five-setting four-party tensor, repeatedly. No scientific assertion had failed, and no complete JSON report was written. The partial evidence/first.log and development/check_initial_timeout.py are retained.

The final script computes the same absolute maximum through vectorized contraction over sign tables. One global sign per party can be fixed because it changes only the overall sign of a full-correlation expression. Four smaller coefficient tensors are checked against the original complete sign enumeration. The actual measurement families, number of parties, coefficient tensors for the substantive checks, comparison thresholds, and model are unchanged. No tolerance was loosened. The patch is retained.

Both final executions passed all five groups. Their reports are byte-identical. The previous three suites (3+5+5 groups) reran unchanged and each reproduced its original report exactly. Finite checks are not a proof of the arbitrary-N theorem or independent review.

Three requested primary-PDF screenshots failed with cache-miss errors. Technical comparisons use primary parsed mathematical text; no values from their unviewed plots/tables are used. The supplied planar-compatibility paper was available in full text, and its earlier visual/dictionary audit remains in the preserved record. The unrelated electronic-decoherence PDF was not used.
