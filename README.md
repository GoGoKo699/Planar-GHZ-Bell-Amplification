# Planar GHZ Bell Amplification

**Fixed noisy planar qubit measurements determine an optimal exponential Bell-amplification rate. An explicit GHZ construction attains it.**

| Read next | Purpose |
|---|---|
| [Reading guide](docs/README.md) · [Tutorial-to-theorem bridge](REVIEW.md) | Learn from one external review and local worked calculations |
| [Theorem and proof](docs/THEOREM.md) · [Model and claims](research/MODEL_AND_CLAIMS.md) | Check the construction, converse, resources and normalization |
| [Operational consequences](research/OPERATIONAL_CONSEQUENCES.md) | Interpret finite-party costs and noise |
| [Source audit](literature/SOURCE_AUDIT.md) · [Attribution](literature/ATTRIBUTION.md) | Separate inherited ingredients from the additional implication |
| [Verification](#evidence-and-reproduction) | Inspect executable evidence, certificate interpretation and the comparison policy |
| [LLM guide](llms.txt) | Find relevant questions and authoritative files |

## The fixed-detector question

Suppose every party receives one qubit and uses the same prescribed collection of noisy measurements. The measurement directions and sharpness are known and remain fixed as more parties are added. Can a familiar entangled state reveal every amount of measurement incompatibility? How quickly can the Bell value grow, even if we optimize over every possible state?

For finite families of unbiased binary qubit measurements in a plane through the Bloch-sphere origin, both answers follow from one geometric quantity. A phase-adjusted GHZ state exposes every incompatible family, and its normalized **full-correlation** Bell value has the best possible exponential rate for those same measurements.

## One theorem

Write the measurements in their common equatorial basis as

```math
M_{s|x}=\frac{I+sA_x}{2},\qquad s\in\{-1,1\},
```

```math
A_x=a_{x1}\sigma_x+a_{x2}\sigma_y,\qquad \|\mathbf a_x\|\le1.
```

Directions may be irregular and sharpness unequal. Let

```math
K=\mathrm{conv}\{\pm\mathbf a_x\},\qquad
\nu=\frac{\mathrm{perimeter}(K)}4,\qquad
r=\max_x\|\mathbf a_x\|.
```

For a segment, perimeter means twice its length. The inherited planar compatibility theorem says that these measurements admit a joint parent exactly when $`\nu\le1`$. Such a parent is one measurement whose outcomes can be classically processed to reproduce any setting in the family.

A full-correlation Bell expression combines products of one outcome from **every** party. Normalize its absolute expectation by its exact local absolute bound: the largest value obtainable with shared randomness and local responses. Let $`\mathcal R_N`$ optimize this ratio over all states and all nonzero such expressions, and let $`\mathcal R_N^{\mathrm{GHZ}}`$ restrict the state to

```math
|\mathrm{GHZ}_{N,\varphi}\rangle
=\frac{|0\rangle^{\otimes N}+e^{i\varphi}|1\rangle^{\otimes N}}{\sqrt2}
```

in the common plane-normal basis, optimizing the relative phase and Bell expression. For every $`N\ge2`$ and nonzero family,

```math
\boxed{\frac{\nu^N}{2}\le\mathcal R_N^{\mathrm{GHZ}}
\le\mathcal R_N\le r\nu^{N-1}\le\nu^N.}
```

Consequently,

```math
\boxed{\lim_{N\to\infty}(\mathcal R_N^{\mathrm{GHZ}})^{1/N}
=\lim_{N\to\infty}(\mathcal R_N)^{1/N}=\nu.}
```

If $`\nu>1`$, the explicit lower bound eventually exceeds the local threshold of one. If $`\nu\le1`$, joint measurability rules out Bell violation for every state. Thus, within this class, incompatibility is exactly what can be amplified by sufficiently many GHZ parties.

The root limit identifies the exponential rate, not the exact optimum at a fixed party number. Our explicit construction is within a factor of two of the optimal normalized full-correlation value. That comparison concerns Bell values, not the excess above one or sampling cost. Ratios are not floored at one. The all-zero family gives zero; a nonzero collinear family gives exactly $`\mathcal R_N=\mathcal R_N^{\mathrm{GHZ}}=r^N`$ with $`\nu=r`$.

## Why the bounds meet

**Geometry supplies coefficients.** Yoshino et al.'s inherited optimal planar dual certificate has bounded signed sums. Encoding its vectors as complex numbers produces a two-by-two matrix whose useful entry is the perimeter factor.

**Tensor products produce a GHZ witness.** Real parts of products of those complex coefficients give a Bell expression. Every deterministic local value factors into the bounded one-site sums, so the local absolute bound is at most one. Aligning the Bell and GHZ phases gives the lower bound; dividing by the exact local bound can only improve it. The selected GHZ state maximizes this constructed operator. An arbitrary fixed planar functional can instead be maximized in another complementary-bitstring block.

**Joint parents bound every state.** In a mathematical comparison, rescale the first $`N-1`$ sites by $`1/\nu`$ to compatible families and the last site by $`1/r`$ to valid binary observables. Parent outcomes and the last site's conditional Born probabilities form a local model. Restoring the scales gives the ceiling $`r\nu^{N-1}`$. These comparison measurements are proof devices, not extra experimental resources. Taking Nth roots yields the common limit.

The [tutorial-to-theorem bridge](REVIEW.md) works through the algebra and a noisy two-setting example. [Theorem Sections 3–5](docs/THEOREM.md#3-inherited-geometric-input) supply the authoritative construction and converse.

## One tutorial, then this result

The selected learning anchor is:

> O. Gühne, E. Haapasalo, T. Kraft, J.-P. Pellonpää and R. Uola,
> **Incompatible measurements in quantum information science**,
> *Reviews of Modern Physics* **95**, 011003 (2023).
>
> [Author review, arXiv:2112.06784v3](https://arxiv.org/abs/2112.06784v3) ·
> [Published article](https://doi.org/10.1103/RevModPhys.95.011003)

The [reading guide](docs/README.md) maps its POVM, joint-measurement, duality and Bell-locality sections to this repository. The [bridge](REVIEW.md) supplies the exact planar certificate, Bell/GHZ calculation and rate argument locally. Its noisy orthogonal-measurement example leads into the arbitrary-family result. No second external tutorial is required. Research papers remain theorem references; the 2023 review does not contain the 2026 planar perimeter theorem.

## What this adds to existing results

Yoshino et al., [*Joint measurability of coplanar POVMs*](https://arxiv.org/abs/2609.38836v1), supply the entire compatibility geometry, perimeter criterion, parent and optimal dual certificate. General qubit incompatibility activation, compatibility-based Bell bounds and complex GHZ correlation methods also have direct predecessors. Nagata, Laskowski and Paterek's [2006 multisetting construction](https://arxiv.org/abs/quant-ph/0601107v2) already contains the perimeter exponent for every regular setting polygon; Designolle et al. supply optimized symmetric constructions. The [source audit](literature/SOURCE_AUDIT.md) makes the fixed-detector phase comparison explicit.

The additional implication is the conversion of **every fixed planar family** in the declared class into explicit Bell coefficients and a phase-adjusted canonical GHZ state, together with a matching exponential bound over **all states**. General activation alone does not prescribe a full-correlation witness or its rate. The argument is a short connection between established ingredients. [Operational consequences](research/OPERATIONAL_CONSEQUENCES.md) give the finite logarithmic-rate estimate, fixed-margin party cost and precise noise interpretation; the [attribution record](literature/ATTRIBUTION.md) identifies the source passages.

## One finite-party illustration

For the irregular three-setting family in [Section 6](docs/THEOREM.md#6-a-fixed-violation-margin-and-an-exact-example), any full-correlation Bell/local ratio of at least two requires at least **20 parties**, while the **25-party GHZ witness** exceeds two. These are necessary and sufficient bounds, not an exact minimum. The example illustrates the theorem; the arbitrary-party result rests on its analytical proof.

## Scope and reading map

The state is supplied before the measurement choices. Every outcome is retained, with no communication during a trial, postselection, filtering, extra setting or sharper detector. State and inequality design use the known measurement family and plane.

The [model specification](research/MODEL_AND_CLAIMS.md) gives the assumptions and normalization. The [operational consequences](research/OPERATIONAL_CONSEQUENCES.md) distinguish global white-state noise from independent detector noise and give finite-party bounds for a fixed violation margin.

The [reading guide](docs/README.md#repository-map) locates the proof, operational consequences, source comparisons and verification policy. The [LLM guide](llms.txt) gives relevant research questions, search terms and the authoritative reading order.

## Evidence and reproduction

Use Python 3.13.5 and the pinned scientific packages:

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python tools/verify.py --output .artifacts/local-01
```

The output directory must be new. The runner executes all **18 original scientific groups** and compares the four reports with their unchanged references. Infrastructure tests are counted separately. Exact byte equality is distinguished from permitted floating-point drift, and every changed field is recorded. The [verification policy](VERIFICATION.md) explains these comparisons.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

The repository retains the owner's [MIT license](LICENSE). Referenced third-party articles remain under their own licenses and are linked, not bundled.
