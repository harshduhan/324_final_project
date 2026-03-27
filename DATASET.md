# Dataset Documentation

## Overview
This repository uses Indian political party manifesto text files as the core dataset for analysis, embedding experiments, visualization, and classification.

## Dataset Files
The current dataset is organized as plain text files in the `data/` directory.

Expected files:
- `BJP_2009.txt`
- `BJP_2014.txt`
- `INC_2009.txt`
- `INC_2014.txt`

These files represent manifesto text grouped by:
- political party
- election year

## File Naming Convention
Dataset files follow the format:

`<PARTY>_<YEAR>.txt`

Examples:
- `BJP_2009.txt`
- `INC_2014.txt`

This naming convention is used so scripts and notebooks can load files consistently and compare parties across election years.

## Source and Preprocessing
Manifesto text may originate from PDF documents and be converted into plain text using the preprocessing pipeline in `preprocess.py`.

Typical flow:
1. Store original PDF files in `pdf_data/`
2. Run preprocessing to extract text
3. Save processed text into `data/`
4. Use the cleaned text files in notebooks for analysis

## Intended Use
These dataset files are used for:
- text preprocessing
- sentence chunking
- embedding generation
- dimensionality reduction and visualization
- rhetorical comparison across parties
- year-over-year drift analysis
- classification experiments

## Directory Layout
```text
data/
  BJP_2009.txt
  BJP_2014.txt
  INC_2009.txt
  INC_2014.txt

pdf_data/
  <source PDFs>

preprocess.py
validate_dataset.py
p1.ipynb
p1_minilm.ipynb
p1_mpnet.ipynb
```

## Dataset Quality Notes
- Extracted text quality depends on PDF formatting and extraction quality
- Some files may contain OCR or spacing artifacts
- Duplicate filenames or alternate copies should be reviewed before experiments
- Consistent preprocessing is important for reliable comparisons

## Validation
The repository includes `validate_dataset.py` to help check:
- whether expected files exist
- whether filenames follow the expected convention
- whether files are empty or unusually short
- basic dataset statistics

Example usage:
```bash
python validate_dataset.py --data-dir data
```

## Future Improvements
Possible extensions to the dataset include:
- adding manifesto files from additional years
- adding more political parties
- storing metadata such as source, page count, and extraction date
- adding automated cleaning and normalization steps
- versioning the dataset separately from experiment notebooks
