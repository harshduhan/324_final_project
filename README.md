# Party manifesto embeddings (BJP / INC)

## Setup

```bash
pip install pandas numpy tqdm matplotlib seaborn sentence-transformers scikit-learn scipy umap-learn PyMuPDF
```

(`requirements.txt` only pins pandas; use the line above for notebooks and scripts.)

## Data

- **Raw PDFs:** `pdf_data/{BJP,INC}_{2009,2014,2019,2024}.pdf`
- **Extract text:** `python preprocess.py` → writes `data/*.txt`
- **Masked text (party-name tokens removed):** `python mask_data.py` → writes `masked_pdf_data/*.txt`

Notebooks use **`data/`** for unmasked runs and **`masked_pdf_data/`** for masked UMAP/drift cells. More detail: `DATASET.md`.

## Run

1. Ensure `data/` (and optionally `masked_pdf_data/`) contain the `.txt` files you need.
2. Open **`p1_mpnet.ipynb`** or **`p1_minilm.ipynb`**.
3. **Run all cells** from the top (model load → encoding → analysis). The MPNet notebook selects `all-mpnet-base-v2`; MiniLM uses `all-MiniLM-L6-v2`.

Figures save next to the repo (e.g. `1MPNet_*` / `1MiniLM_*` PNGs).
