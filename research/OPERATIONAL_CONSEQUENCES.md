# Operational consequences

These consequences follow from [THEOREM](../docs/THEOREM.md) for the same fixed, finite, unbiased binary coplanar qubit family and full-correlation objective.

## What the geometric quantity measures

For the nonzero family, write

```math
\nu=\frac{\mathrm{perimeter}(\mathrm{conv}\{\pm\mathbf a_x\})}{4},
\qquad r=\max_x\|\mathbf a_x\|.
```

The quantity $`\nu`$ is a compatibility gauge: dividing every Bloch vector by $`\nu`$ puts the family on the joint-measurability boundary. This rescaling remains a valid mathematical comparison even for $`\nu`$ below one, since $`r`$ is at most $`\nu`$. It is not a generalized incompatibility robustness, which permits arbitrary noise measurements.

For uniform attenuation $`0\le\eta\le1`$, the observables become $`\eta A_x`$, and every full-correlator Bell operator scales by $`\eta^N`$. Its exact local absolute bound is unchanged. Therefore

```math
\mathcal R_N(\eta A)=\eta^N\mathcal R_N(A),\qquad
\mathcal R_N^{\rm GHZ}(\eta A)=\eta^N\mathcal R_N^{\rm GHZ}(A),\qquad
\nu(\eta A)=\eta\nu.
```

The maximal compatible depolarizing visibility is

```math
\eta_{\rm JM}=\min\{1,1/\nu\}.
```

For the zero family it is one. For an originally incompatible family, eventual GHZ activation under this attenuation occurs exactly when $`\eta\nu>1`$; equality is compatible. Thus the optimal exponential factor is $`\eta\nu`$. This is a uniform, unbiased outcome-noise model, not a no-click or detection-efficiency model. Under the convention $`(M+tI/2)/(1+t)`$, the white-noise mixing ratio required for compatibility is $`\max\{0,\nu-1\}`$. Neither this number nor $`\nu`$ is assigned the meaning of arbitrary-noise robustness.

## A finite bound on the logarithmic rate

The theorem gives an explicit finite-size estimate, not only a limit. For the nonzero family and every $`N\ge2`$,

```math
\log\nu-\frac{\log2}{N}
\le\frac{\log\mathcal R_N^{\rm GHZ}}{N}
\le\frac{\log\mathcal R_N}{N}
\le\log\nu+\frac{\log(r/\nu)}{N}.
```

Both logarithmic rates lie within $`\log(2)/N`$ below $`\log\nu`$. If $`W_N`$ is the exact normalized value of the theorem's explicit witness, then

```math
1\le\frac{\mathcal R_N}{W_N}\le\frac{2r}{\nu}\le2.
```

The factor of two compares normalized Bell values, rather than the excess above the local threshold of one. It is a value bound, not a sampling-cost estimate.

## Fixed-margin party cost and rounding

For $`\nu>1`$ and a fixed target $`R>1`$, define

```math
N_R=\min\{N\ge2:\mathcal R_N\ge R\}.
```

The upper bound in the theorem is necessary for any state and full-correlation functional; the explicit GHZ construction gives the sufficient bound. Hence

```math
\left\lceil1+\frac{\log(R/r)}{\log\nu}\right\rceil
\le N_R
\le\max\left\{2,\left\lceil\frac{\log(2R)}{\log\nu}\right\rceil\right\}.
```

For the strict target $`>R`$, the sufficient party count is

```math
\max\left\{2,\left\lfloor\frac{\log(2R)}{\log\nu}\right\rfloor+1\right\}.
```

These statements do not assume that the exact optimum is monotone in $`N`$. The necessary condition holds for every candidate $`N`$, and the sufficient condition constructs a witness at the displayed $`N`$.

Since $`r\le1`$, putting $`\nu=1+\epsilon`$ yields, for a fixed $`R>1`$ and sufficiently small positive $`\epsilon`$,

```math
1+\frac{\log R}{\log(1+\epsilon)}
\le N_R
\le\frac{\log(2R)}{\log(1+\epsilon)}+1.
```

Thus $`N_R=\Theta(1/\epsilon)`$ uniformly even when the family varies as $`\epsilon`$ tends to zero. The estimate specifies the scaling order for a target fixed above one; its constants are the displayed bounds.

## Global white-state noise is a different parameter

Let $`0\le w\le1`$ be the visibility in

```math
\rho_w=w|\mathrm{GHZ}_{N,\varphi}\rangle\langle\mathrm{GHZ}_{N,\varphi}|
+(1-w)\frac{I}{2^N}.
```

Every full-correlation Bell operator here is traceless. Its expectation on this state is $`w`$ times the pure-state expectation. Combining this state noise with uniform local attenuation multiplies a specified witness value by $`w\eta^N`$, not by $`w^N\eta^N`$.

For fixed positive $`w`$, the construction reaches at least $`R`$ whenever

```math
w(\eta\nu)^N\ge2R.
```

A constant global white-state visibility leaves the witness's exponential factor unchanged, while fixed local attenuation changes it to $`\eta\nu`$. A visibility that itself decays with $`N`$ need not preserve the rate.

The [verification policy](../VERIFICATION.md#interpreting-the-archived-rational-witness) explains the archived rational witness reports.

The [proof analysis](CONTRIBUTION_REVIEW.md) explains the analytical dependencies. The [model specification](MODEL_AND_CLAIMS.md) gives the full assumptions.
