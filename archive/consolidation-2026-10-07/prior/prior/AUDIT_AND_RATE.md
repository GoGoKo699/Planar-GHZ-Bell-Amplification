# Planar measurements and GHZ states: proof audit and the exact amplification rate

**7 October 2026. Fresh Merlin–Arthur exploration after separation from Partial-Monitoring-Capacity.**

**Decision: retain the bounded planar result.** The preceding constructive implication survives the analytical audit. Adding a simple all-state converse shows that its GHZ construction has the optimal exponential full-correlation Bell amplification rate. This does not establish optimal finite-party experiments, statistical efficiency, general biased/noncoplanar measurements, or exhaustive priority. The closest September 2026 compatibility preprint remains available only at primary-indexed-abstract level.

No repository, protected project, prior monitoring code, or electronic-decoherence paper was accessed or used for the science. This is an author-side proof and literature assessment, not independent review. The predecessor scout and its complete evidence remain byte-preserved under `prior/`.

## 1. Fixed measurement resources and what is new this round

Every party receives one qubit and uses the same prescribed finite family

$$
M_{\pm|x}=(I\pm A_x)/2,\qquad
A_x=a_{x1}\sigma_x+a_{x2}\sigma_y,\qquad |\mathbf a_x|\le1.
$$

The observables are binary, unbiased, and coplanar through the Bloch origin. Their lengths and directions can be unequal and irregular. Zero, redundant, collinear, or repeated vectors are allowed. A common basis rotation identifies the measurement plane with the xy plane. There is no postselection, extra sharper setting, party-to-party communication during a trial, or replacement of the detector family as N grows.

The prior scout established an explicit compatibility-to-GHZ construction. Write

$$
K=\operatorname{conv}\{\pm\mathbf a_x\},\qquad
\nu=\operatorname{perimeter}(K)/4.
$$

A degenerate segment has twice its length as perimeter. Compatibility is equivalent to $\nu\le1$. The geometric criterion is not claimed as new: Yoshino et al. [Y26] announce it in their abstract, while the prior note derives the precise centrally symmetric convention independently. Loulidi–Nechita [LN22] supply the established compatibility-norm viewpoint.

The new statement is a **two-sided all-state comparison** for full-correlation Bell functionals. It both audits the construction and answers whether a different state could give a better exponential growth rate. It is not another selected large-N numerical example.

## 2. Mathematical audit of the compatibility certificate

### 2.1 Parent effects, not a physical universal spin flip

The compatibility norm is

$$
\nu(A)=\min\left\{\sum_s\|v_s\|_2:
\mathbf a_x=\sum_s s_xv_s\right\},
$$

with one representative of each opposite pair of sign strings. Starting with any joint parent, averaging opposite effects with their Bloch-inverted partners preserves positivity and unbiased marginals. This is a mathematical construction of effects; it does not assume a completely positive universal spin-flip channel. The resulting paired effects realize precisely the norm formulation. Projecting their Bloch vectors into the measurement plane does not increase their lengths.

The finite-dimensional dual is

$$
\nu(A)=\max_{\{h_x\}}\sum_xh_x\cdot a_x,
\qquad \max_{s_x=\pm1}\left|\sum_xs_xh_x\right|\le1.
$$

The code now checks this optimization independently of its geometric formula, using a constrained optimizer only as a diagnostic. The proof and rational Bell certificates do not depend on trusting an optimizer's global answer.

### 2.2 Why the full hull, including interior settings, is covered

Any sign decomposition puts K inside a zonotope with perimeter $4\sum_s\|v_s\|$. Monotonicity of planar convex perimeter proves the lower bound on the norm.

Conversely, write the centrally symmetric polygon as

$$
K=\sum_i[-g_i,g_i],\qquad \sum_i\|g_i\|=\nu,
$$

where the $g_i$ are half the edges along half its boundary. Every input vector, not only a hull vertex, is $a_x=\sum_i t_{xi}g_i$ with $|t_{xi}|\le1$. For $\nu>0$, the effects

$$
G_{i,\pm}=\frac{\|g_i\|I\pm g_i\cdot\sigma}{2\nu}
$$

form a joint parent for $A_x/\nu$, using response means $\pm t_{xi}$. Thus the uniformly divided family is a valid compatible measurement family even when the original family is already compatible and $\nu<1$. The zero family is handled separately.

An explicit optimal dual comes from the polygon's supporting directions or its edge tangents. The previous angular formula is feasible because $\int_0^{2\pi}|\cos\theta|\,d\theta=4$; its objective is one quarter of the perimeter. This checks the normalization and the implication without assuming that all settings have equal sharpness or are exposed hull vertices.

### 2.3 The phase choice is legitimate

Set $c_x=h_{x1}+ih_{x2}$ and $z_x=a_{x1}+ia_{x2}$. Then

$$
T=\sum_xc_xA_x=\begin{pmatrix}0&u\\v&0\end{pmatrix},
\qquad u=\sum_xc_x\bar z_x,\quad v=\sum_xc_xz_x.
$$

For an optimal dual, $\operatorname{Re}u=\nu$. A common rotation of all $h_x$ preserves feasibility, so a nonzero imaginary part would give an objective $|u|>\nu$ after rotation. Hence $u=\nu$ is real. Reflection and rotation of the certificate likewise show $|v|\le\nu$. No measurement axes are changed in this argument: these operations select the mathematical Bell coefficients.

For

$$
\beta_{x_1\cdots x_N}=\operatorname{Re}\left[e^{i\gamma}\prod_jc_{x_j}\right],
$$

every local deterministic strategy has absolute value at most one. The Bell operator is

$$
\widehat B_N=\tfrac12\left[e^{i\gamma}T^{\otimes N}
+e^{-i\gamma}(T^\dagger)^{\otimes N}\right].
$$

Choosing $\gamma=-N\arg(v)/2$ when $v\ne0$ aligns the two endpoint amplitudes. The GHZ relative phase can then make their expectation positive, giving

$$
Q_N=\frac{\nu^N+|v|^N}{2}\ge\frac{\nu^N}{2}.
$$

For $v=0$ the phase choice is arbitrary. This confirms the original sufficient condition $\nu^N>2$ for a violation. With a nonoptimal strict feasible certificate, the original real pairing $w>1$ still suffices through $w^N/2$; the numerical hull optimum is not a premise for the exact irregular example.

## 3. The new all-state upper bound

For any real coefficient tensor define its exact local absolute bound

$$
L(\beta)=\max_{s_x^{(j)}=\pm1}
\left|\sum_{\vec x}\beta_{\vec x}\prod_{j=1}^{N}s_{x_j}^{(j)}\right|.
$$

Define the largest normalized quantum value with the fixed family A at every site:

$$
\mathcal R_N(A)=\sup_{L(\beta)\le1}
\left\|\sum_{\vec x}\beta_{\vec x}\bigotimes_{j=1}^NA_{x_j}\right\|_\infty.
$$

The operator norm optimizes over all N-qubit states. Let $\mathcal R_N^{\mathrm{GHZ}}$ restrict the state to the ordinary xy-plane GHZ family with an adjustable relative phase. The inequality may depend on A and N in both definitions. Nonzero real coefficient tensors have nonzero L, because deterministic local sign tensors span the coefficient space.

**These are full-correlation functionals:** every term uses one outcome from every party. There are no lower-order marginal terms or constant offsets.

Because $A/\nu$ is jointly measurable, its outcomes on any shared state admit a local hidden-variable model. Homogeneity in the N local observables therefore gives

$$
\left\|\sum_{\vec x}\beta_{\vec x}\bigotimes_jA_{x_j}\right\|_\infty
=\nu^N\left\|\sum_{\vec x}\beta_{\vec x}\bigotimes_j(A_{x_j}/\nu)\right\|_\infty
\le\nu^NL(\beta).
$$

This is the standard parent-measurement/norm upper-bound method [LN22], applied to all N parties. Combining it with the audited constructive lower bound yields

$$
\boxed{\frac{\nu^N}{2}\le\mathcal R_N^{\mathrm{GHZ}}(A)
\le\mathcal R_N(A)\le\nu^N.}
\tag{1}
$$

The construction used a certified local bound of one, which may exceed the true local bound of that Bell functional. Normalizing by the true bound can only improve the displayed lower bound.

For every $\nu>0$, taking Nth roots proves the exact asymptotic rate:

$$
\boxed{\lim_{N\to\infty}(\mathcal R_N^{\mathrm{GHZ}})^{1/N}
=\lim_{N\to\infty}\mathcal R_N^{1/N}=\nu.}
\tag{2}
$$

Equivalently, the per-party logarithmic rate is $\ln\nu$. This is a squeezing-of-bounds proof, not an extrapolation of finite-N numerics. For $\nu=0$, all the full-correlation operators vanish.

**Interpretation.** The planar compatibility norm is exactly the exponential amplification factor of the best full-correlation Bell value. A familiar GHZ family attains that factor and is within a multiplicative factor two of the best possible normalized Bell value at every N. The comparison is not a factor-two approximation to the *excess above the local bound*: when the lower bound is below one it may not even certify a violation. Nor does it imply the exact finite-N optimum.

## 4. For its own constructed inequality, GHZ is exactly optimal

There is a stronger finite-N statement about the constructed Bell operator, distinct from optimizing the inequality itself.

Each computational basis string of Hamming weight k couples only to its bitwise complement. The magnitude of that two-by-two block is bounded by

$$
\frac12\left[\nu^{N-k}|v|^k+|v|^{N-k}\nu^k\right]
\le\frac12(\nu^N+|v|^N).
$$

To see the second step, set $r=|v|/\nu\in[0,1]$ and use

$$
1+r^N-r^k-r^{N-k}=(1-r^k)(1-r^{N-k})\ge0.
$$

The endpoint GHZ block attains the upper bound with the phases chosen above. Thus the chosen GHZ state is an exact largest-eigenvalue state of this constructed inequality. A search over a larger quantum state cannot improve that inequality's value, although another inequality may improve the finite-N value by up to the factor allowed in (1).

Equatorial full-correlation operators and GHZ eigenvectors are established tools, including the two-setting analysis of Werner–Wolf [WW01]. The new statement is not the first general observation that GHZ states are optimal for Bell inequalities.

## 5. A fixed violation margin makes the party-count scaling sharp in order

Let R>1 be a fixed target Bell/local ratio. Any state and full-correlation inequality attaining at least R with the prescribed measurements must satisfy

$$
N\ge\left\lceil\frac{\ln R}{\ln\nu}\right\rceil,
\qquad\nu>1.
$$

The explicit construction strictly exceeds R once

$$
N\ge\max\left\{2,\left\lfloor\frac{\ln(2R)}{\ln\nu}\right\rfloor+1\right\}.
$$

Accordingly the necessary and sufficient party counts both scale as $1/(\nu-1)$ near compatibility **for a fixed nonzero margin R-1**. This does not prove such a lower bound for merely obtaining an arbitrarily tiny positive violation.

For target R=2 the analytical counts are:

| $\nu-1$ | All-state necessary count | GHZ sufficient strict count |
|---|---:|---:|
| 0.1 | 8 | 15 |
| 0.01 | 70 | 140 |
| 0.001 | 694 | 1387 |

These are theorem-based counts, not an experimental scaling forecast or minimum-party optimization.

For the exact irregular triple preserved in the preceding scout, rational square-root enclosures give

$$
1.05775505175540324<\nu<1.05775505175540325.
$$

They certify $\nu^{12}<2$. Thus at least thirteen parties are necessary to reach **twice** the local bound within the full-correlation task. The old rational coefficients, now raised to the 25th power with the ordinary real GHZ state, give $2.035127554147\ldots>2$ against a certified local bound of one. Hence 25 parties suffice for the factor-two target.

The earlier thirteen-party value $1.037464516759\ldots$ is unchanged. The new lower bound is not a proof that its thirteen-party *first violation* is minimal.

## 6. Noise and scope controls

Uniformly shrinking all local Bloch vectors by t scales the same compatibility norm to $t\nu$. For the unchanged irregular coefficients,

| Extra local shrinkage | Parties | Bell value against certified bound 1 |
|---|---:|---:|
| none | 13 | 1.037464516759... |
| 1% | 13 | 0.910396924071... |
| 1% | 16 | 1.045420377334... |

The scalar calculations are rational and exact before decimal display. More parties can recover a violation in this example because the shrunken family remains incompatible. At 6% additional shrinkage, $0.94\nu<0.994290<1$: the family is compatible, so every state and every Bell experiment using only that family is local, not merely this constructed full-correlation test.

This is not a detector-efficiency theorem: no-click outcomes and biased reassignment have not been modeled. It is not a promise of experimental visibility once GHZ-state noise and finite samples are included. The preceding 2% global white-state-noise calculation remains a different model.

The full-correlation restriction in (1) cannot be dropped. With only the unsharp observable $A=0.5\sigma_x$ at three parties, $\nu^3=0.125$. A functional containing the one-party marginal $\langle A^{(1)}\rangle$ has local bound one and quantum maximum 0.5, which exceeds 0.125. It is degree one in the sharpness, not degree three. Constants would cause the same homogeneity problem. This does not refute any full-correlation statement above.

No result here establishes genuine N-party nonlocality, entanglement depth, self-testing, cryptographic utility, an optimal statistical exponent, or an efficient sampling protocol. The Bell value is dimensionless; its exponential growth does not identify the trial count needed to estimate it.

## 7. Construction-level prior-art audit

### General incompatibility-to-nonlocality existence: PGQ25

Plavala–Guhne–Quintino [PGQ25] prove the broader existence result for arbitrary incompatible qubit POVMs. Their main proof uses positive maps and leaves the state-family and party-count questions explicit in the Discussion. This pass checked the final author version as well as the previously used v3, including the statement that GHZ or Dicke states and an N bound are open directions. Our result does not replace their general theorem: it supplies a constructive answer for the unbiased binary planar class, with an additional full-correlation amplification law. Their trine examples and regular noise thresholds are not being claimed anew.

### Two settings and chosen observables: WW01

Werner–Wolf [WW01], Section V.D, proves that suitably chosen observables on GHZ states attain the extreme quantum correlations in the two-dichotomic-setting scenario. Its GHZ correlation algebra is directly relevant and inherited. Its resource statement is different from the one here: a prescribed family with arbitrarily many settings, unequal sharpness, and an incompatibility norm that determines the repeated-family rate. The paper's two-setting result is not being generalized in name only or described as absent. The universal conversion of an arbitrary planar incompatibility certificate is the implication to assess.

### Symmetric GHZ constructions: DVP24

Designolle–Vertesi–Pokutta [DVP24] use regular polygon directions and optimize symmetric multipartite Bell inequalities. Equations (6)–(8), Sections IX.A–B, and the concluding scope were inspected. Their optimized finite-N facets can improve constants beyond a simple construction. No claim is made to dominate their finite-party examples, discover regular-trine amplification, or produce the first complex-coefficient GHZ inequality. Their inspected construction does not give a rule for arbitrary irregular, unequal-sharpness planar measurements in terms of their compatibility geometry.

### Norms and multilinear methods: LN22, SCPA10, KSS22

Loulidi–Nechita [LN22], Sections 6–8 and especially Theorems 8.1–8.2, provide a compatibility norm and comparisons with bipartite Bell norms, with Alice's family fixed and Bob's measurements optimized. The parent-measurement upper-bound method is inherited. What is additionally derived here is the matching exponential lower bound with the same fixed family at every site.

Salles and collaborators [SCPA10] already organize Bell inequalities through multilinear contractions. Their Euclidean moment inequalities and their supremum-norm extension should not be conflated: the latter recovers standard correlation inequalities, whereas their no-bipartite-violation result concerns the former. Karczewski and collaborators [KSS22] similarly develop complex and multilinear constructions across settings and outcomes. These are precedents for the algebraic manufacturing of Bell inequalities, not evidence that our product-coefficient trick is a new general method. This pass inspected their framing and applicable construction sections, not every theorem or numerical example.

### The unresolved latest comparison: Y26

Yoshino and collaborators [Y26], submitted 30 September 2026, announce the coplanar perimeter compatibility criterion. Its primary indexed abstract is available. Direct abstract, HTML, PDF and source access attempts did not yield full text; runtime PDF/source requests failed DNS. Therefore **the full article may contain a relevant Bell consequence or a directly covering construction, and this pass cannot exclude that possibility**.

The mathematical argument above does not depend on that access: the parent and dual are explicitly derived and checked. The originality assessment does depend on closing this reading gap. A different title, an abstract omitting GHZ, or a failed search is not evidence that the desired implication is absent. This is the highest-priority remaining source comparison, not a reason to add another model or force a publication verdict now.

### Bounded assessment

No directly covering implication was identified in the inspected primary passages. The strongest supported candidate statement is the combination of constructive planar GHZ activation and exact optimal exponential full-correlation rate. The upper bound is elementary once the joint-parent norm is identified; the new rate is a consequence completing the initial theorem's interpretation, not a separate research project.

The main risk remains that the bridge is already an implicit or explicit standard corollary, especially in unread recent material. That question should be resolved before promoting the candidate to a repository or manuscript. There is no need to require biased POVMs, noncoplanar vectors, exact minimum N, or an apparatus proposal to assess this bounded result. Conversely, internal checks are not independent review or priority clearance.

## 8. Verification and repairs

The five final groups passed twice with byte-identical reports. They check independent hull/dual constructions and explicit joint parents, all-state operator bounds against parent statistics, full spectra of the constructed Bell operators, exact rational margin/noise certificates, and restriction/near-boundary controls. The largest new dense quantum matrix is 32 by 32. Higher-party examples use exact powers of two complex rational numbers, not a 25-qubit simulation.

The prior five groups were rerun unchanged and reproduced their canonical report byte for byte. All twelve prior archive members and its eleven manifest-listed hashes remain unchanged. The prior standalone note equals its archived copy.

The first new run failed one test because SLSQP reported a positive-directional-derivative termination while optimizing the dual under squared norm constraints, even near the known correct objective. Four other groups passed. The original source, failed report and diagnostic attempts are retained. The final formulation removes only exactly duplicate opposite-sign constraints and uses the equivalent unsquared norm inequalities with their analytical Jacobian. The optimizer's ftol (1e-12), iteration budget (500), success requirement, objective threshold (2e-8), and full original squared-feasibility threshold (-2e-8) are unchanged. No theorem, physical model or acceptance tolerance was relaxed. The final iterate is still checked against all original sign constraints.

The matrix/optimizer checks supplement analytical proofs. Numerical objectives are not certificates of exact optimality, and random operator tests do not prove the all-state theorem. The rational margin and noise comparisons are independently exact. Direct web screenshots of three mathematical PDF pages failed; source comparisons use readable primary mathematical text and do not claim inspection of unrendered figures or tables.

### Primary references

- **[PGQ25]** M. Plavala, O. Guhne, M. T. Quintino, *All Incompatible Measurements on Qubits Lead to Multiparticle Bell Nonlocality*, Physical Review Letters 134, 200201 (2025). [Author paper](https://arxiv.org/abs/2403.10564).
- **[Y26]** T. Yoshino, K. Tojo, K. Hagihara, A. Tanaka, T. Tomita, *Joint measurability of coplanar POVMs*, arXiv:2609.38836 (2026). [Primary abstract](https://arxiv.org/abs/2609.38836). Full text not accessed.
- **[LN22]** F. Loulidi, I. Nechita, *Measurement Incompatibility versus Bell Nonlocality: An Approach via Tensor Norms*, PRX Quantum 3, 040325 (2022). [Author paper](https://arxiv.org/abs/2205.12668).
- **[DVP24]** S. Designolle, T. Vertesi, S. Pokutta, *Symmetric multipartite Bell inequalities via Frank–Wolfe algorithms*, Physical Review A 109, 022205 (2024). [Author paper](https://arxiv.org/abs/2310.20677).
- **[WW01]** R. F. Werner, M. M. Wolf, *All multipartite Bell correlation inequalities for two dichotomic observables per site*, Physical Review A 64, 032112 (2001). [Author paper](https://arxiv.org/abs/quant-ph/0102024).
- **[SCPA10]** A. Salles, D. Cavalcanti, A. Acin, D. Perez-Garcia, M. M. Wolf, *Bell inequalities from multilinear contractions*, Quantum Information & Computation 10, 703–719 (2010). [Author paper](https://arxiv.org/abs/1002.1893).
- **[KSS22]** M. Karczewski, G. Scala, A. Mandarino, A. B. Sainz, M. Zukowski, *Avenues to generalising Bell inequalities*, Journal of Physics A: Mathematical and Theoretical 55, 384011 (2022). [Author paper](https://arxiv.org/abs/2202.06606).
