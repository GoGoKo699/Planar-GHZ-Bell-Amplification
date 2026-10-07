# Optimal exponential Bell amplification from planar qubit measurements

This is one bounded contribution: converting the inherited planar joint-measurability certificate into an explicit GHZ Bell experiment whose normalized full-correlation value has the optimal exponential scale. The geometric norm, its perimeter formula, and its optimal certificates are due to Yoshino and collaborators [Y26]. General qubit incompatibility activation is already established [PGQ25]. No new compatibility theorem, experimental performance, or exhaustive priority certificate is claimed.

The finite-party upper bound in (2) uses the standard fact that compatibility at all but one site suffices for locality.

## 1. Physical question and fixed resources

Let every party use the same finite family of unbiased binary qubit POVMs

```math
M_{s|x}=\frac{I+sA_x}{2},\qquad
A_x=a_{x1}\sigma_x+a_{x2}\sigma_y,
\qquad s\in\{-1,1\},\quad \|\mathbf a_x\|\le1.
```

Any measurement plane through the Bloch-sphere origin can be brought to this form by a common choice of basis. Directions and sharpness can be irregular and unequal. Repeated settings, zero settings and settings inside the symmetric hull are allowed. The family is fixed while the number of parties grows.

The resources are one qubit per party, an entangled state supplied before the choices, and these local measurements only. No communication during the trial, postselection, privileged sharper detector, filtering, or multiple sequential uses at a site is added. State and Bell-functional design use the known family and its plane; the result is not an uncalibrated device-construction procedure.

For a real full-correlation coefficient tensor $`\beta`$, define

```math
L(\beta)=\max_{s_x^{(j)}=\pm1}
\left|\sum_{x_1,\ldots,x_N}\beta_{x_1\ldots x_N}
\prod_{j=1}^N s_{x_j}^{(j)}\right|,
```

```math
B_\beta=\sum_{x_1,\ldots,x_N}\beta_{x_1\ldots x_N}
 A_{x_1}\otimes\cdots\otimes A_{x_N},
\qquad
\mathcal R_N=\sup_{\beta\ne0}\frac{\|B_\beta\|}{L(\beta)}.
```

Every summand contains one measured outcome at every site. There are no lower-order marginal terms or arbitrary additive constants. The sign strategies span the coefficient space, so $`L(\beta)>0`$ for $`\beta`$ nonzero. $`\mathcal R_N`$ is not artificially floored at one: it may be below one for noisy compatible measurements.

Let $`\mathcal R_N^{\mathrm{GHZ}}`$ restrict the state to

```math
|\mathrm{GHZ}_{N,\varphi}\rangle
=\frac{|0\rangle^{\otimes N}+e^{i\varphi}|1\rangle^{\otimes N}}{\sqrt2}
```

in this common plane-normal basis, while still optimizing $`\beta`$ and $`\varphi`$. It does not include arbitrary local filters or independent changes of the given measurement family.

Set

```math
K=\mathrm{conv}\{\pm\mathbf a_x\},\qquad
\nu=\frac{\mathrm{perimeter}(K)}4,\qquad
r=\max_x\|\mathbf a_x\|.
\tag{1}
```

The perimeter of a segment is twice its length; all-zero measurements give $`\nu=r=0`$. The inherited geometry implies $`r\le\nu\le\pi r/2`$ and compatibility iff $`\nu\le1`$. The operators $`A_x/\nu`$ have a parent whenever $`\nu>0`$. These rescaled operators are a mathematical comparison in the proof, not extra settings supplied in the experiment.

## 2. The theorem

For every $`N\ge2`$ and nonzero family,

```math
\boxed{\frac{\nu^N}{2}
\le \mathcal R_N^{\rm GHZ}
\le \mathcal R_N
\le r\nu^{N-1}
\le\nu^N.}
\tag{2}
```

There is an explicit $`\beta`$ and phase-adjusted GHZ state giving the lower bound; the state in fact maximizes that constructed Bell operator. Therefore

```math
\boxed{
\lim_{N\to\infty}(\mathcal R_N^{\rm GHZ})^{1/N}
=\lim_{N\to\infty}\mathcal R_N^{1/N}=\nu.}
\tag{3}
```

For the zero family both sequences vanish. For a nonzero collinear family one has $`\nu=r`$ and exactly $`\mathcal R_N=\mathcal R_N^{\mathrm{GHZ}}=r^N`$, so no incompatible case is lost in the nondegenerate construction below.

Consequently, incompatibility in this class is equivalent to Bell violation on a sufficiently large member of the stated GHZ family. The necessity follows from compatibility on all sites for every state, not just full-correlator tests. This is a constructive planar-subclass refinement of the established general qubit existence result [PGQ25].

The sharpened upper bound improves finite-party constants, not the exponent. Relative to our explicit constructed ratio, no competing state and full-correlation functional can be larger by more than $`2r/\nu\le2`$. This is a comparison of normalized Bell values, not their excess above one, not sample complexity, and not a statement of exact finite-$`N`$ optimum.

## 3. Inherited geometric input

After removing redundant settings and making a signed reordering, let $`\mathbf a_1,\ldots,\mathbf a_m`$ follow half of the symmetric polygon boundary, with $`\mathbf a_{m+1}=-\mathbf a_1`$. Define

```math
k_i=\mathbf a_i-\mathbf a_{i+1},\qquad
\widehat k_i=k_i/\|k_i\|,
```

```math
h_1=\tfrac12(\widehat k_1+\widehat k_m),\qquad
h_i=\tfrac12(\widehat k_i-\widehat k_{i-1}),\quad i\ge2.
```

These are the columns of the source's matrix $`Y=\tfrac12\widehat K C^T`$ [Y26, Lemma 2.21 and Definitions 3.3–3.7]. Undo the signs and reordering; unused interior settings receive zero coefficients. The source proves

```math
\max_{s_x=\pm1}\left\|\sum_xs_xh_x\right\|\le1,
\qquad
\sum_xh_x\cdot\mathbf a_x=\nu.
\tag{4}
```

Write $`z_x=a_{x1}+i a_{x2}`$, $`c_x=h_{x1}+i h_{x2}`$, and identify $`k_i`$ with its complex coordinate. Substitution and telescoping give

```math
u=\sum_xc_x\bar z_x=\frac12\sum_i\|k_i\|=\nu,
\qquad
v=\sum_xc_xz_x=\frac12\sum_i\frac{k_i^2}{\|k_i\|},
\qquad |v|\le\nu.
\tag{5}
```

Equation (4), including its explicit construction, is inherited. Equation (5) is the elementary dictionary used in the additional Bell argument. The geometry need not be rederived as an allegedly new result.

For a collinear family choose the longest setting $`\mathbf a_j=r\mathbf d`$ and take $`h_j=\mathbf d`$, with other $`h`$ zero. Then $`u=r`$ and $`|v|=r`$; suitable phases recover $`r^N`$ directly.

## 4. The Bell construction

Choose

```math
\beta_{x_1\ldots x_N}
=\mathrm{Re}\left[e^{i\gamma}\prod_{j=1}^Nc_{x_j}\right].
\tag{6}
```

For any local deterministic strategy its value factors:

```math
\left|\mathrm{Re}\left[e^{i\gamma}
\prod_{j=1}^N\sum_x c_xs_x^{(j)}\right]\right|\le1.
```

Thus $`L(\beta)\le1`$. This is a valid upper bound on the local absolute value, not a claim that one is always its exact value. The normalized quantum/local ratio can only improve when the true bound is smaller.

Put

```math
T=\sum_x c_xA_x=\begin{pmatrix}0&\nu\\v&0\end{pmatrix}.
```

Then

```math
B_\beta=\tfrac12\left[e^{i\gamma}T^{\otimes N}
+e^{-i\gamma}(T^\dagger)^{\otimes N}\right].
```

When $`v`$ is nonzero choose $`\gamma=-N\arg(v)/2`$. The upper-right element on the all-zero/all-one subspace is

```math
b_N=e^{-iN\arg(v)/2}\frac{\nu^N+|v|^N}{2}.
```

Choose $`\varphi=-\arg(b_N)`$. The GHZ expectation is $`|b_N|`$. If $`v=0`$, take $`\gamma=\varphi=0`$.

Every other computational-basis block joins a string of Hamming weight $`k`$ to its complement. Its off-diagonal magnitude is bounded by

```math
\frac{\nu^{N-k}|v|^k+\nu^k|v|^{N-k}}2
\le\frac{\nu^N+|v|^N}2,
```

because for $`t=|v|/\nu`$ in $`[0,1]`$, $`(1-t^k)(1-t^{N-k})\ge0`$. Hence the selected GHZ state exactly maximizes this particular operator. This proves the lower bound in (2).

## 5. The all-state upper bound, with one site left arbitrary

Scale the first $`N-1`$ sites to $`A_x/\nu`$; each has the inherited parent measurement. At the last site use $`A_x/r`$, which is a valid binary qubit observable even when its family is incompatible.

Measure the first $`N-1`$ parents mathematically. Their joint outcome $`\lambda`$ has a classical probability and leaves a conditional state at the last site. Conditioned on $`\lambda`$, each earlier site's setting is generated by classical postprocessing; the last site's response is its Born probability on the conditional state. This is a local hidden-variable model. The standard $`N-1`$-compatible-sites locality statement is explicit in [PGQ25, p. 2].

Restoring the factors multiplies every full correlator by $`r\nu^{N-1}`$. For every input state,

```math
|\langle B_\beta\rangle|\le r\nu^{N-1}L(\beta).
```

Taking the state and $`\beta`$ suprema proves the sharpened bound. Scaling all $`N`$ sites instead yields the original $`\nu^N`$ bound. Neither argument supplies the rescaled measurements to the actual experiment.

The nonnegative-root squeeze proves (3). No finite-state numerical search is needed for the arbitrary-$`N`$ statement.

## 6. A fixed violation margin and an exact example

For $`\nu>1`$ and a desired ratio $`R>1`$, any full-correlation experiment reaching at least $`R`$ must have

```math
N\ge\left\lceil1+\frac{\ln(R/r)}{\ln\nu}\right\rceil.
\tag{7}
```

The construction is sufficient to exceed $`R`$ whenever $`\nu^N>2R`$. Thus the required party number has inverse-$`(\nu-1)`$ order for a fixed $`R`$ near incompatibility. The constants depend on the target and, in the lower bound, on $`r`$. No exact minimum for an infinitesimal violation is asserted.

Consider the irregular rational family

```math
\mathbf a_1=(.70,0),\qquad
\mathbf a_2=(-.42,.56),\qquad
\mathbf a_3=(-.28,-.66).
```

Here $`\nu`$ is about 1.05775505 and $`r`$ about .71693793. The 13-party and 25-party values have exact certificates. The upper bound certifies

```math
r\nu^5<1,\qquad r\nu^{18}<2,
```

so at least seven parties are necessary for any full-correlation violation and at least twenty for a ratio of two. The existing construction gives a violation at thirteen and a ratio exceeding two at twenty-five. In particular,

```math
20\le N_{R\ge2}^{\rm full\ correlation}\le25.
```

These are necessary/sufficient bounds, not identification of the optimal $`N`$. Rational upper enclosures of the square roots prove the two exclusions; no rounding of logarithms is a correctness premise. The prior exact coefficient vector certifies the sufficient values. These numbers illustrate the sharpened converse, not a second physical result.

## 7. What GHZ optimality means here

For any fixed $`\beta`$, planar full-correlation operators are anti-diagonal in this basis. They always split into two-dimensional blocks, with GHZ-type maximizing eigenstates of the form $`\frac{|b\rangle+e^{i\varphi}|\bar b\rangle}{\sqrt2}`$. This is elementary planar spin algebra related to standard GHZ constructions [WW01]; it does not by itself establish that a Bell violation exists, construct $`\beta`$ for an arbitrary incompatible family, or determine its asymptotic rate.

It is false that the canonical all-zero/all-one GHZ must maximize every fixed planar Bell operator. For $`A_1=X,\ A_2=Y`$,

```math
B=X\otimes X+X\otimes Y-Y\otimes X+Y\otimes Y
```

has local bound two and operator norm $`2\sqrt2`$, but vanishes on the canonical GHZ subspace. Its maximizing Bell state lies in $`\mathrm{span}\{|01\rangle,|10\rangle\}`$. This scope control does not alter our constructed $`\beta`$, whose maximum is in the canonical GHZ block.

For the constructed GHZ state, every proper nonempty marginal correlator of these equatorial observables vanishes. Thus its complete measurement behavior is

```math
p(s_1,\ldots,s_N|x_1,\ldots,x_N)
=2^{-N}\left[1+\left(\prod_js_j\right)E_{x_1\ldots x_N}\right].
```

There is no conditioning on a special subset of outcomes. A local model for its full tensor can be converted into a local model for this behavior by shared random output signs with product $`+1`$, which erase proper marginals while preserving the full product. This explains the full-correlation task for the constructed state; it does not extend the all-state homogeneous upper bound to arbitrary marginal-containing Bell expressions.

## 8. Attribution and scope

[Y26] supplies the entire geometric compatibility problem and both optimal certificates. [PGQ25] supplies general eventual qubit activation and identifies the state-family/party-count questions. [LN22] supplies compatibility-norm upper-bound methods. [WW01] supplies important GHZ optimality precedents in the two-setting scenario. [DVP24] supplies optimized regular-polygon GHZ Bell constructions. None of these ingredients is assigned new priority here.

The proposed additional implication is: for every fixed irregular planar family in the declared class, an explicit $`\beta`$ and phase-adjusted GHZ attain the compatibility norm's exponential scale, with a matching all-state bound. The inspected source passages do not directly supply that complete statement.

Biased or noncoplanar measurements, detector no-click models, exact finite-$`N`$ Bell optima, genuine multipartite nonlocality, self-testing, cryptographic rates and efficient statistical certification are not claimed and are not automatic prerequisites.

## Primary references

- [Y26] T. Yoshino, K. Tojo, K. Hagihara, A. Tanaka, T. Tomita, *Joint measurability of coplanar POVMs*, [arXiv:2609.38836v1](https://arxiv.org/abs/2609.38836v1), user-supplied PDF. Theorem 1.3, Proposition 3.1, Lemma 2.21, Definitions 3.3–3.7. Full-text source assessment is preserved in [the archived source comparison](../archive/consolidation-2026-10-07/prior/SOURCE_COMPARISON.md).
- [PGQ25] M. Plavala, O. Guhne, M. T. Quintino, *All incompatible measurements on qubits lead to multiparticle Bell nonlocality*, PRL 134,200201 (2025), [author v4](https://arxiv.org/abs/2403.10564v4). Theorem 3; p. 2 all-but-one compatibility; pp. 4–5 Corollary 6 and Discussion; Appendix B proof route.
- [LN22] F. Loulidi, I. Nechita, *Measurement Incompatibility versus Bell Nonlocality: An Approach via Tensor Norms*, PRX Quantum 3,040325 (2022), [author paper](https://arxiv.org/abs/2205.12668). Theorems 8.1–8.2 concern the bipartite fixed-Alice setting, not a stated repeated-family multipartite exponent.
- [WW01] R. F. Werner, M. M. Wolf, *All-multipartite Bell-correlation inequalities for two dichotomic observables per site*, PRA 64,032112 (2001), [author paper](https://arxiv.org/abs/quant-ph/0102024). Section V.D and the explicit two-setting restriction in Section VII.
- [DVP24] S. Designolle, T. Vertesi, S. Pokutta, *Symmetric multipartite Bell inequalities via Frank-Wolfe algorithms*, PRA 109,022205 (2024), [author paper](https://arxiv.org/abs/2310.20677). Equations (6)–(8) specify regular polygon settings. No superiority to its finite-party optimized inequalities is claimed.

The preserved [scientific source](../research/THEOREM.md) defines this theorem.
