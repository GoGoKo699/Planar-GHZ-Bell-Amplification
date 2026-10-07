# Proof and contribution boundaries

This note examines the proof obligations and predecessor boundaries of [THEOREM](../docs/THEOREM.md). The [source audit](../literature/SOURCE_AUDIT.md) derives the regular-polygon exponent already known for every setting count; [operational consequences](OPERATIONAL_CONSEQUENCES.md) explain fixed-margin party cost and noise.

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

The proof uses the finite, known, unbiased binary coplanar qubit family specified in [MODEL_AND_CLAIMS](MODEL_AND_CLAIMS.md), fixed at every site as $`N`$ grows. Its rescalings are mathematical comparisons.

## What the strongest shortcuts do and do not establish

[Plavala–Guhne–Quintino, v4](https://arxiv.org/html/2403.10564v4), Theorem 3, gives nonlocality of the complete measurement behavior for some state and party number. It does not supply a full-correlation witness. Corollary 6 concerns behavior-locality visibility thresholds. Their discussion leaves state-family identification and party bounds open.

The following is a logical comparison, not a further claim attributed to that paper. The planar block argument applies to operators with one equatorial observable at every site. A general Bell expression may contain identities at unmeasured sites and need not have that block structure. Therefore general activation plus planar block diagonalization does not, by itself, prove the present full-correlation construction. Even for a full-correlation tensor, the maximizing complementary block need not be canonical; the theorem's existing counterexample prevents that inference. The construction must still select a suitable tensor and align its canonical block.

[Werner–Wolf](https://arxiv.org/pdf/quant-ph/0102024), Section V.D, realizes extremal correlations with a GHZ state by choosing suitable observables. Its two-setting scope is explicit in Section VII. Those freedoms do not identify a witness for every prescribed many-setting family. [Loulidi–Nechita, v2](https://arxiv.org/html/2205.12668v2), Definition 6.1 and Theorems 8.1–8.2, supply compatibility/Bell norm comparisons in a bipartite optimization with Alice's family fixed. The compatible-parent upper-bound principle is inherited.

## A symmetric exponent already contained in prior work

[Designolle–Vertesi–Pokutta, v2](https://arxiv.org/html/2310.20677v2), Section IX.A (IX.1 in HTML), Eqs. (34)–(35), gives all-party quantum and local values for four regular planar projective settings. Write

```math
\alpha=1+\frac1{\sqrt2},\qquad
\delta=1-\frac1{\sqrt2},\qquad
\ell_n=\alpha^n-\delta^n.
```

Their formulas give

```math
Q_{2n-1}=4^{2n-2},\qquad Q_{2n}=\sqrt2\,4^{2n-1},
\qquad
L_{2n-1}=\frac{4^{n-1}\ell_n}{\sqrt2},\qquad
L_{2n}=\frac{4^n\ell_n}{\sqrt2}.
```

Our direct inference from these formulas is

```math
\lim_{N\to\infty}\left(\frac{Q_N}{L_N}\right)^{1/N}
=\frac{2}{\sqrt{1+1/\sqrt2}}
=4\sin\frac{\pi}{8}=\nu_4.
```

Here the symmetric hull is a regular unit circumradius octagon, with perimeter divided by four equal to $`\nu_4`$. Thus the compatibility-scale exponent is already present in this symmetric case. We claim no new exponent or improved finite-party inequality for that example. What the cited construction does not supply is the arbitrary irregular, unequally sharp fixed-family result with the matching all-state bound.

## Contribution boundary

The precise additional implication is the uniform conversion of **every** family's inherited optimal planar certificate into real Bell coefficients and a phase-adjusted canonical GHZ state, attaining at least half the norm to the Nth power, together with an all-state full-correlation ceiling at the same exponential scale. The measurement family remains fixed. This is more specific than eventual nonlocality and more general in its permitted measurement geometry than the symmetric construction above.

The geometry, locality principle and complex GHZ algebra are established ingredients; the bridge between them is short. Its value rests on the uniform constructive conclusion and operational exponent. The inspected sources do not directly supply the complete statement. [ATTRIBUTION](../literature/ATTRIBUTION.md) records the limits of that source comparison; [MODEL_AND_CLAIMS](MODEL_AND_CLAIMS.md) specifies the scientific scope.

## Source and verification boundaries

The Yoshino v1 source was checked against the uploaded PDF with the SHA-256 in [IMPORT.json](../provenance/IMPORT.json), focusing on Theorem 1.3, Proposition 3.1, Lemma 2.21 and the certificate construction in Section 3. No third-party PDF is redistributed. The PGQ, WW and LN passages above were reread. The DVP comparison uses the explicitly versioned v2 HTML; the unversioned PDF also returned a v3 dated 5 October 2026 with the same relevant formulas. Failed retrievals are not used as negative evidence. The wider archived literature audit remains bounded by its recorded access depth.

Reproduction and exact-revision evidence, including reports and source hashes, are described in [VERIFICATION](../VERIFICATION.md).
