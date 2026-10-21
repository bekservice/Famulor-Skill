"""Behavioral packaging checks: portability, reproducibility and isolation."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile
import io

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('package_release', ROOT / 'scripts/package-release.py')
package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package)


class ReleaseTests(unittest.TestCase):
    def test_archive_is_reproducible_and_exact(self):
        first = package.archive_bytes()
        self.assertEqual(first, package.archive_bytes())
        expected = {'famulor-skill/' + p.relative_to(package.SKILL).as_posix(): p.read_bytes() for p in package.skill_files()}
        with zipfile.ZipFile(io.BytesIO(first)) as archive:
            self.assertEqual(set(expected), set(archive.namelist()))
            for name, content in expected.items():
                self.assertEqual(archive.read(name), content)
                self.assertFalse(name.startswith('/') or '..' in Path(name).parts)
            self.assertIn('famulor-skill/SKILL.md', archive.namelist())
            self.assertNotIn('README.md', archive.namelist())
            self.assertFalse(any('claude-store' in n or '.git/' in n for n in archive.namelist()))

    def test_release_rejects_local_and_unexpected_files(self):
        previous = package.SKILL
        for filename in ('.env', '.private/customer.md', 'customers.csv', 'debug.log'):
            with self.subTest(filename=filename), tempfile.TemporaryDirectory() as tmp:
                package.SKILL = Path(tmp)
                try:
                    path = package.SKILL / filename
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text('Must not enter public release')
                    with self.assertRaises(ValueError):
                        package.archive_bytes()
                finally:
                    package.SKILL = previous

    def test_release_rejects_symlinks(self):
        previous = package.SKILL
        with tempfile.TemporaryDirectory() as tmp:
            package.SKILL = Path(tmp)
            try:
                (package.SKILL / 'external').symlink_to(ROOT / 'README.md')
                with self.assertRaises(ValueError):
                    package.archive_bytes()
            finally:
                package.SKILL = previous


if __name__ == '__main__':
    unittest.main()
