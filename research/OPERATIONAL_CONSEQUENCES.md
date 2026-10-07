# Operational consequences and proof boundaries

These consequences follow from [THEOREM](THEOREM.md) for the same fixed, finite, unbiased binary coplanar qubit family and full-correlation objective. They introduce no additional measurement resource or claim about experimental or statistical efficiency. The [source audit](../literature/SOURCE_AUDIT.md) supplies the strengthened predecessor comparison.

## What the geometric quantity measures

For the nonzero family, write

$$
\nu=\frac{\operatorname{perimeter}(\operatorname{conv}\{\pm\mathbf a_x\})}{4},
\qquad r=\max_x\|\mathbf a_x\|.
$$

The quantity nu is a compatibility gauge: dividing every Bloch vector by nu puts the family on the joint-measurability boundary. This rescaling remains a valid mathematical comparison even for nu below one, since r is at most nu. It is not a generalized incompatibility robustness, which permits arbitrary noise measurements.

For uniform attenuation `0 <= eta <= 1`, the observables become `eta A_x`, and every full-correlator Bell operator scales by `eta^N`. Its exact local absolute bound is unchanged. Therefore

$$
\mathcal R_N(\eta A)=\eta^N\mathcal R_N(A),\qquad
\mathcal R_N^{\rm GHZ}(\eta A)=\eta^N\mathcal R_N^{\rm GHZ}(A),\qquad
\nu(\eta A)=\eta\nu.
$$

The maximal compatible depolarizing visibility is

$$
\eta_{\rm JM}=\min\{1,1/\nu\}.
$$

For the zero family it is one. For an originally incompatible family, eventual GHZ activation under this attenuation occurs exactly when `eta nu > 1`; equality is compatible. Thus the optimal exponential factor is `eta nu`. This is a uniform, unbiased outcome-noise model, not a no-click or detection-efficiency model. Under the convention `(M + t I/2)/(1+t)`, the white-noise mixing ratio required for compatibility is `max(0, nu-1)`. Neither this number nor nu is assigned the meaning of arbitrary-noise robustness.

## A finite bound on the logarithmic rate

The theorem gives an explicit finite-size estimate, not only a limit. For the nonzero family and every `N >= 2`,

$$
\log\nu-\frac{\log2}{N}
\le\frac{\log\mathcal R_N^{\rm GHZ}}{N}
\le\frac{\log\mathcal R_N}{N}
\le\log\nu+\frac{\log(r/\nu)}{N}.
$$

Both logarithmic rates lie within `log(2)/N` below `log(nu)`. No numerical extrapolation is needed. If `W_N` is the exact normalized value of the theorem's explicit witness, then

$$
1\le\frac{\mathcal R_N}{W_N}\le\frac{2r}{\nu}\le2.
$$

The comparison concerns normalized Bell values. It does not compare the excess above the local bound, the number of trials, or the cost of preparing a state. A compact formula for a Bell tensor does not itself provide an efficient sampling protocol.

## Fixed-margin party cost and rounding

For `nu > 1` and a fixed target `R > 1`, define

$$
N_R=\min\{N\ge2:\mathcal R_N\ge R\}.
$$

The upper bound in the theorem is necessary for any state and full-correlation functional; the explicit GHZ construction gives the sufficient bound. Hence

$$
\left\lceil1+\frac{\log(R/r)}{\log\nu}\right\rceil
\le N_R
\le\max\left\{2,\left\lceil\frac{\log(2R)}{\log\nu}\right\rceil\right\}.
$$

For the strict target `> R`, the sufficient party count is

$$
\max\left\{2,\left\lfloor\frac{\log(2R)}{\log\nu}\right\rfloor+1\right\}.
$$

These statements do not assume that the exact optimum is monotone in N. The necessary condition holds for every candidate N, and the sufficient condition constructs a witness at the displayed N.

Since `r <= 1`, putting `nu = 1 + epsilon` yields, for a fixed `R > 1` and sufficiently small positive epsilon,

$$
1+\frac{\log R}{\log(1+\epsilon)}
\le N_R
\le\frac{\log(2R)}{\log(1+\epsilon)}+1.
$$

Thus `N_R = Theta(1/epsilon)` uniformly even when the family varies as epsilon tends to zero. The result specifies the order, not an exact leading coefficient. It does not determine the minimum parties for an arbitrarily small violation, where the target is not fixed above one.

## Global white-state noise is a different parameter

Let `0 <= w <= 1` be the visibility in

$$
\rho_w=w|\mathrm{GHZ}_{N,\varphi}\rangle\langle\mathrm{GHZ}_{N,\varphi}|
+(1-w)\frac{I}{2^N}.
$$

Every full-correlation Bell operator here is traceless. Its expectation on this state is w times the pure-state expectation. Combining this state noise with uniform local attenuation multiplies a specified witness value by `w eta^N`, not by `w^N eta^N`.

For fixed positive w, the construction reaches at least R whenever

$$
w(\eta\nu)^N\ge2R.
$$

A constant global white-state visibility leaves the witness's exponential factor unchanged, while fixed local attenuation changes it to `eta nu`. A visibility that itself decays with N need not preserve the rate. These are algebraic consequences for the stated noise models, not preparation-fidelity guarantees, calibration-error bounds, or sampling-cost results.

## Exact normalization and the archived certificates

The definition of `R_N` uses the exact local absolute bound `L(beta)`. The constructive proof only needs `L(beta) <= 1`; it never requires equality. Its positive quantum value ensures the Bell tensor is nonzero, and local sign strategies span the tensor space, so `L(beta) > 0`.

The original rational witness report's field `local_absolute_bound = 1` denotes the certified conservative bound used by that checker. It is not an assertion that the exact local maximum equals one. Indeed its rounded one-site coefficients satisfy

$$
\max_s\left|\sum_xc_xs_x\right|^2
=\frac{499999562849}{500000000000}<1.
$$

Their N-site local bound is therefore strictly below one. Dividing by its exact value can only improve the archived sufficient violations. The rational coefficients, the geometric coefficients used for the all-N identity, and their corresponding values remain distinct. No archived script, report, or certificate is corrected or replaced by this explanation.

## Proof obligations resolved within the declared model

| Obligation | Analytical resolution |
|---|---|
| Geometric certificate and complex normalization | The source columns telescope to `sum c_x conjugate(z_x) = nu`, with an exactly real result, and `abs(sum c_x z_x) <= nu`. The centered symmetric hull is essential. |
| Real Bell coefficients, phases and the maximizing block | Realification gives the Hermitian operator in the theorem. The chosen phases align both terms in every complementary-bitstring block; `(1-t^k)(1-t^(N-k)) >= 0` makes the canonical block maximal. |
| All-state ceiling, including `nu < 1` | The rescaled observables are valid; the first N-1 compatible parents supply a hidden variable with setting-independent probability, and the last site's conditional Born response supplies a local response. |
| Zero, collinear and redundant settings | Zero and collinear families are handled before polygon divisions. Signed reordering is undone, and unused settings receive zero coefficients. No extra setting is required. |
| Full behavior and full-correlation scope | The constructed GHZ's proper equatorial marginals vanish. Shared output signs with product one erase proper marginals of a local full tensor. This does not extend the all-state homogeneous bound to arbitrary marginal terms. |
| Finite examples and all-N reasoning | Rational enclosures prove the archived exclusions and sufficient witnesses. The arbitrary-N theorem rests on the analytical construction and converse, not finite tests. |

No unresolved scientific premise was identified for the stated claim in this internal audit. The remaining limitation is the bounded nature of the source comparison, not a queued experiment or stronger-model theorem. Regular-polygon amplification and complex product constructions are inherited; the retained additional implication is the arbitrary fixed-family certificate conversion with the matching all-state full-correlation rate. See [MODEL_AND_CLAIMS](MODEL_AND_CLAIMS.md) for all nonclaims. Reopen research for a concrete proof objection or a directly covering source.
