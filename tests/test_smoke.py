"""Smoke test: proves the package imports and the toolchain runs.

Replace it with real tests as soon as the project has code.
"""

import importlib


def test_package_imports() -> None:
    module = importlib.import_module("doc_extract_review")
    assert module.__name__ == "doc_extract_review"
