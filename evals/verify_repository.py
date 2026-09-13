"""Maintainer checks, using only Python's standard library.

Run from any directory. On Windows, also exercise the setup script in isolated
fixtures. These checks do not evaluate an AI's research output or run Lean.
"""

import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
CORE = ['AGENTS.md', 'ECONOMETRICA_ORCHESTRATOR.md',
        'ECONOMETRICA_DISCOVERY_WORKFLOW.md', 'ECONOMETRICA_VERIFICATION_WORKFLOW.md',
        'ECONOMETRICA_AI_HUMAN_WORKFLOW.md', 'ECONOMETRICA_PANEL_PROTOCOL.md',
        'ECONOMETRICA_VERSION_CONTROL.md']


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class RepositoryChecks(unittest.TestCase):
    def test_core_revisions_and_relative_links(self):
        for name in CORE:
            self.assertIn('Workflow revision: 2026-09', (ROOT / name).read_text(encoding='utf-8').splitlines())
        # Check the maintained docs' inline file links, not arbitrary paper files.
        # Anchor validity, reference-style links and remote availability are outside scope.
        sources = [ROOT / name for name in CORE + ['README.md', 'FIRST_RUN.md',
                   'INSTALL.md', 'TOOLCHAIN_README.md', 'CONTRIBUTING.md']]
        sources += [path for folder in ('docs', 'examples', 'evals') for path in (ROOT / folder).glob('*.md')]
        for source in sources:
            content = source.read_text(encoding='utf-8')
            content = re.sub(r'```.*?```', '', content, flags=re.S)
            for target in re.findall(r'\]\((<[^>]+>|[^)\s]+)(?:\s+"[^"]*")?\)', content):
                target = target.strip('<>')
                if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                    continue
                target = unquote(target.split('#', 1)[0])
                self.assertTrue((source.parent / target).exists(), f'{source.relative_to(ROOT)} -> {target}')

    def test_main_really_checks_boundaries_and_sample(self):
        search = load_module('search_template', ROOT / 'verification_templates/counterexample_search.py')
        seen = []
        with patch.object(search, 'claim_holds', side_effect=lambda p: seen.append(p) or True), patch('builtins.print'):
            search.main()
        self.assertEqual(len(seen), 10020)
        self.assertIn(search.Params(0.0, 1.0), seen)
        self.assertIn(search.Params(10.0, 1.0), seen)
        # A boundary-only failure that continuous random draws generally miss.
        failures = search.find_counterexamples(lambda p: p.beta < 1, search.boundary_cases())
        self.assertEqual({p.alpha for p in failures}, {0.0, 1e-9, 1.0, 10.0})
        boundaries = [search.Params(0, 0), search.Params(0, 1)]
        sample = [search.Params(1, 0.37), search.Params(2, 0.69)]
        seen.clear()
        with patch.object(search, 'boundary_cases', return_value=iter(boundaries)), \
             patch.object(search, 'sample_params', return_value=iter(sample)), \
             patch.object(search, 'claim_holds', side_effect=lambda p: seen.append(p) or True), \
             patch('builtins.print'):
            search.main()
        self.assertEqual(seen, boundaries + sample)

    def test_search_limit_and_seed(self):
        search = load_module('search_template', ROOT / 'verification_templates/counterexample_search.py')
        sample = list(search.sample_params(20, 9))
        self.assertEqual(sample, list(search.sample_params(20, 9)))
        self.assertEqual(len(sample), 20)
        self.assertTrue(all(0 <= p.alpha <= 10 and 0 <= p.beta <= 1 for p in sample))
        failures = search.find_counterexamples(lambda p: False, search.boundary_cases(), limit=2)
        self.assertEqual(len(failures), 2)
        for limit in (0, -1):
            with self.assertRaises(ValueError):
                search.find_counterexamples(lambda p: False, search.boundary_cases(), limit=limit)


@unittest.skipUnless(os.name == 'nt', 'PowerShell setup scenarios require Windows')
class SetupChecks(unittest.TestCase):
    shell = None

    def setUp(self):
        if not self.shell:
            self.skipTest('No PowerShell executable found')
        self.temp = tempfile.TemporaryDirectory(prefix='econ-workflow-test-')
        self.folder = Path(self.temp.name).resolve()
        # Only this newly created fixture directory may be recursively cleaned.
        assert self.folder.parent == Path(tempfile.gettempdir()).resolve()
        self.addCleanup(self.temp.cleanup)
        for name in [*CORE, 'verify_toolchain.ps1']:
            shutil.copyfile(ROOT / name, self.folder / name)
        self.config = self.folder / 'config.json'
        self.settings = {name: str(self.folder / f'absent-{name}.exe') for name in
                         ['gitPath', 'latexPath', 'pythonPath', 'leanPath', 'lakePath', 'wolframScriptPath']}
        self.save_config()

    def save_config(self):
        self.config.write_text(json.dumps(self.settings), encoding='utf-8')

    def run_setup(self, *args):
        return subprocess.run([self.shell, '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File',
                               str(self.folder / 'verify_toolchain.ps1'), '-ConfigPath', str(self.config), *args],
                              cwd=ROOT, capture_output=True, text=True, errors='replace', timeout=30)

    def test_optional_tools_absent_and_local_status(self):
        run = self.run_setup()
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertIn('Present, revision 2026-09', run.stdout)
        self.assertEqual(run.stdout.count('Configured path missing'), 6)
        self.assertFalse((self.folder / 'toolchain_status.md').exists())
        run = self.run_setup('-WriteStatus')
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertIn('not theorem or paper correctness', (self.folder / 'toolchain_status.md').read_text(encoding='utf-8-sig'))
        selected = self.folder / 'chosen.md'
        run = self.run_setup('-WriteStatus', '-StatusPath', str(selected))
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertTrue(selected.exists())

    def test_missing_or_mixed_protocol_fails(self):
        target = self.folder / 'ECONOMETRICA_VERIFICATION_WORKFLOW.md'
        target.unlink()
        run = self.run_setup()
        self.assertNotEqual(run.returncode, 0)
        self.assertIn(target.name, run.stdout)
        target.write_text('# old protocol\n', encoding='utf-8')
        run = self.run_setup()
        self.assertNotEqual(run.returncode, 0)
        self.assertIn('wrong revision: ' + target.name, run.stdout)

    def test_bad_or_explicitly_missing_config_fails(self):
        for content in ['{broken', '[]', '[{}]', 'null']:
            self.config.write_text(content, encoding='utf-8')
            self.assertNotEqual(self.run_setup().returncode, 0)
        self.config.unlink()
        self.assertNotEqual(self.run_setup().returncode, 0)

    def test_actual_python_package_discovery(self):
        self.settings['pythonPath'] = sys.executable
        self.save_config()
        run = self.run_setup()
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertIn('Python: Version check passed', run.stdout)
        self.assertRegex(run.stdout, r'Optional Python packages: sympy:(found|missing)')

    def test_wolfram_smoke_test_is_opt_in_and_exact(self):
        # A fixture command, not a Wolfram installation or scientific calculation.
        fake = self.folder / 'fake-wolfram.cmd'
        marker = self.folder / 'was-launched.txt'
        self.settings['wolframScriptPath'] = str(fake)
        self.save_config()
        def command(value):
            fake.write_text('@echo off\r\n'
                            'if not "%~1"=="-code" exit /b 9\r\n'
                            'if not "%~2"=="Print[2+2]" exit /b 10\r\n'
                            'echo called>"%~dp0was-launched.txt"\r\n'
                            f'echo {value}\r\nexit /b 0\r\n', encoding='ascii')
        command('40')
        run = self.run_setup()
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertFalse(marker.exists())
        run = self.run_setup('-RunSmokeTests')
        self.assertTrue(marker.exists())
        self.assertIn('Wolfram arithmetic smoke test: Failed', run.stdout)
        command('4')
        run = self.run_setup('-RunSmokeTests')
        self.assertIn('Wolfram arithmetic smoke test: Passed (2+2 only)', run.stdout)

    def test_lean_and_lake_discovery_does_not_launch_shims(self):
        fake = self.folder / 'fake-lean.cmd'
        marker = self.folder / 'lean-launched.txt'
        fake.write_text('@echo off\r\necho called>"%~dp0lean-launched.txt"\r\nexit /b 0\r\n', encoding='ascii')
        self.settings.update(leanPath=str(fake), lakePath=str(fake))
        self.save_config()
        run = self.run_setup()
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertFalse(marker.exists())
        self.assertIn('Lean: Executable found; execution not checked', run.stdout)
        self.assertIn('Lake: Executable found; execution not checked', run.stdout)


def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite(loader.loadTestsFromTestCase(RepositoryChecks))
    shells = list(dict.fromkeys(path for name in ('pwsh', 'powershell') if (path := shutil.which(name))))
    for shell in shells or [None]:
        for method in loader.getTestCaseNames(SetupChecks):
            test = SetupChecks(method)
            test.shell = shell
            suite.addTest(test)
    return suite


if __name__ == '__main__':
    unittest.main(verbosity=2)
