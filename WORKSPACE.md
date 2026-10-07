# Repository maintenance

The canonical repository is **GoGoKo699/Planar-GHZ-Bell-Amplification**. [AGENTS.md](AGENTS.md) contains the editing and verification instructions. Start from live main and inspect open pull requests before editing; the repository history already includes the original import.

## Authority and evidence

| Record | Role |
|---|---|
| [Preserved theorem](research/THEOREM.md) and [model](research/MODEL_AND_CLAIMS.md) | Define the scientific claim and resources. |
| [Theorem reading view](docs/THEOREM.md) | Generated presentation of the preserved theorem, with historical workflow notices omitted. |
| [Attribution](literature/ATTRIBUTION.md), [source comparison](literature/SOURCE_AUDIT.md) and [proof review](research/CONTRIBUTION_REVIEW.md) | Identify inherited inputs, inspected source boundaries and proof obligations. |
| [Verification policy](VERIFICATION.md) | Defines protected files, numerical comparison and exact-revision review. |
| [Import record](provenance/IMPORT.json), [archive](archive/README.md) and [historical assessment](research/ASSESSMENT.md) | Preserve the supplied evidence and its original context. |

The [reading guide](docs/README.md) maps the reader-facing material. Maintenance instructions and historical assessments are not tutorial prerequisites.

## Reproduction and review

Use a feature branch and a fresh verification output directory. Review the exact diff, protected hashes, downloaded PR-head reports and their source hashes before merging the expected head. Inspect the separate merged-main artifact afterward. Pull requests retain revision-specific receipts; the repository's reading pages describe the result rather than an editing timeline.

Keep the 81-file snapshot and protected theorem/assessment unchanged. Regenerate the theorem reading view with `python tools/render_docs.py`. Do not repeat completed source audits without a concrete proof objection, a directly covering source or a requested new claim.
