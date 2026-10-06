"""Validate and package the static Firefox UI theme with the standard library."""

import json
import re
from pathlib import Path
from xml.etree import ElementTree
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


def main():
    root = Path(__file__).resolve().parents[1]
    source = root / "src"
    manifest = json.loads((source / "manifest.json").read_text(encoding="utf-8"))
    if manifest.get("manifest_version") != 2 or not manifest.get("theme"):
        raise ValueError("Expected a static Firefox theme manifest")
    if any(key in manifest for key in ("permissions", "background", "content_scripts")):
        raise ValueError("The static theme must not request permissions or execute scripts")
    version = manifest["version"]
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("Expected a numeric major.minor.patch version")
    asset = (source / manifest["theme"]["images"]["theme_frame"]).resolve()
    if source.resolve() not in asset.parents or not asset.is_file():
        raise ValueError("Theme image must exist inside src/")
    ElementTree.parse(asset)
    destination = root / "dist" / f"empire-temporelle-{version}.zip"
    destination.parent.mkdir(exist_ok=True)
    with ZipFile(destination, "w") as archive:
        files = [(source / "manifest.json", "manifest.json"),
                 (asset, asset.relative_to(source).as_posix()),
                 (root / "LICENSE", "LICENSE")]
        for path, archive_name in files:
            info = ZipInfo(archive_name, (2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())
    with ZipFile(destination) as archive:
        if archive.testzip() is not None:
            raise ValueError("Archive integrity check failed")
    print(f"Validated and packaged: {destination}")


if __name__ == "__main__":
    main()
