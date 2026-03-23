# Project Structure

This repository analyzes Indian political party manifestos using text preprocessing, sentence embeddings, visualization, and classification workflows.

## Repository Layout

- `data/`  
  Contains manifesto text files used as the primary dataset for analysis and modeling.

- `pdf_data/`  
  Stores PDF-based source material or intermediate extracted content derived from source documents.

- `preprocess.py`  
  Handles text cleaning, preprocessing, and preparation steps before modeling or embedding generation.

- `p1.ipynb`  
  Main notebook for exploratory analysis and the overall project workflow.

- `p1_minilm.ipynb`  
  Notebook focused on experiments using MiniLM-based sentence embeddings.

- `p1_mpnet.ipynb`  
  Notebook focused on experiments using MPNet-based sentence embeddings.

- `requirements.txt`  
  Lists the Python dependencies required to run the notebooks and scripts in this project.

- `README.md`  
  Provides an overview of the project, setup instructions, and a summary of the analysis pipeline.

## Workflow Summary

1. Collect and organize manifesto text data.
2. Preprocess and clean the text.
3. Generate sentence embeddings for semantic analysis.
4. Visualize embedding structure and compare party rhetoric.
5. Evaluate classification approaches across representation methods.

## Notes

- Keep large raw files organized inside the data folders.
- Use separate notebooks for separate modeling experiments.
- Document any major preprocessing or modeling changes in the repository documentation.
