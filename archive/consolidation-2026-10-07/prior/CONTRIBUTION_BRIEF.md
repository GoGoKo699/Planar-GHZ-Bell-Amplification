# From planar compatibility to optimal GHZ Bell amplification

**Research brief, 7 October 2026. Author-side claim; no priority or acceptance certificate.**

## Physical question

A fixed collection of noisy qubit measurements may fail to expose nonlocality in small experiments even when it is incompatible. For unbiased binary measurements in one Bloch plane, must one search over complicated many-qubit states, or can a familiar GHZ family expose every incompatible collection? What is the best exponential amplification attainable with those same detectors?

## Fixed resources

Every party uses the same finite family

$$M_{\pm|x}=(I\pm A_x)/2,\qquad A_x=\mathbf a_x\cdot(\sigma_x,\sigma_y),\quad\|\mathbf a_x\|\le1.$$

Settings can be irregular, unequally sharp, repeated, or redundant. No postselection or extra measurement setting is supplied. The family stays fixed while the party number N grows. Bell functionals contain only full N-party products of outcomes; terms involving proper subsets of parties are outside the amplification theorem.

## Inherited geometric input

Yoshino et al., arXiv:2609.38836v1, Theorem1.3 and Proposition3.1, establish compatibility iff

$$\nu=\tfrac14\operatorname{perimeter}(\operatorname{conv}\{\pm\mathbf a_x\})\le1.$$

Their Lemma2.21 and Definitions3.3–3.7 explicitly construct optimal primal/dual certificates. In our notation the dual is

$$\max_{s_x=\pm1}\left|\sum_xs_xc_x\right|\le1,\qquad
\sum_xc_x\bar z_x=\nu,\quad z_x=a_{x1}+ia_{x2}.$$

The remaining complex sum v=sum_x c_x z_x obeys |v|<=nu. Neither the norm, perimeter theorem, parent, nor dual construction is claimed as new.

## Candidate Bell theorem

Let R_N be the optimal absolute full-correlation Bell value normalized by its exact local bound, optimized over all N-qubit states and real Bell tensors, with the prescribed family at every site. Let R_N^GHZ restrict the state to a phase-adjusted GHZ state in the common measurement-plane basis. Then

$$\boxed{\tfrac12\nu^N\le R_N^{\rm GHZ}\le R_N\le\nu^N.}$$

Consequently their Nth-root limits both equal nu. Every incompatible family therefore admits a constructive GHZ violation, with any integer N>=2 satisfying nu^N>2 sufficient.

## Proof in two steps

**Construction.** Use beta_{x_1...x_N}=Re[e^{i gamma}prod_j c_{x_j}]. Its deterministic local values factor into bounded one-party sign sums. The quantum operator is one-half of e^{i gamma}T^{tensor N}+h.c., with T=[[0,nu],[v,0]]. Aligning gamma and the GHZ phase gives (nu^N+|v|^N)/2. The remaining complementary-bitstring blocks have no larger eigenvalue magnitude. Thus the selected GHZ exactly maximizes its constructed functional.

**Converse.** A_x/nu is compatible by the inherited norm theorem. Such measurements generate local correlations on every state. Restoring N factors of nu multiplies any full-correlation functional by nu^N. This bounds every competing state and Bell tensor. Squeezing the Nth roots establishes the exponent.

The proof is analytical. Scalar examples and finite-matrix checks are diagnostics, not premises for the all-state assertion.

## Precise predecessor distinction

Plavala–Guhne–Quintino's 2025 PRL proves general incompatible-qubit activation and explicitly asks about familiar state families and party counts. This resolves only the unbiased binary planar subclass. Existing regular-polygon GHZ constructions and compatibility-norm Bell upper bounds are inherited methods. The additional statement is their constructive class-wide connection with a matched exponential converse for an arbitrary fixed planar family.

The uploaded compatibility paper develops no Bell/state construction or amplification theorem. This closes that specific access/overlap question. It does not prove that no other paper implicitly or explicitly establishes the same connection.

## Meaning and limits

The comparison says that more complicated states cannot improve the exponential full-correlation rate over GHZ for these detectors. It does not show exact finite-N optimality of the Bell functional, minimal N for an arbitrarily small violation, genuine multipartite nonlocality, nonlocality depth, self-testing, efficient sample complexity, or robustness to biased/no-click outcomes.

For a fixed target ratio R>1, necessary N>=ln(R)/ln(nu) and sufficient nu^N>2R give the same inverse-(nu-1) order near compatibility. These concern normalized Bell values, not the total number of experimental trials.

## Assessment

Retain the bounded theorem. The meaningful remaining judgment is whether this constructive solution and operational norm equality are a sufficiently consequential addition to the closest results. Its short proof is neither a reason to reject it nor evidence of importance by itself. No broader measurement model or additional experimental design is a prerequisite to making that judgment.
