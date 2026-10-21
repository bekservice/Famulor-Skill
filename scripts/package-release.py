#!/usr/bin/env python3
"""Build reproducible skill archives without dependencies or network access."""
import argparse
import hashlib
import io
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'famulor-skill'
EXCLUDED = {'.DS_Store', '__pycache__', '__MACOSX'}
ALLOWED_SUFFIXES = {'.md', '.json', '.py', '.yaml', '.yml', '.svg', '.png', '.jpg', '.jpeg', '.webp'}


def skill_files():
    for path in sorted(SKILL.rglob('*')):
        if path.is_symlink():
            raise ValueError(f'Symlinks are not allowed in a release: {path.relative_to(ROOT)}')
        if path.is_file() and not set(path.parts).intersection(EXCLUDED) and path.suffix != '.pyc':
            relative = path.relative_to(SKILL)
            if any(part.startswith('.') for part in relative.parts) or path.suffix not in ALLOWED_SUFFIXES:
                raise ValueError(f'Unexpected file in release: {relative}; review before packaging')
            yield path


def archive_bytes():
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in skill_files():
            info = zipfile.ZipInfo('famulor-skill/' + path.relative_to(SKILL).as_posix(), (2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, path.read_bytes(), compresslevel=9)
    return buffer.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verify committed famulor.skill matches source byte-for-byte')
    args = parser.parse_args()
    data = archive_bytes()
    target = ROOT / 'famulor.skill'
    if args.check:
        if not target.exists() or target.read_bytes() != data:
            parser.exit(1, 'famulor.skill differs from source. Run python3 scripts/package-release.py\n')
        print('Archive matches skill source byte-for-byte.')
        return
    target.write_bytes(data)
    dist = ROOT / 'dist'
    dist.mkdir(exist_ok=True)
    for name in ('famulor.skill', 'famulor-skill.zip'):
        (dist / name).write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    (dist / 'SHA256SUMS').write_text(''.join(f'{digest}  {name}\n' for name in ('famulor.skill', 'famulor-skill.zip')))
    print(f'Packaged {len(list(skill_files()))} files; {len(data):,} bytes; SHA-256 {digest}')


if __name__ == '__main__':
    main()
