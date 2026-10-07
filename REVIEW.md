# From measurement incompatibility to GHZ Bell amplification

**One geometric quantity controls how fixed planar qubit detectors amplify full-correlation Bell values. A GHZ state reaches its optimal exponential scale.**

This bridge starts from the single tutorial anchor: Gühne, Haapasalo, Kraft, Pellonpää and Uola, [*Incompatible measurements in quantum information science*](https://arxiv.org/abs/2112.06784v3), Rev. Mod. Phys. **95**, 011003 (2023). The [reading guide](docs/README.md) identifies the relevant sections. Familiarity with qubit states, Pauli matrices and tensor products is assumed.

The review supplies the language of noisy measurements, joint parents, incompatibility quantification and Bell locality. It does not contain the later arbitrary-planar perimeter theorem or the GHZ construction below. We state the geometric input with its attribution, then explain the connection. The authoritative statement and complete proof remain in [THEOREM](research/THEOREM.md); the experiment and nonclaims remain in [MODEL_AND_CLAIMS](research/MODEL_AND_CLAIMS.md).

| Stage | Question |
|---|---|
| [Measurements](#1-noisy-measurements-as-bloch-vectors) | What is fixed about the detectors? |
| [Joint parents](#2-one-parent-measurement-and-bell-locality) | How does compatibility produce a local model? |
| [Bell objective](#3-the-full-correlation-objective-and-its-local-bound) | Which Bell value is being compared? |
| [Planar geometry](#4-the-inherited-planar-certificate) | Which geometric quantity and coefficients are inherited? |
| [Construction](#5-complex-coefficients-build-the-bell-expression) | How do the coefficients become a GHZ witness? |
| [GHZ value](#6-the-ghz-block-and-its-phase) | Why does the constructed quantum value grow? |
| [Converse](#7-joint-parents-bound-every-competing-state) | Why can no state beat the exponential rate? |
| [Rate](#8-the-common-exponential-factor) | What does the matching rate establish? |
| [Example](#9-a-worked-example-two-noisy-orthogonal-settings) | How does the dictionary work for familiar detectors? |

## 1. Noisy measurements as Bloch vectors

The review's Sections II.A–B and III.A describe binary qubit POVMs. In our unbiased case, the two effects are

```math
M_{s|x}=\frac{I+sA_x}{2},\qquad
A_x=\mathbf a_x\cdot\boldsymbol\sigma,\qquad
s\in\{-1,1\},\quad \|\mathbf a_x\|\le1.
```

The vector points along a measurement direction, and its length is the sharpness. A zero vector returns a fair random sign independently of the state. A unit vector gives a sharp spin measurement. The observable is the outcome-weighted sum of its effects: the expectation of the recorded sign is the expectation of the operator A_x.

All vectors in this project lie in a plane through the origin. Choose its normal as the computational z axis, so

```math
A_x=a_{x1}\sigma_x+a_{x2}\sigma_y
=\begin{pmatrix}0&\overline z_x\\z_x&0\end{pmatrix},
\qquad z_x=a_{x1}+i a_{x2}.
```

Every party uses this same finite family. Directions and sharpness are known and fixed as the number of parties grows; the state and the Bell coefficients can depend on them. A coordinate choice does not provide a new detector.

## 2. One parent measurement and Bell locality

Section II.B of the review defines compatibility by a parent POVM and classical postprocessing:

```math
M_{s|x}=\sum_\lambda p(s|x,\lambda)G_\lambda,
\qquad G_\lambda\ge0,\quad \sum_\lambda G_\lambda=I.
```

One can measure the parent first and subsequently simulate any requested setting by processing its outcome. This is a statement about all input states, rather than an accidental agreement of statistics on one state. Compatibility is broader than commutativity for noisy POVMs.

Section IV.A explains why a jointly measurable family on one side of a bipartite experiment cannot violate a Bell inequality: the parent outcome supplies a hidden variable, and the other party's conditional response supplies its local response function.

The multipartite version used here leaves one party arbitrary. If the first N−1 parties each have parents, their joint parent outcomes have a probability distribution and leave a conditional quantum state at the last party. Given those outcomes, the first parties respond through classical postprocessing and the last party responds through the Born rule. That is a local model. The all-but-one-sites statement is an inherited ingredient; [THEOREM, Section 5](research/THEOREM.md#5-the-all-state-upper-bound-with-one-site-left-arbitrary) identifies its source.

## 3. The full-correlation objective and its local bound

A full correlator multiplies one recorded sign from every party:

```math
E_{x_1\ldots x_N}
=\sum_{s_1,\ldots,s_N}\left(\prod_{j=1}^N s_j\right)
p(s_1,\ldots,s_N|x_1,\ldots,x_N).
```

For real coefficients beta, the Bell operator and exact local absolute bound are

```math
B_\beta=\sum_{x_1,\ldots,x_N}\beta_{x_1\ldots x_N}
A_{x_1}\otimes\cdots\otimes A_{x_N},
```

```math
L(\beta)=\max_{s_x^{(j)}=\pm1}
\left|\sum_{x_1,\ldots,x_N}\beta_{x_1\ldots x_N}
\prod_{j=1}^N s_{x_j}^{(j)}\right|.
```

Why deterministic signs? Shared randomness mixes local strategies, and each probabilistic response is itself a mixture of deterministic responses. The absolute value of a mixture cannot exceed the largest absolute value of its components. Thus the displayed maximum is the bound for every local model. A nonzero coefficient tensor has a positive local bound, because the deterministic sign tensors span the coefficient space.

The normalized quantum value is the absolute expectation divided by this exact bound. Optimizing over all states gives the Hermitian operator norm; optimizing also over nonzero tensors gives

```math
\mathcal R_N=\sup_{\beta\ne0}\frac{\|B_\beta\|}{L(\beta)}.
```

A ratio above one violates locality. A ratio below one is meaningful: the objective is not floored at one. There are no marginal terms or additive constants in this homogeneous full-correlation objective. An upper estimate for a particular tensor's local bound can prove a violation, but it must not be relabeled its exact local bound.

## 4. The inherited planar certificate

Take the symmetric hull of the fixed detector vectors and define

```math
K=\operatorname{conv}\{\pm\mathbf a_x\},\qquad
\nu=\frac{\operatorname{perimeter}(K)}4,\qquad
r=\max_x\|\mathbf a_x\|.
```

For a segment, perimeter is twice its length. For the all-zero family both quantities vanish. Yoshino et al., [*Joint measurability of coplanar POVMs*](https://arxiv.org/abs/2609.38836v1), provide the entire arbitrary-planar geometry: compatibility holds exactly when nu is at most one. For nu greater than zero, they also provide a parent after scaling the observables by 1/nu and an explicit optimal dual certificate. This later research paper supplies an inherited lemma; it is not a second tutorial anchor.

For a nondegenerate hull, its certificate gives real vectors h_x such that

```math
\max_{s_x=\pm1}\left\|\sum_x s_x h_x\right\|\le1,
\qquad \sum_x h_x\cdot\mathbf a_x=\nu.
```

The first condition limits every classical sign sum. The second pairs the certificate with the detectors and reaches the geometric value. This is the role of a dual certificate: a feasible bound that is attained. Sections III.B.1–2 of the tutorial explain the general optimization and noise-robustness language; the explicit polygon formula belongs to the later planar source. Redundant settings receive zero certificate coefficients, so they do not obstruct the construction. [THEOREM, Section 3](research/THEOREM.md#3-inherited-geometric-input) states the complete edge formula and source passages.

Encode each certificate vector as a complex number:

```math
c_x=h_{x1}+i h_{x2},\qquad
\max_{s_x=\pm1}\left|\sum_x c_xs_x\right|\le1.
```

The explicit planar certificate also gives

```math
T=\sum_x c_xA_x
=\begin{pmatrix}0&\nu\\v&0\end{pmatrix},
\qquad v=\sum_xc_xz_x,\quad |v|\le\nu.
```

Here the upper-right entry is the real number nu because the edge formula makes the imaginary part of the sum vanish. The real pairing alone would not establish that fact. This matrix dictionary is the link from the inherited geometry to the Bell argument.

## 5. Complex coefficients build the Bell expression

Choose real Bell coefficients by taking the real part of a product:

```math
\beta_{x_1\ldots x_N}
=\operatorname{Re}\left[e^{i\gamma}\prod_{j=1}^N c_{x_j}\right].
```

The complex numbers are a design tool; the Bell expression and its measured value remain real. Its value on any deterministic local strategy factorizes:

```math
\left|\operatorname{Re}\left[
e^{i\gamma}\prod_{j=1}^N\sum_x c_xs_x^{(j)}\right]\right|\le1.
```

Each factor has modulus at most one by the certificate. Consequently this tensor has a local bound at most one, although its exact local bound can be smaller.

The same product structure gives its operator:

```math
B_\beta=\frac12\left[
e^{i\gamma}T^{\otimes N}
+e^{-i\gamma}(T^\dagger)^{\otimes N}\right].
```

This is the connection we need: classical values are controlled by signed sums of the certificate, while the quantum value is controlled by powers of its matrix entries.

## 6. The GHZ block and its phase

The off-diagonal matrix T flips every computational bit. The Bell operator therefore splits into two-dimensional blocks, each joining a bit string to its complement. The all-zero/all-one block is

```math
\begin{pmatrix}0&b_N\\\overline b_N&0\end{pmatrix},
\qquad
b_N=\frac{e^{i\gamma}\nu^N+e^{-i\gamma}\overline v^{\,N}}2.
```

If v is nonzero, choose the Bell phase to align the two contributions and the GHZ phase to select the positive eigenvector:

```math
\gamma=-\frac{N\arg v}{2},\qquad
\varphi=-\arg b_N,\qquad
|\mathrm{GHZ}_{N,\varphi}\rangle
=\frac{|0\rangle^{\otimes N}+e^{i\varphi}|1\rangle^{\otimes N}}{\sqrt2}.
```

If v is zero, both phases can be zero. The resulting value is

```math
Q_N=\frac{\nu^N+|v|^N}{2}\ge\frac{\nu^N}{2}.
```

The selected GHZ state also maximizes this constructed operator. For a string with k ones, the corresponding off-diagonal magnitude is at most

```math
\frac{\nu^{N-k}|v|^k+\nu^k|v|^{N-k}}2
\le\frac{\nu^N+|v|^N}2.
```

To see the second inequality, set t equal to the ratio of the modulus of v to nu. Then t lies between zero and one, and the difference is proportional to the nonnegative product below:

```math
(1-t^k)(1-t^{N-k})\ge0.
```

Dividing Q_N by the exact local bound, which is positive and at most one, proves a normalized value at least nu to the Nth power divided by two. This GHZ maximality is about the tensor just constructed. For an arbitrary fixed planar tensor, a different complementary-bitstring block can maximize the operator; [THEOREM, Section 7](research/THEOREM.md#7-what-ghz-optimality-means-here) gives a counterexample to a broader claim.

## 7. Joint parents bound every competing state

The lower bound used a particular tensor and state. The converse must cover every tensor and every state. For a nonzero family, it does so with the locality argument from Section 2 and the inherited parent:

```math
\widetilde A_x^{(j)}=A_x/\nu\quad (j=1,\ldots,N-1),
\qquad \widetilde A_x^{(N)}=A_x/r.
```

The first N−1 families admit joint parents. At the last site the scaled observables are valid binary qubit observables because their norm is at most one. No parent is required there. These are mathematical comparison measurements in the proof; the actual experiment still uses its original detectors.

The comparison correlations are local for every input state, so every full-correlation Bell expectation is bounded by L(beta). Restoring the scales multiplies each full correlator by the same factor:

```math
|\langle B_\beta\rangle|
\le r\nu^{N-1}L(\beta),\qquad
\mathcal R_N\le r\nu^{N-1}\le\nu^N.
```

This homogeneity is why the theorem fixes the full-correlation task. Marginal terms would acquire different scale factors and require a separate argument.

## 8. The common exponential factor

Let the GHZ-restricted optimum allow the phase-adjusted canonical state above and arbitrary real full-correlation tensors. For every nonzero family and every N at least two,

```math
\frac{\nu^N}{2}
\le\mathcal R_N^{\mathrm{GHZ}}
\le\mathcal R_N
\le r\nu^{N-1}\le\nu^N.
```

Taking Nth roots squeezes both optima to the same limit:

```math
\lim_{N\to\infty}(\mathcal R_N^{\mathrm{GHZ}})^{1/N}
=\lim_{N\to\infty}\mathcal R_N^{1/N}=\nu.
```

If nu exceeds one, the explicit lower bound eventually exceeds the local threshold. If nu is at most one, compatibility supplies a local model for every state. Thus every incompatible family in the declared class can be exposed by enough GHZ parties, and the compatibility norm is its optimal exponential Bell-amplification factor.

The geometric constant is not the exact optimum at a given party number. The construction is within a factor of two of the optimal normalized Bell value; this comparison does not concern the excess above one or the number of experimental samples. A nonzero collinear family instead has nu equal to r and both optima exactly equal to r to the Nth power. The all-zero family gives zero.

## 9. A worked example: two noisy orthogonal settings

Use the same two detectors at every site, with sharpness eta:

```math
A_1=\eta\sigma_x,\qquad A_2=\eta\sigma_y,
\qquad 0<\eta\le1.
```

Their symmetric hull is a square with side length equal to the square root of two times eta. The tutorial's two-observable criterion and the planar perimeter criterion agree:

```math
r=\eta,\qquad \nu=\sqrt2\eta,
\qquad \text{compatibility}\ \Longleftrightarrow\ \eta\le1/\sqrt2.
```

The certificate and its matrix dictionary are particularly simple:

```math
h_1=(1/\sqrt2,0),\qquad h_2=(0,1/\sqrt2),
\qquad c_1=1/\sqrt2,\quad c_2=i/\sqrt2,
```

```math
\left|\frac{s_1+i s_2}{\sqrt2}\right|=1,
\qquad
T=\frac{\eta}{\sqrt2}(\sigma_x+i\sigma_y)
=\begin{pmatrix}0&\sqrt2\eta\\0&0\end{pmatrix}.
```

Thus v is zero, and the construction yields the unnormalized quantum value

```math
Q_N=(\sqrt2\eta)^N/2.
```

At three parties and zero phase, the resulting tensor is a scaled familiar Mermin expression:

```math
\mathcal M_3=E_{111}-E_{122}-E_{212}-E_{221},
\qquad \beta\cdot E=\frac{\mathcal M_3}{2\sqrt2}.
```

Its exact local absolute bound is two. For deterministic outcomes, either the first-party-1 bracket or the first-party-2 bracket below vanishes, and the other has magnitude two:

```math
\mathcal M_3
=s_1^{(1)}\big(s_1^{(2)}s_1^{(3)}-s_2^{(2)}s_2^{(3)}\big)
-s_2^{(1)}\big(s_1^{(2)}s_2^{(3)}+s_2^{(2)}s_1^{(3)}\big).
```

On the zero-phase GHZ state, the four correlators give a Mermin value of four times eta cubed. The normalized witness value is therefore

```math
\frac{|\langle\mathcal M_3\rangle|}{L(\mathcal M_3)}=2\eta^3.
```

For example, eta equal to 0.8 gives 1.024. The scaled tensor's exact local bound is the reciprocal square root of two, illustrating why the general estimate of at most one need not be tight. A compatible family cannot violate; an incompatible family need not violate at this particular party number. The theorem supplies eventual violation as N grows. This is a familiar special case used to learn the dictionary, not a new symmetric-setting result.

## 10. What the bridge does and does not add

The single tutorial anchor teaches the conceptual background. Yoshino et al. supply the later planar criterion, parent and dual certificate. Compatibility-based Bell bounds, qubit activation, complex correlation constructions and regular-polygon GHZ amplification all have predecessors. The [attribution record](literature/ATTRIBUTION.md) and [source audit](literature/SOURCE_AUDIT.md) keep these inputs distinct from the additional implication for arbitrary fixed planar families.

The experiment uses one qubit per party, supplied entanglement, a known detector family and all recorded outcomes. It involves no communication during a trial, filtering, postselection, extra setting or sharper detector. The proof does not establish results for biased or noncoplanar families, marginal-containing expressions, exact finite-party optimality, genuine multipartite nonlocality, entanglement depth, self-testing, cryptographic rates, detector no-click robustness, efficient statistical certification or implemented GHZ preparation.

Global white-state noise and independent detector noise are different operations. The [operational consequences](research/OPERATIONAL_CONSEQUENCES.md) explain their distinct effects, finite logarithmic-rate estimates and fixed-margin party bounds. These consequences support the same claim. Finite checks and examples illustrate the proof; the arbitrary-party statement rests on the analytical argument.

Continue with [THEOREM](research/THEOREM.md) for the formal proof, or use the [reading guide](docs/README.md) to move between the tutorial and this bridge.
