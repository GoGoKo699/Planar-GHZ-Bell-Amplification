"""Repository safety tests, separately counted from the 18 scientific groups."""
from pathlib import Path
import hashlib
import importlib.util
import json
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
            source = '# Theorem\n\n$$\nK=\\operatorname{conv}\\{a\\}\n$$\n'
            (root/'research/THEOREM.md').write_text(source)
            view = root/'docs/THEOREM.md'
            view.write_text(renderer.theorem_view(root))
            renderer.check(root)
            readme = root/'README.md'
            readme.write_text('```math\nK=\\operatorname{conv}\\{a\\}\n```\n')
            with self.assertRaisesRegex(ValueError, 'Unsupported math macro'):
                renderer.check(root)
            readme.write_text('```math\nK=\\mathrm{conv}\\{a\\}\n```\n')
            renderer.check(root)
            view.write_text(view.read_text().replace('K=', 'Q='))
            with self.assertRaisesRegex(ValueError, 'reading view is stale'):
                renderer.check(root)
            self.assertEqual((root/'research/THEOREM.md').read_text(), source)


if __name__ == '__main__':
    unittest.main(verbosity=2)
