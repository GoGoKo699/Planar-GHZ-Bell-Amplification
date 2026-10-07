# Reading guide

**Read one tutorial, then use the repository bridge to reach the fixed-planar GHZ theorem.**

The single anchor is Gühne, Haapasalo, Kraft, Pellonpää and Uola, [*Incompatible measurements in quantum information science*](https://arxiv.org/abs/2112.06784v3), Rev. Mod. Phys. **95**, 011003 (2023). The [author PDF](https://arxiv.org/pdf/2112.06784v3) is freely available. The section labels and printed pages below refer to that version; the HTML rendering uses numerical subsection labels instead of letters.

Basic qubit states, Pauli matrices and tensor products are assumed. Start with [REVIEW](../REVIEW.md) if you already know joint measurability; otherwise follow this short route through the tutorial.

| Tutorial section | Printed pages | What to learn | Repository bridge |
|---|---:|---|---|
| II.A–B: Measurements and instruments; Joint measurability | 3–4 | POVM effects, noisy qubits, one parent and classical postprocessing. Instruments provide context; a sequential-measurement protocol is not used here. | [Measurements](../REVIEW.md#1-noisy-measurements-as-bloch-vectors), [parents](../REVIEW.md#2-one-parent-measurement-and-bell-locality) |
| III.A: Criteria for joint measurability and measurement uncertainty relations | 5–6 | Bloch-vector bias/sharpness and the two-observable compatibility criterion. | [Planar geometry](../REVIEW.md#4-the-inherited-planar-certificate), [orthogonal example](../REVIEW.md#9-a-worked-example-two-noisy-orthogonal-settings) |
| III.B.1–2: Semidefinite programs; Various quantifiers of incompatibility | 6–8 | Feasible primal/dual certificates, strong-duality language and the distinction between noise models. | [Certificate](../REVIEW.md#4-the-inherited-planar-certificate), [operational consequences](../research/OPERATIONAL_CONSEQUENCES.md) |
| III.C: Constructing joint measurements | 8–9 | How a parent can reproduce the requested marginals. The construction methods give context; their auxiliary measurements are not experimental resources added to our model. | [Parents](../REVIEW.md#2-one-parent-measurement-and-bell-locality), [all-state bound](../REVIEW.md#7-joint-parents-bound-every-competing-state) |
| IV.A: Bell nonlocality | 10–11 | Local response functions, correlation expressions, parent-implies-locality and the limits of a direct bipartite incompatibility/nonlocality equivalence. | [Exact local bound](../REVIEW.md#3-the-full-correlation-objective-and-its-local-bound), [converse](../REVIEW.md#7-joint-parents-bound-every-competing-state) |

The review's remaining topics are optional for this result. The repository supplies the parts this source does not contain: the later general planar perimeter/certificate lemma with attribution, the complex tensor/GHZ calculation and the multipartite rescaling argument. No second textbook or review is required by this reading route. The primary papers remain the sources of their specific inherited results.

## Repository map

| Step | Read | What it establishes |
|---|---|---|
| 1 | [README](../README.md) | The physical question, theorem and contribution in compact form. |
| 2 | [REVIEW](../REVIEW.md) | The tutorial-to-theorem bridge, including a noisy two-setting example. |
| 3 | [Model and claims](../research/MODEL_AND_CLAIMS.md) | Fixed resources, exact full-correlation objective and nonclaims. |
| 4 | [Theorem](THEOREM.md) | Complete coefficient construction, GHZ phases, converse and degeneracies. |
| 5 | [Operational consequences](../research/OPERATIONAL_CONSEQUENCES.md) | Finite-rate estimates, fixed-margin party cost and noise interpretation. |
| 6 | [Attribution](../literature/ATTRIBUTION.md), [source audit](../literature/SOURCE_AUDIT.md) | Which ingredients are inherited and what the inspected predecessor passages cover. |
| 7 | [Verification](../VERIFICATION.md) | What finite checks establish and how they relate to the analytical proof. |

The theorem and model define the claim. REVIEW and this guide explain it without changing it. The [archive](../archive/README.md) preserves the earlier exploration and failed attempts; it is not required preparation for the theorem.

## Three useful checkpoints

| Check | Answer |
|---|---|
| Does a parent have to reproduce one chosen state's statistics or every state's statistics? | Every state's statistics. Its effects and postprocessing reproduce the original POVMs. |
| If a witness has a local bound at most one, must its exact local bound equal one? | No. Normalize by the exact positive bound; the three-party orthogonal example has a scaled local bound of the reciprocal square root of two. |
| Does the common Nth-root limit identify the exact best Bell value for each $`N`$? | No. It identifies the optimal exponential factor. The finite bounds retain a constant-factor gap in general. |
