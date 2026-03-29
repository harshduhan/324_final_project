import fitz  # PyMuPDF
from pathlib import Path
from tqdm import tqdm

# ================================
# CONFIGURATION
# ================================

PDF_DIR = Path("pdf_data")
TXT_DIR = Path("data")

# ================================
# EXTRACTION
# ================================


def extract_pdf_to_txt(pdf_path: Path, txt_path: Path) -> None:
    doc = fitz.open(pdf_path)
    print(f"Loaded PDF: {pdf_path} ({doc.page_count} pages)")

    full_text = ""
    for page_num in tqdm(range(doc.page_count), desc=f"Extracting {pdf_path.name}"):
        page = doc[page_num]
        text = page.get_text("text")  # pure text mode
        full_text += text + "\n\n"

    txt_path.parent.mkdir(parents=True, exist_ok=True)
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(full_text)

    print(f"Saved text to: {txt_path}")


def main() -> None:
    pdfs = sorted(PDF_DIR.glob("*.pdf"))
    if not pdfs:
        print(f"No PDFs found in {PDF_DIR.resolve()}")
        return

    for pdf_path in pdfs:
        txt_path = TXT_DIR / f"{pdf_path.stem}.txt"
        extract_pdf_to_txt(pdf_path, txt_path)


if __name__ == "__main__":
    main()
