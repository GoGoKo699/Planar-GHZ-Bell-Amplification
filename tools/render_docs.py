#!/usr/bin/env python3
"""Generate and check the portable reading view of the protected theorem."""
from __future__ import annotations
import argparse
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MATH = re.compile(r'^```math\n(.*?)^```\s*$|^\$\$\s*\n(.*?)^\$\$\s*$', re.M | re.S)
INLINE_MATH = re.compile(r'\$`([^`\n]+)`\$')
CODE_FENCE = re.compile(r'^```[^\n]*\n.*?^```\s*$', re.M | re.S)
FENCE_LINE = re.compile(r'^[ ]{0,3}(`{3,}|~{3,})(.*)$')
READER_PATHS = (
    'README.md', 'REVIEW.md', 'VERIFICATION.md', 'docs/THEOREM.md', 'docs/README.md',
    'research/MODEL_AND_CLAIMS.md', 'research/OPERATIONAL_CONSEQUENCES.md',
    'research/CONTRIBUTION_REVIEW.md', 'literature/SOURCE_AUDIT.md',
    'literature/ATTRIBUTION.md',
)
# Inline text labels avoid the renderer's unsupported numbered-equation table.
PORTABLE_TAGS = {
    r'\tag{1}': r'\qquad\text{(1)}',
    r'\tag{2}': r'\qquad\text{(2)}',
    r'\tag{3}': r'\qquad\text{(3)}',
    r'\tag{4}': r'\qquad\text{(4)}',
    r'\tag{5}': r'\qquad\text{(5)}',
    r'\tag{6}': r'\qquad\text{(6)}',
    r'\tag{7}': r'\qquad\text{(7)}',
}

THEOREM_TITLE = '# Optimal exponential Bell amplification from planar qubit measurements'
# These exact editorial changes apply only to the protected theorem's reading
# copy. Every anchor must occur once: source drift requires an explicit review.
# Equations and the bibliography stay unchanged; scope prose stays tied to the model.
THEOREM_READER_EDITS = (
    ('**7 October 2026. Consolidated author-side theorem.** ', ''),
    ('This is one bounded contribution: converting', 'The theorem converts'),
    (' No new compatibility theorem, experimental performance, or exhaustive priority certificate is claimed.', ''),
    (
        'This account replaces the exploration sequence as the main reading path. '
        'Earlier notes and checks remain unchanged in the '
        '[protected import](../archive/consolidation-2026-10-07/README.md). '
        'The only strengthened bound in this pass is the finite-party upper bound '
        'in (2), using the standard fact that compatibility at all but one site '
        'suffices for locality. The asymptotic exponent and all earlier examples '
        'remain valid.',
        'The finite-party upper bound in (2) uses the standard fact that '
        'compatibility at all but one site suffices for locality.',
    ),
    (
        '## 6. A fixed violation margin and the retained exact example',
        '## 6. A fixed violation margin and an exact example',
    ),
    ('Keep the existing irregular rational family', 'Consider the irregular rational family'),
    (
        'The old 13-party and 25-party exact certificates remain unchanged.',
        'The 13-party and 25-party values have exact certificates.',
    ),
    ('The strengthened upper bound now certifies', 'The upper bound certifies'),
    ('The existing construction gives', 'The explicit construction gives'),
    ('The prior exact coefficient vector certifies', 'The rational coefficient vector certifies'),
    (' These numbers illustrate the sharpened converse, not a second physical result.', ''),
    ('The proposed additional implication is:', 'The additional implication is:'),
    (
        '## 8. Attribution, significance, and stopping boundary',
        '## 8. Attribution and scope',
    ),
    (
        ' Its proof is concise; the remaining judgment is whether the connection '
        'is sufficiently consequential, not whether its ingredients are unfamiliar.',
        '',
    ),
    (' No exhaustive priority or independent scientific review has occurred.', ''),
    ('Stop expanding the scientific scope for the current assessment. ', ''),
    (
        'Biased or noncoplanar measurements, detector no-click models, exact finite-N '
        'Bell optima, genuine multipartite nonlocality, self-testing, cryptographic '
        'rates and efficient statistical certification are not claimed and are '
        'not automatic prerequisites.',
        'The result concerns full-correlation Bell values for the fixed unbiased '
        'binary coplanar measurements defined in Section 1. It determines their '
        'optimal exponential rate, with finite-party values bounded as in (2).',
    ),
    (' The theorem is recorded here for focused author review.', ''),
    (' This initialization does not initiate a manuscript submission, release or external contact.', ''),
)

# Presentation substitutions in the protected theorem's prose only. Longest
# matches take precedence, and one substitution pass cannot change its own TeX.
THEOREM_NOTATION = {
    'R_N=R_N^GHZ=r^N': r'\mathcal R_N=\mathcal R_N^{\mathrm{GHZ}}=r^N',
    'R_N^GHZ': r'\mathcal R_N^{\mathrm{GHZ}}',
    'R_N': r'\mathcal R_N',
    'L(beta)>0': r'L(\beta)>0',
    'L(beta)<=1': r'L(\beta)\le1',
    'nu=r=0': r'\nu=r=0',
    'r<=nu<=pi r/2': r'r\le\nu\le\pi r/2',
    'nu<=1': r'\nu\le1',
    'nu>0': r'\nu>0',
    'nu>1': r'\nu>1',
    'nu=r': r'\nu=r',
    'N>=2': r'N\ge2',
    '2r/nu<=2': r'2r/\nu\le2',
    'a_1,...,a_m': r'\mathbf a_1,\ldots,\mathbf a_m',
    'a_{m+1}=-a_1': r'\mathbf a_{m+1}=-\mathbf a_1',
    'Y=(1/2) Khat C^T': r'Y=\tfrac12\widehat K C^T',
    'z_x=a_{x1}+i a_{x2}': r'z_x=a_{x1}+i a_{x2}',
    'c_x=h_{x1}+i h_{x2}': r'c_x=h_{x1}+i h_{x2}',
    'a_j=r d': r'\mathbf a_j=r\mathbf d',
    'h_j=d': r'h_j=\mathbf d',
    'u=r': r'u=r',
    '|v|=r': r'|v|=r',
    'gamma=-N arg(v)/2': r'\gamma=-N\arg(v)/2',
    'phi=-arg(b_N)': r'\varphi=-\arg(b_N)',
    '|b_N|': r'|b_N|',
    'v=0': r'v=0',
    'gamma=phi=0': r'\gamma=\varphi=0',
    't=|v|/nu': r't=|v|/\nu',
    '[0,1]': r'[0,1]',
    '(1-t^k)(1-t^{N-k})>=0': r'(1-t^k)(1-t^{N-k})\ge0',
    'N-1': r'N-1',
    'A_x/nu': r'A_x/\nu',
    'A_x/r': r'A_x/r',
    'r nu^{N-1}': r'r\nu^{N-1}',
    'nu^N>2R': r'\nu^N>2R',
    'nu^N': r'\nu^N',
    'r^N': r'r^N',
    'R>1': r'R>1',
    '(nu-1)': r'(\nu-1)',
    '(|b>+e^{i phi}|bar b>)/sqrt(2)': r'\frac{|b\rangle+e^{i\varphi}|\bar b\rangle}{\sqrt2}',
    'A_1=X,A_2=Y': r'A_1=X,\ A_2=Y',
    '2 sqrt(2)': r'2\sqrt2',
    'span{|01>,|10>}': r'\mathrm{span}\{|01\rangle,|10\rangle\}',
    'k_i': r'k_i',
    'k': r'k',
    '+1': r'+1',
    'h': r'h',
    'v': r'v',
    'beta': r'\beta',
    'phi': r'\varphi',
    'nu': r'\nu',
    'lambda': r'\lambda',
    'r': r'r',
    'N': r'N',
    'R': r'R',
}
THEOREM_TOKENS = re.compile(
    r'(?<![\w\\])(?:' + '|'.join(
        re.escape(key) for key in sorted(THEOREM_NOTATION, key=len, reverse=True)
    ) + r')(?!\w)'
)

# Deliberately limited to mathematical spellings found in the reading route;
# paths, commands, source identifiers and words such as "beta" are not TeX.
ASCII_MATH = re.compile(
    r'\b(?:R_N(?:\^GHZ)?|A_x|[czh]_x|k_i|b_N|Q_N|L\(beta\)|'
    r'nu(?=\s*(?:[<>=^]|r\b))|eta(?=\s*(?:[<>=^]|nu\b))|'
    r'N(?=\s*(?:[<>=]|[-−]\d\b))|r(?=\s*(?:[<>=^]|nu\b)))'
)
CODE_MATH = re.compile(
    r'^(?:nu|eta|beta|phi|gamma|lambda|R_N(?:\^GHZ)?|A_x|h_x|k_i|'
    r'z_x|c_x|Q_N|L\(beta\)|r|N|R|v|T|K)\b'
)


def inline_prose(line: str) -> str:
    parts = re.split(r'(`[^`\n]+`|\[[^\]]+\]\([^)]+\))', line)
    for index in range(0, len(parts), 2):
        parts[index] = THEOREM_TOKENS.sub(
            lambda match: '$`' + THEOREM_NOTATION[match.group()] + '`$', parts[index]
        )
    return ''.join(parts)


def theorem_reader_prose(text: str) -> str:
    """Remove exact author-workflow prose from the known protected theorem."""
    if not text.startswith(THEOREM_TITLE+'\n'):
        raise ValueError('Theorem reading-copy title anchor has changed')
    for old, _ in THEOREM_READER_EDITS:
        if text.count(old) != 1:
            raise ValueError(f'Theorem reading-copy editorial anchor has changed: {old}')
    for old, new in THEOREM_READER_EDITS:
        text = text.replace(old, new, 1)
    return text


def theorem_view(root: Path = ROOT) -> str:
    text = (root/'research/THEOREM.md').read_text()
    if root.resolve() == ROOT.resolve() or text.startswith(THEOREM_TITLE+'\n'):
        text = theorem_reader_prose(text)
    text = text.replace(r'\operatorname{', r'\mathrm{')
    for old, new in PORTABLE_TAGS.items():
        text = text.replace(old, new)
    opened = False
    references = False
    lines = []
    for line in text.splitlines():
        if line == '$$':
            lines.append('```' if opened else '```math')
            opened = not opened
        else:
            if line == '## Primary references':
                references = True
            if not opened and not references and not line.startswith('#'):
                line = inline_prose(line)
            lines.append(line)
    if opened:
        raise ValueError('Unclosed display math in protected source')
    return '\n'.join(lines).rstrip() + '\n\n' + (
        'The preserved [scientific source](../research/THEOREM.md) defines this theorem.\n')


def fenced_math(text: str, relative: str) -> list[str]:
    """Collect raw math bodies while allowing literal examples in other fences."""
    blocks = []
    fence = None
    body = []
    for line in text.splitlines(keepends=True):
        match = FENCE_LINE.match(line.rstrip('\r\n'))
        if fence is not None:
            marker, is_math = fence
            if (
                match and match[1][0] == marker[0] and len(match[1]) >= len(marker)
                and not match[2].strip()
            ):
                if is_math:
                    blocks.append(''.join(body))
                fence = None
                body = []
            elif is_math:
                if '$$' in line or match:
                    raise ValueError(f'Mixed display math delimiters in {relative}')
                body.append(line)
            continue
        if match:
            info = match[2].strip()
            if info.split(maxsplit=1)[:1] == ['math'] and info != 'math':
                raise ValueError(f'Unsupported math fence info in {relative}')
            fence = (match[1], info == 'math')
        elif '$$' in line:
            raise ValueError(f'Display math must use a math fence in {relative}')
    if fence is not None and fence[1]:
        raise ValueError(f'Unclosed math fence in {relative}')
    return blocks


def check(root: Path = ROOT) -> dict:
    if (root/'docs/THEOREM.md').read_text() != theorem_view(root):
        raise ValueError('The theorem reading view is stale; run python tools/render_docs.py')
    paths = list(root.glob('*.md')) + list((root/'research').glob('*.md'))
    paths += list((root/'literature').glob('*.md')) + list((root/'docs').rglob('*.md'))
    protected = {root/'research/THEOREM.md', root/'research/ASSESSMENT.md'}
    blocks = 0
    inline = 0
    for path in paths:
        if path in protected:
            continue
        for formula in fenced_math(path.read_text(), str(path.relative_to(root))):
            blocks += 1
            if any(macro in formula for macro in (r'\operatorname', r'\tag')):
                raise ValueError(f'Unsupported math macro in {path.relative_to(root)}')
    for relative in READER_PATHS:
        path = root/relative
        if not path.is_file():
            continue
        prose = CODE_FENCE.sub('', MATH.sub('', path.read_text()))
        for match in INLINE_MATH.finditer(prose):
            inline += 1
            if any(macro in match.group() for macro in (r'\operatorname', r'\tag')):
                raise ValueError(f'Unsupported math macro in {relative}')
        prose = INLINE_MATH.sub('', prose)
        if '$`' in prose or '`$' in prose:
            raise ValueError(f'Unclosed inline math in {relative}')
        for match in re.finditer(r'`([^`\n]+)`', prose):
            if CODE_MATH.search(match[1]) or ASCII_MATH.search(match[1]):
                raise ValueError(f'Mathematical expression left as code in {relative}: {match[1]}')
        prose = re.sub(r'`[^`\n]+`', '', prose)
        prose = re.sub(r'\]\([^)]*\)', ']', prose)
        if match := ASCII_MATH.search(prose):
            raise ValueError(f'ASCII mathematical expression in {relative}: {match.group()}')
    return {
        'theorem_view_matches_source': True,
        'math_blocks_checked': blocks,
        'inline_math_checked': inline,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check without rewriting files')
    args = parser.parse_args()
    if not args.check:
        (ROOT/'docs/THEOREM.md').write_text(theorem_view())
    print(check())
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
