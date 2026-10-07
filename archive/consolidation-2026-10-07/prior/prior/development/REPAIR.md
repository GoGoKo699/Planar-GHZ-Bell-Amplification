# Optimizer reformulation, not a scientific correction

The initial five-group run passed groups 2–5 and failed group 1. SLSQP reported a positive-directional-derivative termination while solving the same compatibility dual using squared-norm inequalities. Its iterate was near the expected objective, but the required success flag was false. This was not treated as a successful optimization.

Diagnostics retained in this directory tried the equivalent dual with fewer duplicate constraints and then the norm formulation. The final checker uses `1 - norm(sum_x s_x h_x) >= 0` and its analytical Jacobian, retaining one representative from each exactly duplicate sign/opposite-sign pair. The original checker used `1 - norm(...)**2 >= 0`. The feasible sets are identical.

The optimization ftol remains 1e-12, the maximum iteration count remains 500, the objective agreement threshold remains 2e-8, and the full original squared-feasibility bound remains -2e-8. Successful termination is still required. No old report, physical measurement, theorem, Bell coefficient, or scientific tolerance was changed. The post-solve checks still enumerate the full original sign set.

All final five groups passed on two complete runs with byte-identical reports. The original preceding five-group suite also reproduced exactly. The general result is proved analytically and does not depend on accepting any finite optimizer's claim of global optimality.
