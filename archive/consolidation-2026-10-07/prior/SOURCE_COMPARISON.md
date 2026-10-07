# Uploaded-source comparison: planar compatibility and GHZ Bell amplification

**7 October 2026. Source-audit addendum to the existing planar-GHZ candidate.**

**Decision: retain and consolidate the bounded Bell result.** The full uploaded v1 of Yoshino–Tojo–Hagihara–Tanaka–Tomita confirms the compatibility norm, its exact perimeter value, and the primal/dual construction used in our notes. It does not state or derive a Bell inequality, a GHZ-state prescription, a number-of-parties bound, or the optimal full-correlation amplification exponent. The proposed Bell consequence remains distinct from the results actually developed in this article. This is not exhaustive priority clearance or independent scientific review.

No prior scientific formula is changed. The important update is attribution: the **explicit optimal dual certificate**, as well as the perimeter criterion, belongs among the inherited ingredients. The new note makes the dictionary exact rather than arguing from the absence of a Bell-related title or keyword. No repository, monitoring project, spin-strip project, or electronic-decoherence material was used or modified.

## 1. Exact source and reading depth

The inspected source is the user-supplied `2609.38836v1.pdf`, titled *Joint measurability of coplanar POVMs*, 17 pages, dated 30 September 2026. SHA-256:

`1181693ddd202f90eff59ebfc13f556e00bf472037e401ae9de2fd5f1c67eb88`

All 17 pages were read in extracted mathematical text and visually scanned in rendered pages. The edge-vector diagram on page 11 and the lens-region diagram on page 14 were inspected. The diagram on page 11 fixes the signs of the boundary differences; page 14 illustrates the nesting argument behind the alternating-unit-vector norm bound. Neither figure is a Bell experiment or a multipartite state construction. The source PDF and extracted full text are not redistributed in this checkpoint.

The paper is organized into an introduction/main theorem, a general compatibility optimization, and the two-dimensional construction. Section 3.6 finishes the dual norm proof on page 17; references follow immediately. The four references concern the Andrejic–Kunjwal compatibility conjectures, Busch's two-measurement condition, Grinko–Uola's general binary-qubit characterization, and convex analysis. The absence assessment below rests on this complete reading and the actual mathematical outputs, not on a keyword count alone.

The previous notes' statements that this article was unread describe those earlier passes. They are preserved as historical records and superseded here only as statements of current access.

## 2. What the article already proves

Use m for the number of settings, to avoid confusing it with our party number N. Every measurement is unbiased and binary:

$$
M_{\pm|x}=\frac{I\pm\mathbf a_x\cdot\boldsymbol\sigma}{2},
\qquad \mathbf a_x\in\mathbb R^2\subset\mathbb R^3,
\qquad\|\mathbf a_x\|\le1.
$$

The precise convex hull is centrally symmetric:

$$K=\operatorname{conv}\{\pm\mathbf a_x\}.$$

It is not the polygon obtained by joining every listed vector in its input order, nor the nonsymmetric hull of only the positive representatives.

| Our existing proof ingredient | Exact uploaded-source location | Assessment |
|---|---|---|
| Compatibility iff the sign-decomposition norm is at most one | Definition 2.4 and Lemma 2.6, pp. 4–6 | Inherited; their norm L is our nu, with no extra factor. |
| Averaging a parent to opposite, Bloch-inverted outcomes | Definition 2.7 and Lemma 2.8, pp. 4–5 | Inherited effect-level construction; not a physical universal spin-flip channel. |
| Removal of redundant/interior settings and output relabeling | Lemma 2.9, Corollary 2.10, pp. 6–7; Section 3.1, p. 11 | Inherited hull reduction. |
| Exact value nu = perimeter(K)/4 | Theorem 1.3, p. 2; Proposition 3.1, p. 10 | Explicit main result of the source. |
| An optimal primal and dual certificate | Lemma 2.21, p. 10; Definitions 3.3–3.7, pp. 11–12; Sections 3.3–3.6 | Already constructed, not just a nonconstructive existence theorem. |
| Equal-radius angular formula | Proposition 1.6, p. 3 | Resolves the stated Andrejic–Kunjwal common-circle conjecture; not a claim of ours. |
| Bell tensor, GHZ state, party bound, full-correlation exponent | Not a result in this v1 | These belong to the additional bridge in our current notes, subject to the wider prior-art boundary below. |

The source therefore overlaps **more than only the numerical criterion**. A claim that its theorem gives merely an existence test, while our contribution makes the compatibility witness explicit, would be false.

## 3. The exact dictionary for the dual certificate

After the source's reduction, let a_1,...,a_m be successive representatives along half the boundary, and set a_{m+1}=-a_1. Assume a genuinely two-dimensional polygon; zero/collinear inputs are treated separately as compatible single-axis families, not forced into this matrix parametrization.

The source defines

$$
 k_i=a_i-a_{i+1},\qquad\widehat k_i=k_i/\|k_i\|,
 \qquad K_{\rm edge}=(k_1,\ldots,k_m),
 \qquad \widehat K=(\widehat k_1,\ldots,\widehat k_m).
$$

Its sign matrix B contains the 2^(m-1) strings with first coordinate +1. Its P selects the rows indexed 2^(m-i), and its C has diagonal +1, subdiagonal -1, and an additional +1 in position (1,m). Definitions 3.3–3.7 give

$$
K_{\rm edge}=AC,\qquad
X=\tfrac12K_{\rm edge}P^T,\qquad
Y=\tfrac12\widehat K C^T.
$$

Their Lemma 3.9 supplies C P^T B=2I, hence XB=A. In our notation the columns of Y are exactly the geometric dual coefficients h_i:

$$
h_1=\tfrac12(\widehat k_1+\widehat k_m),\qquad
h_i=\tfrac12(\widehat k_i-\widehat k_{i-1})\quad(2\le i\le m).
$$

These are the same half-boundary edge-tangent expressions computed by the earlier checker, after undoing the source's signed permutation of settings. Interior settings receive zero coefficients; repeated settings admit equivalent ways of distributing their coefficient. This equality is also the derivative of the half-perimeter sum with respect to the vertices.

The source's dual constraints and complementary equality give

$$
\max_{s_i=\pm1}\left\|\sum_i s_i h_i\right\|\le1,
\qquad
\sum_i h_i\cdot a_i
=\frac12\sum_i\|k_i\|=\nu.
$$

Both conditions are inherited. The new dictionary checker implements the source matrices literally, checks the integer sign identities, and compares them with the previous independent monotone-chain construction. Agreement in those finite checks supplements this algebraic identity; it does not establish a new compatibility theorem.

## 4. What must still be added to obtain our Bell conclusion

Identify each planar vector with a complex number z_i and each h_i with c_i. The source certificate yields

$$
\left|\sum_i s_i c_i\right|\le1.
$$

The additional step is to form the N-party full-correlation functional

$$
\beta_{x_1\ldots x_N}=\operatorname{Re}\!\left[e^{i\gamma}
  c_{x_1}\cdots c_{x_N}\right].
$$

For every local deterministic assignment its value has absolute value at most one, since it factors into the product of the bounded one-site sign sums. This is ordinary complex multilinear Bell algebra; no new general inequality-manufacturing principle is claimed.

Now put T=sum_i c_i A_i, where A_i=a_{i1}sigma_x+a_{i2}sigma_y. In the chosen basis,

$$
T=\begin{pmatrix}0&u\\v&0\end{pmatrix},\qquad
u=u=\frac12\sum_i\|k_i\|,
\qquad v=\frac12\sum_i\frac{(k_{i1}+ik_{i2})^2}{\|k_i\|}.
$$

These equalities follow by substituting the source's Y and telescoping; |v|<=nu follows by the triangle inequality. They make the connection particularly transparent: no separate numerical optimization of the dual is needed.

The Bell operator is

$$
\widehat{\mathcal B}_N=\tfrac12\left[e^{i\gamma}T^{\otimes N}
 +e^{-i\gamma}(T^\dagger)^{\otimes N}\right].
$$

Choose gamma and the relative GHZ phase to align its two |0...0><1...1| contributions. Then

$$
\langle\mathrm{GHZ}_N|\widehat{\mathcal B}_N|\mathrm{GHZ}_N\rangle
=\tfrac12(\nu^N+|v|^N)\ge\nu^N/2.
$$

The other complementary-bitstring blocks cannot have greater norm, so this GHZ is an exact maximal eigenstate of its constructed functional. That does not establish the optimal functional at fixed N.

For the converse, the observables A_x/nu have a joint parent by the inherited norm theorem. Every state then produces local correlations for those scaled measurements. A full N-party correlator scales by nu^N, so, for every real Bell tensor beta,

$$
\left\|\sum_{\vec x}\beta_{\vec x}
 A_{x_1}\otimes\cdots\otimes A_{x_N}\right\|
\le\nu^N L(\beta),
$$

where L is the exact local absolute bound. This is the standard compatible-measurement bound, now applied to all N fixed sites. The final two-sided statement is

$$
\frac{\nu^N}{2}\le\mathcal R_N^{\rm GHZ}\le\mathcal R_N\le\nu^N,
\qquad
\lim_{N\to\infty}(\mathcal R_N^{\rm GHZ})^{1/N}
=\lim_{N\to\infty}\mathcal R_N^{1/N}=\nu.
$$

Here R_N optimizes the normalized full-correlation value over all states and all such Bell tensors, with the given measurement family fixed at every site. For an incompatible family nu>1, a sufficient party count for a violation is N>=2 with nu^N>2. For a fixed target ratio R>1, the already derived lower and upper party bounds scale as 1/(nu-1) near compatibility. No new version of those scientific statements is introduced by this source pass.

**The article supplies the geometric certificate. It does not perform this conversion to a full-correlation Bell tensor or establish the matching multipartite exponent.** The conversion is concise, so the strongest skeptical description is a new consequence of substantial established ingredients, not a new geometric theory. The intended contribution is the physical implication and the constructive exact asymptotic rate.

## 5. Wider predecessor comparison: what this upload does and does not settle

The upload resolves a concrete access problem. It does not make the wider priority question disappear.

- Plavala–Guhne–Quintino, arXiv:2403.10564v4 / PRL134,200201 (2025), Theorem 3, proves arbitrary incompatible qubit POVMs can yield multipartite Bell nonlocality. Its Discussion, pp. 4–5, explicitly asks whether known GHZ/Dicke families suffice and how many parties are required. The present result supplies a constructive answer for unbiased binary planar measurements, not for biased/noncoplanar families or arbitrary outcomes. The general existence conclusion is inherited.
- Loulidi–Nechita, arXiv:2205.12668 / PRX Quantum3,040325 (2022), Sections6–8, particularly Theorems8.1–8.2, compare a compatibility norm with bipartite Bell norms. The compatible-family upper-bound method is inherited. The inspected setting fixes Alice's family and optimizes Bob's observables; it does not state the repeated-family, N-party GHZ exponent above.
- Designolle–Vertesi–Pokutta, arXiv:2310.20677 / PRA109,022205 (2024), Eqs.(6)–(8), SectionsIX–X, specializes to regular planar polygons and optimized symmetric GHZ inequalities. Those results are direct predecessors for symmetric examples and may improve finite-N constants. Our result is not a claim to beat their optimized finite experiments.
- Grinko–Uola, *Compatibility of Binary Qubit Measurements*, PRL135,200201 (2025), is a reference of the uploaded article. This pass accessed the primary author PDF **v1 from July2024**, and the final journal abstract, not the final journal full text. Its read sections give a general compatibility characterization, steering consequences, and a convex-programming formulation. Steering is not interchangeable with the fixed-all-sites multipartite Bell experiment here. No full-text negative-priority claim about its final version is made.

The earlier Werner–Wolf and complex-multilinear comparisons remain in the preserved prior note. They were not newly rerun as whole-paper audits. The current searches and targeted primary reads found no covering conclusion at the declared scope. An absence of search hits is not used as proof of priority.

One should not state that the planar theorem solves PGQ's whole GHZ question, establishes genuine N-party nonlocality, or implies efficient statistical certification. The existence of full-correlation Bell violations and their normalized exponent are the proved targets. A factor-two comparison of Bell values is not a factor-two comparison of sample complexity, detector efficiency, or the excess above the local bound.

## 6. Contribution and next research allocation

**Retain the unified theorem for focused consolidation.** The uploaded article does not subsume the Bell conclusion. It makes its inherited input and the remaining new implication much more sharply identifiable.

Suggested core statement: *For any fixed finite family of unbiased binary coplanar qubit measurements, the joint-measurability norm is exactly the regularized full-correlation Bell-amplification factor, and phase-adjusted GHZ states attain it constructively within a universal factor two at finite N.*

The simple physical question is whether unknown, increasingly elaborate entangled states are needed to reveal arbitrarily weak incompatibility in this class. The construction shows that a familiar state family suffices, with the optimal exponential amplification rate and explicit party bounds. This is the case to assess, not the attractiveness of the polygon picture or the number of examples.

The main objection remains that the Bell connection may be considered a short consequence of known compatibility and GHZ methods. We should address that objection by the exact theorem-level comparison, not add a biased measurement, higher dimension, detector model, or extra numerical digits. No experimental implementation or every-setting marginal theorem is needed to assess the existing claim, and none is claimed.

`CONTRIBUTION_BRIEF.md` provides a compact standalone claim and proof route with the attribution built in. No journal acceptance, independent proof review, comprehensive priority certificate, repository creation, manuscript submission, or external contact has occurred.

## 7. Verification and preservation

Three new groups passed on the first completed execution and on repetition, with byte-identical JSON reports. They check:

1. The source's integer sign-matrix identities for two through eight half-hull vertices, including its alternating-sign condition.
2. The exact dictionary between its X/Y formulas and the previous geometric implementation on six measurement families, including interior and duplicate settings.
3. The complex Bell bridge built from those source columns, comparing the edge formulas for u,v and full spectra for two through five parties.

The largest new quantum matrix is 32 by32. The new checks attribute, reproduce, and verify normalization; they are not new experimental or many-body results.

The preceding five audit groups and five initial-scout groups were rerun unchanged. Both reports match their original references byte for byte. All 36 members of the immediate preceding archive remain unchanged, including its previously recorded failed optimizer run. The uploaded PDF remains unchanged.

One initial shell launch attempted to redirect a log before its output directory existed. Python did not start. Creating the missing output directory resolved that operational error without changing the checker. No scientific assertion failed in the completed new runs, and no tolerance, old formula, or stored report was changed.

## Source links

- Uploaded source: T. Yoshino et al., [arXiv:2609.38836v1](https://arxiv.org/abs/2609.38836v1).
- General qubit Bell theorem: [arXiv:2403.10564v4](https://arxiv.org/abs/2403.10564v4).
- Compatibility/Bell norms: [arXiv:2205.12668](https://arxiv.org/abs/2205.12668).
- Symmetric GHZ inequalities: [arXiv:2310.20677](https://arxiv.org/abs/2310.20677).
- General binary-qubit compatibility, version read: [arXiv:2407.07711v1](https://arxiv.org/abs/2407.07711v1); [final journal record](https://doi.org/10.1103/vv1h-5mf9).
