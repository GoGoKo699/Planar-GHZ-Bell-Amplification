# Focused proof and contribution review

The subsequent [source audit](../literature/SOURCE_AUDIT.md) strengthens this dated review's symmetric comparison: Nagata-Laskowski-Paterek (2006) already give the perimeter exponent for every regular setting count. [Operational consequences](OPERATIONAL_CONSEQUENCES.md) record the completed prerequisite audit and clarify the exact normalization and fixed-margin interpretation. The theorem and the review below remain unchanged.

**7 October 2026. Decision: retain the theorem at its existing scope.** No blocking proof error was found. The contribution is a constructive, quantitative consequence of established compatibility geometry and GHZ methods. This review strengthens the acknowledgment of a symmetric predecessor; it does not change the theorem, its bounds, or its numerical evidence.

The reviewed baseline is main commit `54a805598ded79b5d8749f55e381cc690700a9fa`. This is an author-side review with parallel internal scrutiny, not external independent review or exhaustive priority clearance. [THEOREM](../docs/THEOREM.md) remains the mathematical specification; [ASSESSMENT](ASSESSMENT.md) preserves the preceding consolidation assessment.

## Proof obligations and findings

| Obligation in the theorem | Review finding |
|---|---|
| Section 3: inherited certificate and complex dictionary | The signed half-boundary coefficients agree with Yoshino et al.'s matrix construction. Telescoping gives a real upper-right entry equal to the perimeter norm; the other entry has modulus at most that norm. Interior, repeated and zero settings do not obstruct the construction. |
| Section 4: a real Bell tensor with a valid local bound | Each deterministic value factors into bounded complex sign sums, so the absolute local bound is at most one. It need not equal one. The positive constructed quantum value ensures that the tensor is nonzero. |
| Section 4: phase and maximizing state | The stated phase convention gives a positive GHZ expectation. The complementary-bitstring blocks obey the displayed two-term bound, whose maximum occurs in the canonical all-zero/all-one block. This applies to the constructed tensor. |
| Section 5: converse for every state | The parent outcomes at the first $`N-1`$ sites define the hidden variable; the conditional Born response at the last site is a local response. Restoring the homogeneous scales gives the stated ceiling, including when the norm is below one. |
| Section 2: root limit and degeneracies | The two bounds squeeze both root limits. The zero family vanishes; the collinear case attains exactly the longest-setting length to the Nth power. Neither case requires the polygon parametrization. |
| Section 6: finite-party statements | Exact rational enclosures retain the six-party and nineteen-party exclusions. The archived thirteen-party and twenty-five-party rational witnesses retain the respective sufficient violations. No exact minimum is inferred. |
| Section 7: scope of correlations | The proper equatorial marginals of the constructed GHZ state vanish. The even-parity output twirl preserves its full tensor and erases proper marginals. This does not give an all-state bound for Bell expressions containing marginal terms. |

The rounded rational witness used for the finite examples is a separate sufficient certificate. Its complex sum is not exactly the unrounded geometric norm. The exact geometric coefficients, rather than rounded numerical coefficients, establish the all-party identity and exponent. The original checkers already preserve this distinction.

No missing hypothesis was identified within the declared finite, known, unbiased binary coplanar qubit family, fixed at every site as $`N`$ grows. The comparisons use mathematical rescalings, not additional experimental measurements. The review does not assess a detector apparatus or a sampling protocol.

## What the strongest shortcuts do and do not establish

[Plavala–Guhne–Quintino, v4](https://arxiv.org/html/2403.10564v4), Theorem 3, gives nonlocality of the complete measurement behavior for some state and party number. It does not supply a full-correlation witness. Corollary 6 concerns behavior-locality visibility thresholds. Their discussion leaves state-family identification and party bounds open.

The following is a logical comparison, not a further claim attributed to that paper. The planar block argument applies to operators with one equatorial observable at every site. A general Bell expression may contain identities at unmeasured sites and need not have that block structure. Therefore general activation plus planar block diagonalization does not, by itself, prove the present full-correlation construction. Even for a full-correlation tensor, the maximizing complementary block need not be canonical; the theorem's existing counterexample prevents that inference. The construction must still select a suitable tensor and align its canonical block.

[Werner–Wolf](https://arxiv.org/pdf/quant-ph/0102024), Section V.D, realizes extremal correlations with a GHZ state by choosing suitable observables. Its two-setting scope is explicit in Section VII. Those freedoms do not identify a witness for every prescribed many-setting family. [Loulidi–Nechita, v2](https://arxiv.org/html/2205.12668v2), Definition 6.1 and Theorems 8.1–8.2, supply compatibility/Bell norm comparisons in a bipartite optimization with Alice's family fixed. The compatible-parent upper-bound principle is inherited.

## A symmetric exponent already contained in prior work

[Designolle–Vertesi–Pokutta, v2](https://arxiv.org/html/2310.20677v2), Section IX.A (IX.1 in HTML), Eqs. (34)–(35), gives all-party quantum and local values for four regular planar projective settings. Write

$$
\alpha=1+\frac1{\sqrt2},\qquad
\delta=1-\frac1{\sqrt2},\qquad
\ell_n=\alpha^n-\delta^n.
$$

Their formulas give

$$
Q_{2n-1}=4^{2n-2},\qquad Q_{2n}=\sqrt2\,4^{2n-1},
\qquad
L_{2n-1}=\frac{4^{n-1}\ell_n}{\sqrt2},\qquad
L_{2n}=\frac{4^n\ell_n}{\sqrt2}.
$$

Our direct inference from these formulas is

$$
\lim_{N\to\infty}\left(\frac{Q_N}{L_N}\right)^{1/N}
=\frac{2}{\sqrt{1+1/\sqrt2}}
=4\sin\frac{\pi}{8}=\nu_4.
$$

Here the symmetric hull is a regular unit circumradius octagon, with perimeter divided by four equal to $`\nu_4`$. Thus the compatibility-scale exponent is already present in this symmetric case. We claim no new exponent or improved finite-party inequality for that example. What the cited construction does not supply is the arbitrary irregular, unequally sharp fixed-family result with the matching all-state bound.

## The remaining contribution and stopping decision

The precise additional implication is the uniform conversion of **every** family's inherited optimal planar certificate into real Bell coefficients and a phase-adjusted canonical GHZ state, attaining at least half the norm to the Nth power, together with an all-state full-correlation ceiling at the same exponential scale. The measurement family remains fixed. This is more specific than eventual nonlocality and more general in its permitted measurement geometry than the symmetric construction above.

The strongest objection remains substantial: the difficult geometry, the locality principle, and the complex GHZ algebra are established ingredients; the bridge between them is short. Its value rests on the uniform constructive conclusion and operational exponent, not a new geometric theory or a new mechanism of GHZ nonlocality. The inspected sources do not directly supply the complete statement. That supports retaining a compact theoretical result, without claiming comprehensive novelty clearance.

The assigned contribution review is complete. No further scientific extension or large numerical study is needed to support the frozen claim on the evidence inspected. The next development pass should organize the exposition around the fixed-detector question, the one theorem, its short proof and this exact predecessor boundary. Reopen scientific work only for a concrete proof objection or a source containing the same implication. All nonclaims in [MODEL_AND_CLAIMS](MODEL_AND_CLAIMS.md) remain in force.

## Source and verification boundaries

The Yoshino v1 source was checked against the uploaded PDF with the SHA-256 in [IMPORT.json](../provenance/IMPORT.json), focusing on Theorem 1.3, Proposition 3.1, Lemma 2.21 and the certificate construction in Section 3. No third-party PDF is redistributed. The PGQ, WW and LN passages above were reread. The DVP comparison uses the explicitly versioned v2 HTML; the unversioned PDF also returned a v3 dated 5 October 2026 with the same relevant formulas. Failed retrievals are not used as negative evidence. The wider archived literature audit remains bounded by its recorded access depth.

The takeover baseline passed eight infrastructure tests and all 18 original scientific groups on local Python 3.12.14 with the pinned NumPy/SciPy versions; all four reports were byte-identical to their references. This is a cross-environment local result, not the pinned Python 3.13.5 hosted receipt. Exact PR-head and separate merged-main checks, including downloaded reports and source hashes, belong in the pull-request record under [VERIFICATION](../VERIFICATION.md). No archived source, canonical report, scientific tolerance, theorem or import hash is changed by this review.
