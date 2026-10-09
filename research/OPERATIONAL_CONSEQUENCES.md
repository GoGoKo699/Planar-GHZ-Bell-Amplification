# Operational consequences

These consequences follow from [THEOREM](../docs/THEOREM.md) for the same fixed, finite, unbiased binary coplanar qubit family. Bell-value bounds use its full-correlation objective.

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

## Finite-party convergence of Bell-locality visibility

Fix an incompatible family from above, so $`\nu>1`$ and $`\eta_{\rm JM}=1/\nu`$, and let $`N\ge2`$. Every site uses the same prescribed measurements with uniform local attenuation:

```math
M^{(\eta)}_{s|x}=\frac{I+s\eta A_x}{2}
=\eta M_{s|x}+(1-\eta)\frac I2,
\qquad 0\le\eta\le1.
```

For an $`N`$-qubit state $`\rho`$, the complete behavior is

```math
p_{\rho,\eta}(\mathbf s|\mathbf x)
=\mathrm{tr}\!\left[\rho\bigotimes_{j=1}^N M^{(\eta)}_{s_j|x_j}\right].
```

Define two thresholds, keeping the family, settings and party number fixed:

- $`\eta_N^{\mathrm{Bell}}`$ is the supremum of $`\eta\in[0,1]`$ for which $`p_{\rho,\eta}`$ is Bell local for **every** $`N`$-qubit state. This tests arbitrary Bell inequalities, including marginal terms.
- $`\eta_N^{\mathrm{fc}}`$ is the supremum of $`\eta\in[0,1]`$ for which **no** $`N`$-qubit state violates any full-correlation Bell inequality. It tests locality of the full-correlation tensor alone.

Reducing a positive $`\eta`$ to $`\eta'\le\eta`$ is independent local output processing: keep an outcome with probability $`\eta'/\eta`$, otherwise replace it by a fair random sign. At zero visibility all outputs are uniform. Locality is preserved in both cases, so the admissible visibilities form intervals starting at zero. The finite-setting local polytopes are closed, and the probabilities depend continuously on visibility; intersecting over all states includes each threshold endpoint. Complete-behavior locality implies full-correlation locality, hence $`\eta_N^{\mathrm{Bell}}\le\eta_N^{\mathrm{fc}}`$.

**Complete behavior.** For every $`N\ge2`$,

```math
\frac1\nu\le\eta_N^{\mathrm{Bell}}
\le\min\left\{1,\frac{2^{1/N}}\nu\right\}.
```

At $`\eta\le1/\nu`$, joint parents give locality for every state. At $`\eta>2^{1/N}/\nu`$, the explicit GHZ construction in [theorem Eq. (2)](../docs/THEOREM.md#2-the-theorem), together with exact attenuation, gives a normalized full-correlation value at least $`(\eta\nu)^N/2>1`$. This also witnesses nonlocality of the complete behavior. Equality of that lower bound to one does not establish violation. If $`2^{1/N}/\nu\ge1`$, the upper bound is the physical endpoint one. Consequently,

```math
0\le\frac{\eta_N^{\mathrm{Bell}}}{\eta_{\rm JM}}-1
\le 2^{1/N}-1
=\frac{\ln2}{N}+O(N^{-2}).
```

This is an explicit relative $`O(1/N)`$ upper bound on the gap, rather than an exact finite-party threshold or asymptotic coefficient. The complete-behavior convergence is due to Plávala–Gühne–Quintino, Definition 5 and Corollary 6; the [source comparison](../literature/SOURCE_AUDIT.md#visibility-threshold-comparison) matches the conventions.

**Full correlations.** The theorem's $`\mathcal R_N(A)`$ optimizes over all states and nonzero real full-correlation functionals, using the exact local absolute bound without flooring the ratio at one. The full-correlation local polytope is centrally symmetric: flipping every output at one site negates its tensor. Thus its supporting inequalities are precisely those absolute local bounds. All states satisfy them exactly when $`\eta^N\mathcal R_N(A)\le1`$, by the attenuation identity above. Since $`\mathcal R_N(A)>0`$,

```math
\eta_N^{\mathrm{fc}}
=\min\left\{1,\mathcal R_N(A)^{-1/N}\right\}.
```

Taking reciprocal Nth roots in theorem Eq. (2) reverses the inequalities and gives

```math
\min\left\{1,\frac{(\nu/r)^{1/N}}\nu\right\}
\le\eta_N^{\mathrm{fc}}
\le\min\left\{1,\frac{2^{1/N}}\nu\right\}.
```

For each **fixed** incompatible family, sufficiently large $`N`$ makes both clipped expressions smaller than one. Then

```math
\frac{(\nu/r)^{1/N}-1}{\nu}
\le\eta_N^{\mathrm{fc}}-\eta_{\rm JM}
\le\frac{2^{1/N}-1}{\nu}.
```

Because $`\nu>1`$ and $`0<r\le1`$, the constant $`\ln(\nu/r)`$ is positive. Expanding the exponentials proves $`\eta_N^{\mathrm{fc}}-\eta_{\rm JM}=\Theta(1/N)`$ for that fixed family; the bounds do not determine the exact leading coefficient. This quantifier keeps the family independent of $`N`$.

The positive lower gap applies only to full correlations. Attenuation scales a $`k`$-party marginal correlator by $`\eta^k`$, so an arbitrary Bell expression with marginal terms need not scale by $`\eta^N`$ and may detect nonlocality earlier. Complete behavior has the $`O(1/N)`$ upper gap above; full correlations have the fixed-family $`\Theta(1/N)`$ gap.

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
