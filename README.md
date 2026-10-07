# Planar GHZ Bell Amplification

**A constructive GHZ Bell experiment for fixed noisy planar qubit measurements, with the optimal exponential full-correlation amplification rate.**

This repository records one bounded theoretical result. It is an author-side research account, not a claim of exhaustive priority, independent proof review, or demonstrated experimental performance.

## Physical question

Given a prescribed family of noisy qubit detectors, must one search over increasingly complicated entangled states to expose measurement incompatibility? For unbiased binary measurements in a plane through the Bloch-sphere origin, a phase-adjusted GHZ family suffices. Its normalized Bell value has the best possible exponential growth for those same fixed detectors.

Each party uses the same finite family

```math
M_{\pm|x}=\frac{I\pm A_x}{2},\qquad
A_x=a_{x1}\sigma_x+a_{x2}\sigma_y,\qquad \|\mathbf a_x\|\le1.
```

Directions and sharpness may be unequal. Define

```math
\nu=\frac14\operatorname{perimeter}\!\left(\operatorname{conv}\{\pm\mathbf a_x\}\right),
\qquad r=\max_x\|\mathbf a_x\|.
```

Let `R_N` optimize the absolute Bell value divided by its exact local bound over all states and **full-correlation** Bell tensors, with these detectors fixed. For every `N >= 2` and nonzero family,

```math
\frac{\nu^N}{2}\le\mathcal R_N^{\mathrm{GHZ}}
\le\mathcal R_N\le r\nu^{N-1}\le\nu^N,
\qquad
\lim_{N\to\infty}(\mathcal R_N)^{1/N}
=\lim_{N\to\infty}(\mathcal R_N^{\mathrm{GHZ}})^{1/N}=\nu.
```

The [theorem](research/THEOREM.md) gives the explicit Bell coefficients, GHZ phase, degenerate-family cases and party bounds. For the retained irregular three-setting example, a factor-two Bell/local ratio requires at least 20 parties, and the existing 25-party GHZ witness suffices. This is not an exact minimum-party classification.

## Attribution and limits

The compatibility norm, perimeter criterion, parent measurement, and optimal geometric dual certificate are inherited from Yoshino et al., *Joint measurability of coplanar POVMs*, [arXiv:2609.38836v1](https://arxiv.org/abs/2609.38836v1). General eventual activation of incompatible qubit measurements, compatibility-based Bell bounds and symmetric GHZ constructions also have direct predecessors. The proposed additional conclusion is their explicit fixed-family GHZ connection with a matching all-state exponential rate; see [attribution](literature/ATTRIBUTION.md).

Every Bell term uses one outcome from every party. There is no postselection, communication within a trial, extra sharper detector, or uncounted filtering. The result does not cover biased or noncoplanar families, arbitrary marginal-containing Bell expressions, genuine multipartite nonlocality, self-testing, or efficient statistical certification. A compact coefficient formula is not a sample-complexity guarantee.

## Reading map

| Read | Purpose |
|---|---|
| [Model and claims](research/MODEL_AND_CLAIMS.md) | Fixed resources, the central implication and what is not established. |
| [Theorem and proof](research/THEOREM.md) | Main mathematical account; start here for proof review. |
| [Focused contribution review](research/CONTRIBUTION_REVIEW.md) | Proof obligations, the symmetric exponent already in prior work, and the precise retained contribution. |
| [Consolidation assessment](research/ASSESSMENT.md) | Preceding assessment and the scientific-scope boundary. |
| [Attribution and source depths](literature/ATTRIBUTION.md) | Inherited geometry and the recorded primary-source audit. |
| [Verification](VERIFICATION.md) | Four original suites, protected evidence and reproducible commands. |
| [Workspace handoff](WORKSPACE.md) | Exact project identity and next bounded task. |

The [archive](archive/README.md) preserves the complete 81-member consolidation snapshot, including earlier attempts, failed checks and original reports. The focused review adds proof scrutiny and a sharper predecessor comparison; the theorem, scripts, reference reports and scientific tolerances remain unchanged. No third-party PDF is redistributed.

## Reproduce

Use Python 3.13.5 and the pinned scientific packages:

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python tools/verify.py --output .artifacts/local-01
```

The output directory must be new. The runner executes all **18 original groups** (5 consolidation, 3 source dictionary, 5 audit/rate, 5 initial scout) and compares the four reports with the unchanged references. It records exact equality separately from permitted numerical drift; every difference is retained. Read [VERIFICATION](VERIFICATION.md) before changing checks or references.

## Purpose and contact

This repository serves as a record of the work and a guide for the author's self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

The repository retains the owner's [MIT license](LICENSE). Referenced third-party articles remain under their own licenses and are linked, not bundled.
