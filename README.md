# Planar GHZ Bell Amplification

**Fixed noisy planar qubit measurements determine an optimal exponential Bell-amplification rate. An explicit GHZ construction attains it.**

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
K=\operatorname{conv}\{\pm\mathbf a_x\},\qquad
\nu=\frac{\operatorname{perimeter}(K)}4,\qquad
r=\max_x\|\mathbf a_x\|.
```

For a segment, perimeter means twice its length. The inherited planar compatibility theorem says that these measurements admit a joint parent exactly when `nu <= 1`. Such a parent is one measurement whose outcomes can be classically processed to reproduce any setting in the family.

A full-correlation Bell expression combines products of one outcome from **every** party. Normalize its absolute expectation by its exact local absolute bound: the largest value obtainable with shared randomness and local responses. Let `R_N` optimize this ratio over all states and all nonzero such expressions, and let `R_N^GHZ` restrict the state to

```math
|\mathrm{GHZ}_{N,\varphi}\rangle
=\frac{|0\rangle^{\otimes N}+e^{i\varphi}|1\rangle^{\otimes N}}{\sqrt2}
```

in the common plane-normal basis, optimizing the relative phase and Bell expression. For every `N >= 2` and nonzero family,

```math
\boxed{\frac{\nu^N}{2}\le\mathcal R_N^{\mathrm{GHZ}}
\le\mathcal R_N\le r\nu^{N-1}\le\nu^N.}
```

Consequently,

```math
\boxed{\lim_{N\to\infty}(\mathcal R_N^{\mathrm{GHZ}})^{1/N}
=\lim_{N\to\infty}(\mathcal R_N)^{1/N}=\nu.}
```

If `nu > 1`, the explicit lower bound eventually exceeds the local threshold of one. If `nu <= 1`, joint measurability rules out Bell violation for every state. Thus, within this class, incompatibility is exactly what can be amplified by sufficiently many GHZ parties.

The root limit identifies the exponential rate, not the exact optimum at a fixed party number. Our explicit construction is within a factor of two of the optimal normalized full-correlation value. That comparison concerns Bell values, not the excess above one or sampling cost. Ratios are not floored at one. The all-zero family gives zero; a nonzero collinear family gives exactly `R_N = R_N^GHZ = r^N` with `nu = r`.

## Why the bounds meet

**1. Geometry supplies one set of coefficients.** Yoshino et al.'s optimal planar dual certificate gives real vectors `h_x`. Encode them as complex numbers `c_x = h_x1 + i h_x2`. Their signed sums are bounded, and the edge formula in [the theorem, Section 3](research/THEOREM.md#3-inherited-geometric-input) gives

```math
\max_{s_x=\pm1}\left|\sum_xc_xs_x\right|\le1,
\qquad
T=\sum_xc_xA_x=\begin{pmatrix}0&\nu\\v&0\end{pmatrix},
\qquad |v|\le\nu.
```

The compatibility geometry and its certificate are inherited. The complex matrix is the link to the Bell construction.

**2. Tensor products turn those coefficients into a GHZ witness.** Choose real Bell coefficients

```math
\beta_{x_1\ldots x_N}
=\operatorname{Re}\left[e^{i\gamma}\prod_{j=1}^N c_{x_j}\right].
```

Every deterministic local value factors into the bounded one-site sign sums, so the local absolute bound is at most one. Aligning the Bell phase and GHZ phase gives the quantum value

```math
Q_N=\frac{\nu^N+|v|^N}{2}\ge\frac{\nu^N}{2}.
```

Dividing by the exact local bound can only improve this lower bound. The selected GHZ state maximizes this constructed Bell operator; it need not maximize an arbitrary fixed planar Bell expression. [Section 4](research/THEOREM.md#4-the-bell-construction) specifies both phases and checks all complementary-bitstring blocks.

**3. Joint parents bound every competing state.** In a mathematical comparison, rescale the first `N-1` sites by `1/nu` so each admits a joint parent, and the last site by `1/r` so its observables are valid. The parent outcomes and the last site's conditional quantum response form a local model. Restoring the scales multiplies every full correlator by `r nu^(N-1)`, proving the all-state upper bound. These rescaled measurements are proof devices, not extra resources supplied to the experiment. Taking Nth roots of the two bounds yields the common limit.

## What this adds to existing results

Yoshino et al., [*Joint measurability of coplanar POVMs*](https://arxiv.org/abs/2609.38836v1), supply the entire compatibility geometry, perimeter criterion, parent and optimal dual certificate. General qubit incompatibility activation, compatibility-based Bell bounds and complex GHZ correlation methods also have direct predecessors. Nagata, Laskowski and Paterek's [2006 multisetting construction](https://arxiv.org/abs/quant-ph/0601107v2) already contains the perimeter exponent for every regular setting polygon; Designolle et al. supply optimized symmetric constructions. The [source audit](literature/SOURCE_AUDIT.md) makes the fixed-detector phase comparison explicit.

The additional implication is the conversion of **every fixed planar family** in the declared class into explicit Bell coefficients and a phase-adjusted canonical GHZ state, together with a matching exponential bound over **all states**. General activation alone does not prescribe a full-correlation witness or its rate. The argument is a short connection between established ingredients. [Operational consequences](research/OPERATIONAL_CONSEQUENCES.md) give the finite logarithmic-rate estimate, fixed-margin party cost and precise noise interpretation; the [attribution record](literature/ATTRIBUTION.md) identifies the source passages.

## One finite-party illustration

For the retained irregular three-setting family in [Section 6](research/THEOREM.md#6-a-fixed-violation-margin-and-the-retained-exact-example), any full-correlation Bell/local ratio of at least two requires at least **20 parties**, while the existing **25-party GHZ witness** exceeds two. These are necessary and sufficient bounds, not an exact minimum. The example illustrates the theorem; the arbitrary-party result rests on its analytical proof.

## Scope and reading map

The state is supplied before the measurement choices. Every outcome is retained, with no communication during a trial, postselection, filtering, extra setting or sharper detector. State and inequality design use the known measurement family and plane.

The theorem does not cover biased or noncoplanar families, Bell expressions with marginal terms, exact finite-party optimality, genuine multipartite nonlocality, entanglement depth, self-testing, cryptographic rates, detector no-click robustness, efficient statistical certification or implemented GHZ preparation. Global white-state noise and independent detector noise are distinct. This is an author-side theoretical account; internal checks do not establish external independent review or exhaustive priority clearance.

| Read | Purpose |
|---|---|
| [Model and claims](research/MODEL_AND_CLAIMS.md) | Precise resources, normalization and nonclaims. |
| [Theorem and proof](research/THEOREM.md) | Complete construction, converse, degeneracies and party bounds. |
| [Operational consequences](research/OPERATIONAL_CONSEQUENCES.md) | Finite rate estimate, fixed-margin cost, noise conventions and certificate interpretation. |
| [Focused contribution review](research/CONTRIBUTION_REVIEW.md) | Proof scrutiny and the precise predecessor boundary. |
| [Source audit](literature/SOURCE_AUDIT.md) | Stronger regular-polygon predecessor and current primary-source comparison. |
| [Attribution](literature/ATTRIBUTION.md) | Inherited results and source-reading depth. |
| [Verification](VERIFICATION.md) | Original checks, preserved evidence and numerical comparison policy. |

The [consolidation assessment](research/ASSESSMENT.md) records the preceding assessment. The [archive](archive/README.md) retains all 81 historical snapshot members, including failed attempts and original reports. For repository maintenance, start with [WORKSPACE](WORKSPACE.md) and [CURRENT](work_orders/CURRENT.md). No third-party PDF is redistributed.

## Reproduce

Use Python 3.13.5 and the pinned scientific packages:

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python tools/verify.py --output .artifacts/local-01
```

The output directory must be new. The runner executes all **18 original scientific groups** and compares the four reports with their unchanged references. Eight infrastructure tests are counted separately. Exact byte equality is distinguished from permitted floating-point drift, and every changed field is recorded. Read [VERIFICATION](VERIFICATION.md) before changing checks or references.

## Purpose and contact

This repository serves as a record of the work and a guide for the author's self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

The repository retains the owner's [MIT license](LICENSE). Referenced third-party articles remain under their own licenses and are linked, not bundled.
