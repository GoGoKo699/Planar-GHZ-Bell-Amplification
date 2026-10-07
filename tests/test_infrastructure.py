"""Repository safety tests, separately counted from the 18 scientific groups."""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('verify', ROOT/'tools/verify.py')
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


class InfrastructureTests(unittest.TestCase):
    def test_protected_snapshot_and_license(self):
        result = verify.inspect_archive()
        self.assertEqual(result['snapshot_members'], 81)
        self.assertTrue(result['all_hashes_match'])

    def test_active_links(self):
        self.assertGreater(verify.check_links(), 20)

    def test_nested_reading_guide_links_are_checked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root/'archive').mkdir()
            (root/'archive/README.md').write_text('Historical evidence.\n')
            (root/'llms.txt').write_text('Automated reading guide.\n')
            (root/'docs/lessons').mkdir(parents=True)
            guide = root/'docs/lessons/README.md'
            guide.write_text('[Missing proof](../../research/missing.md)\n')
            with self.assertRaisesRegex(ValueError, 'Broken local link'):
                verify.check_links(root)
            (root/'research').mkdir()
            (root/'research/missing.md').write_text('Proof.\n')
            self.assertEqual(verify.check_links(root), 1)
            (root/'llms.txt').write_text('[Missing guide](docs/missing.md)\n')
            with self.assertRaisesRegex(ValueError, 'Broken local link'):
                verify.check_links(root)

    def test_exact_discrete_and_float_difference_record(self):
        a = {'n': 3, 'status': 'PASS', 'value': 1.0, 'q': ['1/3', True]}
        b = {**a, 'value': 1.0+1e-14}
        differences = verify.compare(b, a)
        self.assertEqual(len(differences), 1)
        self.assertEqual(differences[0]['path'], '$.value')
        for changed in ({**a, 'n': 4}, {**a, 'n': 3.0}, {**a, 'status': 'FAIL'}, {**a, 'q': ['2/3', True]}):
            with self.assertRaises(ValueError):
                verify.compare(changed, a)

    def test_reject_bad_numeric_and_structure(self):
        for a,b in [(float('nan'),0.), (float('inf'),0.), (1.001,1.), ([1],[1,2]), ({'a':1},{'b':1})]:
            with self.assertRaises(ValueError):
                verify.compare(a,b)

    def test_output_refusal(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)
            with self.assertRaises(ValueError):
                verify.fresh_output(path)
            self.assertEqual(verify.fresh_output(path/'new'), path/'new')
        with self.assertRaises(ValueError):
            verify.fresh_output(ROOT/'archive/new-evidence')

    def test_exact_number_of_scientific_groups(self):
        self.assertEqual(len(verify.JOBS), 4)
        self.assertEqual(sum(job[3] for job in verify.JOBS), 18)
        for _, script, reference, count in verify.JOBS:
            archive = ROOT/'archive/consolidation-2026-10-07'
            self.assertTrue((archive/script).is_file())
            report = json.loads((archive/reference).read_text())
            self.assertEqual((report['status'],report['tests_run']), ('PASS',count))

    def test_no_redistributed_pdf_or_font(self):
        prohibited = {'.pdf','.ttf','.otf','.woff','.woff2'}
        for p in ROOT.rglob('*'):
            if p.is_file() and '.git' not in p.parts and '.artifacts' not in p.parts:
                self.assertNotIn(p.suffix.lower(), prohibited)

    def test_supported_math_and_contact(self):
        readme=(ROOT/'README.md').read_text()
        self.assertIn('```math',readme)
        self.assertIn('mailto:gogoko699@gmail.com',readme)
        self.assertIn('Purpose and contact',readme)
        self.assertIn('full-correlation',readme)
        self.assertIn('Yoshino',readme)
        self.assertIn('conv',readme)

    def test_portable_math_and_frozen_source_view(self):
        self.assertTrue(verify.check_presentation()['theorem_view_matches_source'])
        spec = importlib.util.spec_from_file_location('render_docs', ROOT/'tools/render_docs.py')
        renderer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(renderer)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root/'research').mkdir()
            (root/'docs').mkdir()
            source = '# Theorem\n\n$$\nK=\\operatorname{conv}\\{a\\}\n\\tag{1}\n$$\n'
            (root/'research/THEOREM.md').write_text(source)
            view = root/'docs/THEOREM.md'
            view.write_text(renderer.theorem_view(root))
            self.assertIn(r'\qquad\text{(1)}', view.read_text())
            self.assertNotIn(r'\tag', view.read_text())
            renderer.check(root)
            readme = root/'README.md'
            readme.write_text('```math\nK=\\operatorname{conv}\\{a\\}\n```\n')
            with self.assertRaisesRegex(ValueError, 'Unsupported math macro'):
                renderer.check(root)
            readme.write_text('```math\nK=\\mathrm{conv}\\{a\\}\n```\n')
            renderer.check(root)
            readme.write_text('```math\nK=\\mathrm{conv}\\{a\\}\n\\tag{1}\n```\n')
            with self.assertRaisesRegex(ValueError, 'Unsupported math macro'):
                renderer.check(root)
            readme.write_text('$`K=\\mathrm{conv}\\{a\\}\\tag{1}`$\n')
            with self.assertRaisesRegex(ValueError, 'Unsupported math macro'):
                renderer.check(root)
            readme.write_text('```math\nK=\\mathrm{conv}\\{a\\}\\qquad\\text{(1)}\n```\n')
            renderer.check(root)
            view.write_text(view.read_text().replace('K=', 'Q='))
            with self.assertRaisesRegex(ValueError, 'reading view is stale'):
                renderer.check(root)
            self.assertEqual((root/'research/THEOREM.md').read_text(), source)

    def test_inline_math_rendering_and_prose_regression(self):
        spec = importlib.util.spec_from_file_location('render_docs', ROOT/'tools/render_docs.py')
        renderer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(renderer)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root/'research').mkdir()
            (root/'docs').mkdir()
            source = (
                '# Finite-N theorem\n\nFor N>=2, nu<=1 and R_N^GHZ.\n\n'
                '[Source](../research/N.md)\n\n$$\nN=2\n$$\n\n'
                '## Primary references\n\n- [R] R. Author.\n'
            )
            (root/'research/THEOREM.md').write_text(source)
            view = renderer.theorem_view(root)
            (root/'docs/THEOREM.md').write_text(view)
            self.assertIn('# Finite-N theorem', view)
            self.assertIn('$`N\\ge2`$', view)
            self.assertIn('$`\\nu\\le1`$', view)
            self.assertIn('$`\\mathcal R_N^{\\mathrm{GHZ}}`$', view)
            self.assertIn('[Source](../research/N.md)', view)
            self.assertIn('```math\nN=2\n```', view)
            self.assertIn('- [R] R. Author.', view)
            self.assertEqual(renderer.check(root)['inline_math_checked'], 3)
            self.assertEqual((root/'research/THEOREM.md').read_text(), source)
            readme = root/'README.md'
            for bad, message in (
                ('`nu <= 1`', 'left as code'),
                ('`R_N`', 'left as code'),
                ('nu <= 1', 'ASCII mathematical expression'),
                ('R_N', 'ASCII mathematical expression'),
                ('$`\\nu\\le1$', 'Unclosed inline math'),
                ('$`\\operatorname{conv}\\{a\\}`$', 'Unsupported math macro'),
            ):
                with self.subTest(bad=bad):
                    readme.write_text(bad+'\n')
                    with self.assertRaisesRegex(ValueError, message):
                        renderer.check(root)
            readme.write_text('Use `python tools/verify.py` for the beta coefficients.\n')
            renderer.check(root)

    def test_fenced_math_preserves_delimiters_and_literal_examples(self):
        spec = importlib.util.spec_from_file_location('render_docs', ROOT/'tools/render_docs.py')
        renderer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(renderer)
        formula = (
            r'\max\left\{2,\left\lceil\frac{\log(2R)}{\log\nu}'
            r'\right\rceil\right\}.'+'\n'
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root/'research').mkdir()
            (root/'docs').mkdir()
            (root/'research/THEOREM.md').write_text('# Theorem\n\n$$\nx=1\n$$\n')
            (root/'docs/THEOREM.md').write_text(renderer.theorem_view(root))
            readme = root/'README.md'
            valid = '```math\n'+formula+'```\n'
            readme.write_text(valid)
            self.assertEqual(renderer.fenced_math(valid, 'README.md'), [formula])
            self.assertEqual(
                renderer.fenced_math(valid, 'README.md')[0].encode(), formula.encode(),
            )
            renderer.check(root)
            for bad, message in (
                ('$$\n'+formula+'$$\n', 'must use a math fence'),
                ('$$x=1$$\n', 'must use a math fence'),
                ('A value $$x=1$$ in prose.\n', 'must use a math fence'),
                ('```math\n'+formula, 'Unclosed math fence'),
                ('```math\n$$\n'+formula+'$$\n```\n', 'Mixed display math delimiters'),
                ('```math\n$$x=1$$\n```\n', 'Mixed display math delimiters'),
                ('```math extra\n$$\nx=1\n$$\n```\n', 'Unsupported math fence info'),
            ):
                with self.subTest(bad=bad):
                    readme.write_text(bad)
                    with self.assertRaisesRegex(ValueError, message):
                        renderer.check(root)
            for example in (
                '```text\n$$\n'+formula+'$$\n```\n',
                '```text\n$$x=1$$\n```\n',
                '````text\n```math\n$$\n'+formula+'$$\n```\n````\n',
                '~~~text\n$$\n'+formula+'$$\n~~~\n',
            ):
                with self.subTest(example=example):
                    readme.write_text(example)
                    self.assertEqual(renderer.fenced_math(example, 'README.md'), [])
                    renderer.check(root)

    def test_theorem_reader_editorial_changes_preserve_science(self):
        spec = importlib.util.spec_from_file_location('render_docs', ROOT/'tools/render_docs.py')
        renderer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(renderer)
        source_path = ROOT/'research/THEOREM.md'
        source_bytes = source_path.read_bytes()
        source = source_bytes.decode()
        view = renderer.theorem_view()
        source_math = [match[2] for match in renderer.MATH.finditer(source)]
        view_math = [match[1] for match in renderer.MATH.finditer(view)]
        self.assertEqual(len(source_math), 24)
        normalized = []
        for formula in source_math:
            formula = formula.replace(r'\operatorname{', r'\mathrm{')
            for number in range(1, 8):
                formula = formula.replace(
                    r'\tag{'+str(number)+'}', r'\qquad\text{('+str(number)+')}',
                )
            normalized.append(formula)
        self.assertEqual(normalized, view_math)
        self.assertEqual(
            [tag for formula in source_math for tag in re.findall(r'\\tag\{(\d+)\}', formula)],
            [str(number) for number in range(1, 8)],
        )
        self.assertNotIn(r'\tag', view)
        for number in range(1, 8):
            self.assertEqual(view.count(r'\qquad\text{('+str(number)+')}'), 1)
        bibliography = source.split('## Primary references\n', 1)[1].strip()
        view_bibliography = view.split('## Primary references\n', 1)[1].split(
            '\nThe preserved [scientific source]', 1,
        )[0].strip()
        self.assertEqual(view_bibliography, bibliography)
        for boundary in (
            'No new compatibility theorem, experimental performance, or exhaustive priority certificate is claimed.',
            'No communication during the trial, postselection, privileged sharper detector, filtering, or multiple sequential uses at a site is added.',
            'State and Bell-functional design use the known family and its plane; the result is not an uncalibrated device-construction procedure.',
            'This is a comparison of normalized Bell values, not their excess above one, not sample complexity, and not a statement of exact finite-N optimum.',
            'Biased or noncoplanar measurements, detector no-click models, exact finite-N Bell optima, genuine multipartite nonlocality, self-testing, cryptographic rates and efficient statistical certification are not claimed and are not automatic prerequisites.',
        ):
            self.assertIn(renderer.inline_prose(boundary), view)
        self.assertIn('The 13-party and 25-party values have exact certificates.', view)
        self.assertIn('## 8. Attribution and scope', view)
        self.assertNotIn('focused author review', view)
        self.assertNotIn('manuscript submission', view)
        for old, _ in renderer.THEOREM_READER_EDITS:
            with self.subTest(anchor=old):
                with self.assertRaisesRegex(ValueError, 'editorial anchor has changed'):
                    renderer.theorem_reader_prose(source.replace(old, 'missing anchor', 1))
                with self.assertRaisesRegex(ValueError, 'editorial anchor has changed'):
                    renderer.theorem_reader_prose(source+'\n'+old)
        with self.assertRaisesRegex(ValueError, 'title anchor has changed'):
            renderer.theorem_reader_prose(source.replace(renderer.THEOREM_TITLE, '# Changed title', 1))
        self.assertEqual(source_path.read_bytes(), source_bytes)
        self.assertEqual(
            hashlib.sha256(source_bytes).hexdigest(),
            '201515a6e33e910d86087072a9a99acc052fdb2b3d6ba3722d4719418facbda1',
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)
