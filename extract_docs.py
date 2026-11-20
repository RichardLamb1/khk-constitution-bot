"""Convert the two governance PDFs next to this script to UTF-8 Markdown."""

from pathlib import Path
from tempfile import TemporaryDirectory

import pymupdf4llm


PROJECT_DIR = Path(__file__).resolve().parent


def main() -> None:
    pdf_paths = [PROJECT_DIR / name for name in ("constitution.pdf", "bylaws.pdf")]
    missing = [path.name for path in pdf_paths if not path.is_file()]
    if missing:
        raise SystemExit(f"Place {', '.join(missing)} next to extract_docs.py.")

    documents: dict[Path, str] = {}
    for path in pdf_paths:
        try:
            markdown = pymupdf4llm.to_markdown(str(path))
        except Exception as error:
            raise SystemExit(f"Could not convert {path.name}. {error}") from None
        if not markdown.strip():
            raise SystemExit(f"No text was extracted from {path.name}. Check the PDF.")
        documents[path.with_suffix(".md")] = markdown

    try:
        with TemporaryDirectory(dir=PROJECT_DIR) as staging:
            staging_path = Path(staging)
            for path, markdown in documents.items():
                (staging_path / path.name).write_text(markdown, encoding="utf-8")
            for path in documents:
                (staging_path / path.name).replace(path)
                print(f"Wrote {path.name}")
    except OSError as error:
        raise SystemExit(f"Could not write the Markdown documents. {error}") from None


if __name__ == "__main__":
    main()
