# Model and claim hierarchy

## Fixed experiment

Each party holds one qubit and chooses from the same finite family of unbiased binary POVMs. Their Bloch vectors lie in one plane through the origin and have length at most one. The family is fixed as the number of parties grows. State and inequality design know the family and its plane. Outcomes are always retained; no filtering, communication during the trial, postselection, extra setting or privileged sharper detector is provided.

The Bell objective is the absolute full-correlation value divided by its exact local absolute bound. Every tensor term contains one outcome from each of the N parties. The objective is not artificially floored at one; compatible noisy detectors can have a ratio below one.

## Main added implication

For `nu = perimeter(conv{+/- a_x})/4` and `r = max ||a_x||`, the [theorem](../docs/THEOREM.md) constructs Bell coefficients and a phase-adjusted canonical GHZ state with value at least `nu^N/2`, while every state and full-correlation tensor obeys the ceiling `r nu^(N-1)`. Their Nth-root limits equal `nu`.

This gives constructive GHZ activation whenever `nu > 1`, the exact asymptotic amplification factor, and necessary/sufficient finite-party bounds for a fixed violation margin. Those are consequences of one connection, not separate proposed discoveries. The zero and collinear cases are explicit in the theorem.

## Inherited inputs

Yoshino et al. supply the full planar compatibility norm, perimeter criterion, redundant-setting reduction, parent and optimal dual certificate. Plavala, Guhne and Quintino supply general incompatible-qubit activation and ask about familiar state families and party counts. Compatibility norm bounds, complex GHZ correlation algebra and regular-polygon amplification rates for every setting count are also inherited. [ATTRIBUTION](../literature/ATTRIBUTION.md) and the [source audit](../literature/SOURCE_AUDIT.md) identify the inspected passages.

## What the checks establish

Finite exact arithmetic certifies selected Bell witnesses and party bounds. Small dense matrices check normalizations, parent decompositions, complementary-bitstring blocks and scope counterexamples. The largest archived dense check has dimension 32. The arbitrary-party result rests on the analytical proof, not these examples.

The chosen GHZ state maximizes our constructed functional. It need not maximize an arbitrary fixed planar functional: another complementary-bitstring block may be optimal. All-state exponential optimality is not exact finite-party optimality.

## Explicit nonclaims

No exact smallest party count for an arbitrarily small violation; no theorem for biased/noncoplanar POVMs or arbitrary marginal terms; no genuine N-party nonlocality, entanglement-depth bound, self-testing, cryptographic rate, finite-sample efficiency, detector no-click robustness, or implemented GHZ preparation. Global white-state noise is not independent detector noise. The pure full-correlation behavior is normalized and involves no postselection.

No external independent proof review, exhaustive priority clearance or external acceptance has occurred. The [internal contribution review](CONTRIBUTION_REVIEW.md), [source audit](../literature/SOURCE_AUDIT.md) and [operational consequences](OPERATIONAL_CONSEQUENCES.md) record the completed scientific prerequisites. The [README](../README.md) provides the compact exposition. The scientific scope remains frozen.
