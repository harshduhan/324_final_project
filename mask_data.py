import fitz  # PyMuPDF
import os
import re
from pathlib import Path
from tqdm import tqdm

# ================================
# CONFIGURATION
# ================================

DATA_DIR = Path("data")
OUTPUT_DIR = Path("masked_pdf_data")

# Longest / most specific patterns first (case-insensitive).
_MASK_PATTERNS = [
    re.compile(r"\bBhartiya\s+Janat[ao]?\s+Party\b", re.IGNORECASE),
    re.compile(r"\bBharatiya\s+Janata\s+Party\b", re.IGNORECASE),
    re.compile(r"\bcongress\b", re.IGNORECASE),
    re.compile(r"\bBJP\b", re.IGNORECASE),
    re.compile(r"\bINC\b", re.IGNORECASE),
    re.compile(r"\bNDA\b", re.IGNORECASE),
    re.compile(r"\bUPA\b", re.IGNORECASE),
]

MASK_TOKEN = "[MASKED]"


def extract_text_from_pdf(pdf_path: Path) -> str:
    """Same extraction as preprocess.py: page-wise text, joined with blank lines."""
    doc = fitz.open(pdf_path)
    full_text = ""
    for page_num in tqdm(range(doc.page_count), desc=f"Extracting {pdf_path.name}"):
        page = doc[page_num]
        text = page.get_text("text")
        full_text += text + "\n\n"
    return full_text


def load_text_from_data_file(path: Path) -> str:
    if path.suffix.lower() == ".pdf":
        return extract_text_from_pdf(path)
    if path.suffix.lower() == ".txt":
        return path.read_text(encoding="utf-8")
    raise ValueError(f"Unsupported file type: {path}")


def mask_text(text: str) -> str:
    out = text
    for pat in _MASK_PATTERNS:
        out = pat.sub(MASK_TOKEN, out)
    return out


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    files = sorted(
        p
        for p in DATA_DIR.iterdir()
        if p.is_file() and p.suffix.lower() in {".pdf", ".txt"}
    )
    if not files:
        print(f"No .pdf or .txt files found in {DATA_DIR.resolve()}")
        return

    for src in files:
        print(f"Processing {src.name}...")
        raw = load_text_from_data_file(src)
        masked = mask_text(raw)
        # Keep .txt output (same basename as source, .txt for PDFs too)
        out_path = OUTPUT_DIR / (src.stem + ".txt")
        out_path.write_text(masked, encoding="utf-8")
        print(f"  Wrote {out_path}")


if __name__ == "__main__":
    main()
