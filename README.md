# Party manifesto embeddings (BJP / INC)

This project encodes Indian party manifesto text with **Sentence Transformers**, then runs **UMAP** views, **rhetorical drift** comparisons, and **logistic regression** (train on 2009–2019, test on 2024). Two encoder setups are provided: **MPNet** (`all-mpnet-base-v2`) and **MiniLM** (`all-MiniLM-L6-v2`).

## Repository layout

| Path | Role |
|------|------|
| `processing_pipeline/` | `preprocess.py` (PDF → text), `mask_data.py` (optional party-name masking) |
| `transformers_ipynbs/` | Analysis notebooks: `p1_mpnet.ipynb`, `p1_minilm.ipynb` |
| `pdf_data/` | Source manifesto PDFs (`BJP_{year}.pdf`, `INC_{year}.pdf`) |
| `data/` | Plain text extracted from PDFs (input to notebooks for **unmasked** runs) |
| `masked_pdf_data/` | Masked `.txt` files (party tokens replaced; **masked** notebook sections) |
| `results/` | Saved figures and exports (optional; notebooks can also write PNGs to the working directory) |
| `DATASET.md` | Naming conventions and dataset notes |

## Requirements

- **Python 3.10+**
- Dependencies are declared in `pyproject.toml`. From the **repository root**:

  ```bash
  pip install -e .
  ```

## Reproduce the text data

Commands assume your shell’s **current directory is the repo root** (paths like `pdf_data/` and `data/` are relative to that).

1. Place PDFs under `pdf_data/` using names such as `BJP_2009.pdf`, `INC_2014.pdf`, etc.
2. Extract text:

   ```bash
   python processing_pipeline/preprocess.py
   ```

   Writes one `.txt` per PDF into `data/`.

3. *(Optional)* Build masked copies for runs that strip party-related strings:

   ```bash
   python processing_pipeline/mask_data.py
   ```

   Reads from `data/`, writes to `masked_pdf_data/`.

## Run the notebooks

1. Start Jupyter or VS Code’s notebook UI **with the repository root as the working directory** (e.g. run `jupyter lab` from the repo root, or open the folder as the workspace root). The notebooks load paths like `data/` and `masked_pdf_data/` relative to that root.
2. Open `transformers_ipynbs/p1_mpnet.ipynb` or `transformers_ipynbs/p1_minilm.ipynb`.
3. **Run all cells** from top to bottom. Earlier cells load sentence-transformers models; later cells build embeddings, plots, and classifiers.
4. **Masked vs unmasked:** the notebooks switch `data_dir` between `masked_pdf_data` and `data` in different sections—use the matching folder for each block.

`plt.savefig(...)` calls write PNGs (e.g. `1MPNet_*.png`, `1MiniLM_*.png`) into the **process working directory** (typically the repo root if you followed step 1).

## Documentation

For file naming and dataset usage details, see **`DATASET.md`**.
