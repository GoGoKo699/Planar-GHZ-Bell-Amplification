# Fixed-family source audit

This primary-source comparison explains the regular-polygon predecessors and the boundary of the arbitrary fixed-family [claim](../research/MODEL_AND_CLAIMS.md). [ATTRIBUTION](ATTRIBUTION.md) records inherited inputs and source-reading limits; the [proof review](../research/CONTRIBUTION_REVIEW.md) examines the construction and converse.

## Regular-polygon amplification was already known for every setting count

Nagata, Laskowski and Paterek, [*Bell inequality with an arbitrary number of settings and its applications*](https://arxiv.org/abs/quant-ph/0601107v2), PRA 74, 062109 (2006), explicitly give in Eq. (38)

$$
V(N,M)=\frac{[M\sin(\pi/(2M))]^N}{2\cos(\pi/(2M))},\qquad M\ge2.
$$

Equations (6)-(7), (17), (22) and (24) specify the regular settings, absolute local bound, GHZ value and Bell spectrum. The accessible [unversioned primary PDF](https://arxiv.org/pdf/quant-ph/0601107) identifies v2, 31 October 2006 in its arXiv header. Versioned PDF/HTML retrieval failures are not negative evidence.

The following comparison to detectors fixed as $`N`$ varies is our derivation. Put $`\theta_m=\pi m/M`$ and rename the source's parity parameter as

$$
\xi_N=[M+1]_2[N]_2+1,\qquad
\delta_N=\frac{\pi\xi_N}{2MN},\qquad\Gamma_N=N\delta_N.
$$

Keep the fixed observables at $`\theta_m`$. Use coefficients $`\cos(\sum_{j=1}^N\theta_{m_j}+\Gamma_N)`$ and the permitted canonical-GHZ phase $`\varphi=-\Gamma_N`$. The GHZ correlations equal these coefficients, and their squared sum gives $`Q_N=M^N/2`$. The common $`N`$-dependent angular offset is absorbed in the state and Bell phases rather than supplied by changing the detectors.

For an independent check of the absolute local bound, let $`\alpha=\pi/(2M)`$. The convex hull of sign sums $`\sum_m s_m e^{i\theta_m}`$ is a regular $`2M`$-gon zonotope of circumradius $`\csc\alpha`$. Its vertex arguments are $`(M-1)\alpha+2k\alpha`$. The real product expression is separately real-linear, so its maximum absolute value is attained at vertices. Adding $`\Gamma_N`$ makes the product argument an odd multiple of $`\alpha`$. Consequently

$$
L_N=\csc(\alpha)^N\cos\alpha,\qquad
\lim_{N\to\infty}V(N,M)^{1/N}=M\sin\alpha
=\frac{\mathrm{perimeter}(K_M)}4.
$$

Common sharpness $`t`$ multiplies each full correlator by $`t^N`$, giving root rate $`tM\sin\alpha`$. The fixed-detector phase absorption and this noise translation are elementary inferences made here. No new priority is assigned to the regular-polygon exponent, its uniformly noisy version, or the complex product method. The paper's communication-complexity applications are not transferred to the present theorem.

## The precise remaining implication

The current theorem takes any prescribed finite unbiased binary coplanar qubit family, including irregular directions and unequal sharpness, converts its inherited optimal planar certificate into explicit real Bell coefficients and a phase-adjusted canonical GHZ state, and compares it with every state and full-correlation functional:

$$
\nu^N/2\le\mathcal R_N^{\rm GHZ}\le\mathcal R_N
\le r\nu^{N-1}.
$$

No inspected passage supplies this complete arbitrary-family implication. The geometric classification, general activation theorem, compatibility-bound principle and complex GHZ algebra are inherited. The bridge is short, so the result should be assessed as a uniform constructive and quantitative consequence, without treating known amplification as a newly discovered phenomenon.

## Dependency and subsumption comparisons

| Primary source and inspected passages | Established input and remaining boundary |
|---|---|
| Yoshino et al., [2609.38836v1](https://arxiv.org/html/2609.38836v1), Theorem 1.3, Proposition 3.1, Lemma 2.21, Definitions 3.3-3.7 and Sections 3.3-3.6 | Supplies the centered symmetric-hull perimeter, exact compatibility gauge, reduction and optimal primal/dual certificate. The column formula and complex telescoping identity match the declared model. The source is not presented as a Bell construction. |
| Plavala-Guhne-Quintino, [2403.10564v4](https://arxiv.org/html/2403.10564v4), Theorem 3, Corollary 6 and Discussion | Supplies general incompatible-qubit activation, the all-but-one-compatible-sites locality observation, and behavior-visibility convergence. It leaves familiar-state and party-count questions explicit. This work answers only the stated planar subclass and full-correlation rate. |
| Loulidi-Nechita, [2205.12668v2](https://arxiv.org/html/2205.12668v2), Definition 6.1 and Theorems 8.1-8.2 | Supplies compatibility/Bell norm comparisons with Alice's family fixed and Bob optimized in a bipartite task. The current task repeats the same prescribed family at every site. |
| Werner-Wolf, [quant-ph/0102024](https://arxiv.org/pdf/quant-ph/0102024), Sections V.D and VII | Supplies GHZ extremality with suitably chosen observables in the two-setting full-correlation scenario. It does not specify an arbitrary prescribed many-setting noisy family. |
| Nagata-Laskowski-Paterek, [quant-ph/0601107v2](https://arxiv.org/abs/quant-ph/0601107v2), Eqs. (6)-(7), (17), (22), (24), (38) | Supplies the all-setting-count regular-polygon rate above. The irregular unequal-sharpness certificate conversion and its matching all-state converse are not stated in the inspected argument. |
| Designolle-Vertesi-Pokutta, [2310.20677v3](https://arxiv.org/html/2310.20677v3), Section IX.A, Eqs. (34)-(35), with comparison to [v2](https://arxiv.org/html/2310.20677v2) | Supplies optimized symmetric constructions and the four-setting special-case exponent. These formulas are unchanged in v3. The surrounding recurrence is corrected to $`L_{N+4}=8(L_{N+2}-L_N)`$ with $`L_{2n}=4L_{2n-1}`$. The versions are not claimed identical. No superiority in finite-party constants, detection efficiency or statistical cost is asserted. |
| Salles et al., [1002.1893](https://arxiv.org/abs/1002.1893), Section 6.2, Proposition 10 | Multilinear contractions recover linear correlation Bell inequalities. That generic framework is inherited; the inspected passage does not identify the optimal geometric certificate or perimeter rate for every prescribed irregular noisy planar family. |
| Karczewski et al., [2202.06606](https://arxiv.org/abs/2202.06606), Sections 4.1-4.2, especially Eqs. (15)-(16) | Supplies complex tensor coefficient constructions and broader setting/outcome frameworks. The product-complex method receives no new-priority framing; the specific optimal certificate conversion is the comparison point. |

The comparisons use the listed primary passages and the reading boundaries in [ATTRIBUTION](ATTRIBUTION.md) and the [historical source records](../archive/README.md). No directly covering theorem was found in those passages. Failed retrievals and irrelevant search results are not evidence of absence; the comparison does not certify priority against all literature.
