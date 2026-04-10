# Party manifesto embeddings (BJP / INC)

Sentence embeddings and analysis on Indian party manifesto text (notebooks: MPNet and MiniLM).

## Reproduce

1. **Python 3.10+**
2. Install dependencies (from repo root):

   ```bash
   pip install -e .
   ```

3. **Data:** put PDFs in `pdf_data/` as `BJP_{year}.pdf` / `INC_{year}.pdf` (e.g. 2009, 2014, 2019, 2024).
4. **Build text files:**

   ```bash
   python preprocess.py          # → data/*.txt
   python mask_data.py           # optional → masked_pdf_data/*.txt
   ```

5. **Run analysis:** open `p1_mpnet.ipynb` or `p1_minilm.ipynb` and run all cells. Use `data/` for unmasked runs; use `masked_pdf_data/` where the notebook expects masked text.

Figures are written alongside the repo (e.g. `1MPNet_*.png`, `1MiniLM_*.png`).

More on the dataset layout: `DATASET.md`.
