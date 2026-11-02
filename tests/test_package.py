"""Check that the public skill and ChatGPT upload remain self-contained."""

import importlib.util
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("build_chatgpt", ROOT / "scripts/build_chatgpt.py")
BUILDER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILDER)


class PackageTests(unittest.TestCase):
    def test_all_skill_documents_are_bundled(self):
        documents = {path.relative_to(BUILDER.SKILL).as_posix()
                     for path in BUILDER.SKILL.rglob("*.md")} | {"LICENSE"}
        self.assertEqual(documents, set(BUILDER.PARTS))
        self.assertEqual(len(documents), len(BUILDER.PARTS))

    def test_relative_links_resolve_without_private_dependencies(self):
        documents = list(ROOT.glob("*.md")) + list((ROOT / "chatgpt").glob("*.md"))
        documents += list((ROOT / "docs").rglob("*.md")) + list(BUILDER.SKILL.rglob("*.md"))
        for document in documents:
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", document.read_text(encoding="utf-8")):
                url = urlsplit(target)
                if url.scheme or url.netloc or not url.path:
                    continue
                with self.subTest(document=str(document.relative_to(ROOT)), target=target):
                    resolved = (document.parent / unquote(url.path)).resolve()
                    boundary = BUILDER.SKILL if document.is_relative_to(BUILDER.SKILL) else ROOT
                    self.assertTrue(resolved.is_relative_to(boundary), "link escapes the package")
                    self.assertTrue(resolved.exists(), "link target is missing")


if __name__ == "__main__":
    unittest.main()
