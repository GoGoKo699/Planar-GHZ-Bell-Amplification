# A constructive GHZ witness for incompatible planar qubit measurements

**7 October 2026. First fresh scout after the Partial-Monitoring-Capacity separation.**

**Decision: retain for one bounded construction-level novelty and proof assessment.** This note gives an author-side constructive implication for every finite family of **unbiased binary qubit measurements in a plane through the Bloch-sphere origin**. It is not a new proof that arbitrary incompatible qubit measurements can become Bell nonlocal; that existence result is established [PGQ25]. The proposed advance is specifying the GHZ state, Bell coefficients, and a sufficient finite party count for the planar subclass, including irregular directions and unequal sharpness.

The compatibility geometry, ordinary GHZ correlation algebra, and convex-duality tools are inherited. A very recent primary abstract [Y26] announces the planar perimeter criterion. Its full text was not accessible here, so exact overlap with its implications remains unresolved. No repository, old scientific code, or protected project was accessed or modified. No new platform or manuscript is selected.

## 1. Physical task and exact scope

Each party receives one qubit and chooses one of the same prescribed measurements,

\[
 M_{\pm|x}=\frac{I\pm A_x}{2},\qquad
 A_x=a_{x1}\sigma_x+a_{x2}\sigma_y,\qquad |\mathbf a_x|\le1,
 \quad x=1,\ldots,m.
\]

The settings can have different directions and different sharpness. A common rotation brings any plane through the origin to the stated xy plane. There are exactly two recorded outcomes, +1 and -1, with no selection of successful trials. Biased effects with an identity component in A_x, noncoplanar families, and missing-outcome detection models are not included by default.

Compatibility means that every setting can be obtained by classical postprocessing of a single parent measurement. If all parties' local sets are compatible, their joint statistics on any shared state have a local hidden-variable model: measure the parent at each site, use the resulting joint classical distribution as the hidden variable, and apply the prescribed local postprocessings.

The question is the converse under a deliberately simple state restriction: **when compatibility fails in this planar class, does a GHZ state suffice?** The state and Bell inequality may depend on the given family. This is not one fixed finite-N experiment detecting every arbitrarily small incompatibility.

The general 2025 existence theorem [PGQ25] allows arbitrary finite qubit POVMs and leaves constructive state-family/party-count questions. Its explicit trine examples do not establish the full planar construction below. Symmetric GHZ inequalities and norm descriptions of compatibility already exist [DVP24,LN22]; no first-ever use of those ingredients is claimed.

## 2. The compatibility norm and its dual

Choose one representative from each pair of opposite sign strings \(s\in\{\pm1\}^m\). Define

\[
 \nu(A)=\min\left\{\sum_s\|\mathbf v_s\|_2:
 \mathbf a_x=\sum_s s_x\mathbf v_s\ \text{for all }x\right\}.
 \tag{1}
\]

Then the measurements are compatible exactly when \(\nu(A)\le1\).

To verify the normalization, start with any joint parent whose outcomes are full sign strings. Average each effect with the Bloch-inverted effect for the opposite string. Qubit Bloch inversion, \((wI+\mathbf v\cdot\boldsymbol\sigma)/2\mapsto(wI-\mathbf v\cdot\boldsymbol\sigma)/2\), preserves positivity. This is a construction of valid effects, not a physical implementation of a universal spin-flip channel. Unbiased marginals are unchanged by this averaging. The resulting opposite parent effects have the form

\[
 G_{s}=\frac{\mu_s I+\mathbf v_s\cdot\boldsymbol\sigma}{2},\quad
 G_{-s}=\frac{\mu_s I-\mathbf v_s\cdot\boldsymbol\sigma}{2},\quad
 \sum_s\mu_s=1,\quad \|\mathbf v_s\|\le\mu_s.
\]

Their signed marginals give (1). Projection of parent Bloch vectors onto the measurement plane does not increase their norms. Conversely, any decomposition with total norm at most one supplies this parent by allocating the remaining scalar weight among its effects. This is a specialized finite-dimensional compatibility-norm representation, consistent with the established framework [LN22].

Its ordinary finite-dimensional convex dual is

\[
 \nu(A)=\max_{\mathbf h_x\in\mathbb R^2}
 \left\{\sum_x\mathbf h_x\cdot\mathbf a_x:
 \max_{s\in\{\pm1\}^m}\left\|\sum_xs_x\mathbf h_x\right\|_2\le1\right\}.
 \tag{2}
\]

In particular, an incompatible family admits a finite certificate with pairing greater than one. A strict feasible certificate, rather than a numerically assumed optimum, is sufficient for the Bell construction.

## 3. In the plane the certificate is explicit geometry

Let

\[
 K=\operatorname{conv}\{\pm\mathbf a_1,\ldots,\pm\mathbf a_m\},\qquad
 P=\operatorname{perimeter}(K).
\]

Use the continuous perimeter convention for a degenerate segment: twice its length. Then

\[
 \boxed{\nu(A)=P/4.}\tag{3}
\]

This compatibility criterion is announced in the recent primary abstract [Y26]. The following elementary argument is included to state the exact centrally symmetric convention and to make this scout independent of inaccessible proof details; the criterion is not claimed as our discovery.

A sign-decomposition in (1) embeds K into the zonotope \(\sum_s[-\mathbf v_s,\mathbf v_s]\). Its perimeter is \(4\sum_s\|\mathbf v_s\|\). Monotonicity of planar convex perimeter gives \(P/4\le\nu\).

Conversely, every centrally symmetric planar polygon is the sum of segments \([-\mathbf g_i,\mathbf g_i]\), where \(\mathbf g_i\) are half the edge vectors along one half of its boundary. Their lengths sum to P/4. Each point \(\mathbf a_x\in K\) can be written \(\sum_i t_{xi}\mathbf g_i\), with \(|t_{xi}|\le1\). The parent with paired Bloch vectors \(\pm\mathbf g_i\), and classical response means \(\pm t_{xi}\), realizes the family after uniform division by P/4. Equivalently it supplies a sign-decomposition of total norm at most P/4. This proves equality. The all-zero case is trivial.

An explicit optimal dual certificate avoids searching over Bell inequalities. For \(\mathbf e_\theta=(\cos\theta,\sin\theta)\), choose a setting attaining

\[
 h_K(\theta)=\max_x|\mathbf e_\theta\cdot\mathbf a_x|.
\]

Let \(\chi_x(\theta)\) indicate that selected setting and let \(\epsilon_x(\theta)\) be the sign of its dot product. Define

\[
 \mathbf h_x=\frac14\int_0^{2\pi}\chi_x(\theta)\epsilon_x(\theta)\mathbf e_\theta\,d\theta.
 \tag{4}
\]

The pairing is \(\frac14\int h_K=P/4\). For any sign string s and any unit vector d,

\[
 \left|\mathbf d\cdot\sum_xs_x\mathbf h_x\right|
 \le\frac14\int_0^{2\pi}|\mathbf d\cdot\mathbf e_\theta|d\theta=1.
\]

Hence (4) is feasible in (2). The angular integral is piecewise elementary, determined by the finite convex hull. Ties can be resolved measurably in any fixed way. Polygon tangents give the same certificate; the checker uses that finite formula and verifies all local sign sums directly.

## 4. Turning the certificate into a GHZ Bell inequality

Set \(z_x=a_{x1}+ia_{x2}\) and \(c_x=h_{x1}+ih_{x2}\). For N parties use the full-correlation Bell functional

\[
 \mathcal B_N=\sum_{x_1,\ldots,x_N}
 \operatorname{Re}\!\left[e^{i\gamma}\prod_{j=1}^N c_{x_j}\right]
 \left\langle\prod_{j=1}^N A_{x_j}^{(j)}\right\rangle.
 \tag{5}
\]

Every deterministic local assignment obeys

\[
 |\mathcal B_N|
 =\left|\operatorname{Re}\left[e^{i\gamma}
 \prod_{j=1}^N\sum_x c_xs_x^{(j)}\right]\right|\le1.
 \tag{6}
\]

Convexity extends this to all local hidden-variable strategies. No communication or postselection is involved.

The quantum calculation only needs one two-by-two matrix,

\[
 T=\sum_xc_xA_x=\begin{pmatrix}0&u\\v&0\end{pmatrix},\quad
 u=\sum_xc_x\bar z_x,\quad v=\sum_xc_xz_x.
\]

For an optimal dual certificate, u is real and equals \(\nu\): a nonzero imaginary part would allow a common rotation of all h to increase the feasible real pairing. Also \(|v|\le\nu\), by conjugating and rotating the certificate. The Bell operator is

\[
 \widehat{\mathcal B}_N=
 \frac12\left[e^{i\gamma}T^{\otimes N}
 +e^{-i\gamma}(T^\dagger)^{\otimes N}\right].
\]

Its matrix element between \(|0\rangle^{\otimes N}\) and \(|1\rangle^{\otimes N}\) is

\[
 b_N=\frac12\left[e^{i\gamma}u^N+e^{-i\gamma}\bar v^N\right].
\]

Choose \(\gamma=-N\arg(v)/2\) when v is nonzero, and choose the GHZ relative phase to be \(-\arg b_N\). If v is zero, the corresponding phase is unrestricted. The resulting state gives

\[
 \boxed{\langle\widehat{\mathcal B}_N\rangle
 =\frac{\nu^N+|v|^N}{2}\ge\frac{\nu^N}{2}.}\tag{7}
\]

Therefore a sufficient party count is

\[
 \boxed{
 N=\max\left\{2,\left\lfloor\frac{\ln2}{\ln\nu}\right\rfloor+1\right\},
 \qquad\nu=P/4>1.
 }\tag{8}
\]

**Author-side constructive conclusion:** every incompatible finite unbiased binary coplanar qubit family violates an explicitly specified Bell inequality on a sufficiently large GHZ state, with exactly that family used at every party. Conversely, a compatible family is Bell local on every state. Equation (8) is sufficient, not minimal.

A nonoptimal certified witness also works: if its real pairing is w>1, phase optimization yields a value at least \(w^N/2\). Thus numerical construction of an exactly optimal hull certificate is not a correctness premise. The exact rational example below uses this observation, and actually needs no adjusted GHZ phase.

## 5. An irregular, pairwise-compatible example

Use exactly the three rational Bloch vectors

\[
 \mathbf a_1=(0.70,0),\quad
 \mathbf a_2=(-0.42,0.56),\quad
 \mathbf a_3=(-0.28,-0.66).
\]

Each pair is jointly measurable. The standard unbiased two-qubit-effect criterion
\(\|a+b\|+\|a-b\|\le2\) is equivalently
\(1+(a\cdot b)^2-\|a\|^2-\|b\|^2\ge0\) here. The three exact positive margins are

\[
 \frac{26609}{250000},\quad\frac{2151}{62500},\quad\frac{3719}{62500}.
\]

The complete triple has \(P/4\simeq1.05775505>1\). This decimal is not used to certify nonlocality. Instead use the exact rational complex coefficients

\[
 c_1=0.492044+0.025383i,\quad
 c_2=-0.271368+0.376503i,\quad
 c_3=-0.226537-0.492541i.
\]

All six-decimal entries are exact rationals. Enumerating just eight local sign strings proves

\[
 \max_s\left|\sum_xs_xc_x\right|^2
 =\frac{499999562849}{500000000000}<1.
\]

The two off-diagonal entries are exactly

\[
 u=\frac{52887723-i}{50000000},\qquad
 v=\frac{-704151-245167i}{50000000}.
\]

At N=13, with \(\gamma=0\) and the ordinary real GHZ state,

\[
 \boxed{
 \mathcal B_{13}=\frac12\operatorname{Re}(u^{13}+v^{13})
 =1.037464516759\ldots>1.
 }\tag{9}
\]

The inequality is verified by exact fraction arithmetic before conversion to the displayed decimal. No large state-vector calculation, local-polytope relaxation or statistical sample estimates the violation. Mixing this state with 2% maximally mixed state gives \(0.98\mathcal B_{13}=1.0167152264\ldots>1\), also certified rationally. This is global white-state noise, not independent per-site detector noise.

If every party were restricted to any chosen pair of these local settings, each local family would have a parent measurement and no Bell inequality could be violated on any shared state. The 13-party construction uses all three settings. This does **not** establish that 13 parties are necessary, or that the full three-setting family is Bell local in every smaller experiment. Pairwise compatibility is not bipartite locality of the full triple.

## 6. Symmetric controls and resource boundaries

For the standard equal-sharpness trine \(a_x=\eta(\cos(2\pi x/3),\sin(2\pi x/3))\), choose \(c_x=e^{2\pi ix/3}/2\). Then \(u=3\eta/2\) and v=0. Choosing \(\gamma=\pi/6\) gives the exact local bound \(\sqrt3/2\), since nonzero local sums have sixth-root phases. The quantum/local ratio is

\[
 \frac{(3\eta/2)^N}{\sqrt3}.
\]

Thus this known regular-polygon construction suffices at N=111 for eta=0.67, N=12 for eta=0.70, and N=4 for eta=0.80. These are exact inequality comparisons and not optimum party counts. Symmetric multisetting GHZ constructions already exist [DVP24]; their regular-polygon improvements are not claimed as the new contribution.

The general sufficient bound grows as \(N\sim\ln2/(\nu-1)\) near compatibility. It is an existence/construction bound, not a claim of efficient experimental sampling. The Bell tensor has a product-form description, so its coefficients can be generated without storing all \(m^N\) entries. Estimating the required expectation with a small statistical error is a different resource question and has not been optimized.

For the irregular witness, 2% global white-state noise is tolerated but 1% additional independent shrinkage of every local Bloch vector multiplies the signal by \(0.99^{13}\) and defeats this particular violation. That is not a proof that no other inequality or state would work. The construction requires a shared orientation for designing the state and inequality; miscalibration, detector bias and no-click outcomes are not implicitly corrected. A Bell violation of the chosen inequality would exclude fully local hidden-variable models, but genuine N-party nonlocality, self-testing, cryptographic rates and entanglement-depth bounds are not established.

## 7. Prior-art assessment and the bounded next task

[PGQ25] proves the broader existence theorem and explicitly asks which known state families and how many parties suffice. Our candidate only answers its unbiased planar subclass, with a concrete GHZ prescription. It does not solve the full noncoplanar or biased problem. [LN22] supplies the established norm viewpoint, in a bipartite fixed-Alice measurement setting. [DVP24] supplies sophisticated regular-polygon GHZ inequalities. [Y26] announces the precise planar compatibility geometry. [AK20] supplies relevant compatibility and subset-compatibility background.

The strongest objection is that (5)–(8) may be an immediate or already recorded corollary once these tools are combined. The particular state-family/party-count implication was not found in the inspected passages. This does not certify novelty. In particular, the full [Y26] preprint is unread, and its discussion could contain exactly the relevant link. Its recent date is not evidence either for or against that possibility.

**Retain one bounded follow-up:** check whether an existing theorem or construction already implies (5)–(8) for arbitrary irregular unbiased coplanar families, and critically rederive the compatibility-to-GHZ implication. If subsumed, record that and stop this formulation. If not, assess whether closing this constructive subclass is consequential enough for focused development. Do not automatically expand to arbitrary bias, higher dimension, state preparation hardware, or exact minimum party counts. The present result is more than a selected numerical point, but no PRL commitment or repository is warranted by this first pass alone.

## 8. Verification and provenance

Five check groups cover the parent/dual geometry, an exact rational 13-party inequality, explicit local-strategy and Bell-operator checks for two to four parties, the symmetric-trine controls, and the locality/noise boundaries. The largest dense quantum operator constructed is 16 by 16. The 13-party certificate uses powers of two rational complex scalars, not an 8192-dimensional simulation. Repeated output is compared byte-for-byte. The general proof is analytical; tests are neither a novelty certificate nor independent scientific review.

No prior scientific checker is imported or rerun. Only the two separation/interaction documents were read from the prior context. Their hashes are recorded, and no protected repository is accessed. No publisher PDF, font or unrelated attachment is redistributed.

### Primary sources and actual reading boundaries

[PGQ25] M. Plavala, O. Guhne and M. T. Quintino, *All Incompatible Measurements on Qubits Lead to Multiparticle Bell Nonlocality*, PRL134,200201 (2025). [Author HTML v3](https://arxiv.org/html/2403.10564v3), [publisher](https://doi.org/10.1103/PhysRevLett.134.200201). Main theorem and proof structure, trine example, and Discussion questions about GHZ/Dicke states and party count inspected. The complete positive-map theorem was not independently reproved.

[Y26] T. Yoshino, K. Tojo, K. Hagihara, A. Tanaka and T. Tomita, *Joint measurability of coplanar POVMs*, [arXiv:2609.38836](https://arxiv.org/abs/2609.38836), submitted30September2026. **Primary indexed abstract only.** Direct abstract, HTML and PDF requests failed. The convex-hull convention and proof used here are supplied explicitly above; no claim of full-text novelty clearance is made.

[LN22] F. Loulidi and I. Nechita, *Measurement Incompatibility versus Bell Nonlocality: An Approach via Tensor Norms*, PRX Quantum3,040325 (2022). [Author PDF v2](https://arxiv.org/pdf/2205.12668). Introduction, operational setting and main-results Section2, especially compatibility norm and bipartite assumptions inspected. Not an exhaustive audit of all later sections or cited tensor-norm generalizations.

[DVP24] S. Designolle, T. Vertesi and S. Pokutta, *Symmetric multipartite Bell inequalities via Frank-Wolfe algorithms*, PRA109,022205 (2024). [Author PDF](https://arxiv.org/pdf/2310.20677). Regular-polygon observables and GHZ correlations Eqs.(6)–(8), overview and concluding scope inspected. No numerical table/plot values imported or superiority to its optimized facets claimed.

[AK20] N. Andrejic and R. Kunjwal, *Joint measurability structures realizable with qubit measurements: Incompatibility via marginal surgery*, PRR2,043147 (2020). [Author PDF](https://arxiv.org/pdf/2003.00785). Definitions, unbiased/coplanar distinctions and two-/three-measurement compatibility statements inspected. No priority claim for pairwise-compatible triples.

[BV18] E. Bene and T. Vertesi, *Measurement incompatibility does not give rise to Bell violation in general*, NJP20,013021 (2018). [Author PDF](https://arxiv.org/pdf/1705.10069), rendering dated14June2021. Introduction, setting and conclusions inspected as a scope check: pairwise compatibility and full-family bipartite locality are distinct. No numerical assertion of all-state bipartite locality for our irregular triple is imported.

All figure/table data are excluded from the source claims in this note; mathematical text was the reading surface. Search-only results, generated summaries and unrelated quantum-control/topological-pump leads are not used as technical evidence.
