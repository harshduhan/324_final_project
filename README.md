# Indian Party Manifesto Analysis using Sentence Embeddings

This project analyzes Indian political party manifestos using transformer-based sentence embeddings, dimensionality reduction, and classification. It compares rhetorical patterns across party manifestos and evaluates whether manifesto chunks can be distinguished by party using semantic embeddings.

## Overview

The project does the following:

- Loads manifesto text files for different parties and years
- Splits each manifesto into chunked text segments
- Generates sentence embeddings using a SentenceTransformer model
- Projects embeddings into 2D using UMAP for visualization
- Measures rhetorical drift across manifesto years using cosine distance between embedding centroids
- Compares transformer embeddings against a TF-IDF baseline for party classification
- Predicts the most likely party for a new paragraph

## Dataset Structure

The notebook expects manifesto text files inside a `data/` folder with filenames like:

```bash
data/
├── BJP_2009.txt
├── BJP_2014.txt
├── INC_2009.txt
└── INC_2014.txt
```

The code for rhetorical drift also attempts to use `2019` manifesto files, so if you want that section to run correctly, you should also include:

```bash
data/BJP_2019.txt
data/INC_2019.txt
```

## Features

### 1. Text Loading and Chunking
Manifestos are loaded from `.txt` files and broken into chunks of roughly 300 words by splitting on sentence boundaries.

### 2. Semantic Embeddings
The project uses `SentenceTransformer` embeddings to represent manifesto chunks in semantic space.

Current model in the notebook:

```python
model_name = 'all-MiniLM-L6-v2'
```

There is also a commented option for a stronger but slower model:

```python
# model_name = 'all-mpnet-base-v2'
```

### 3. UMAP Visualization
All chunk embeddings are combined and reduced to 2 dimensions using UMAP, then plotted to visualize rhetorical clustering by party and year.

Output file:

```bash
1MPNet_umap_scatter_custom.png
```

### 4. Rhetorical Drift
The notebook computes centroid embeddings for each manifesto and measures cosine distance across years to estimate rhetorical change over time.

Output file intended:

```bash
1MPNet_rhetorical_drift_corrected.png
```

### 5. Party Classification
A logistic regression classifier is trained on:

- Sentence-transformer embeddings
- TF-IDF features as a baseline

This allows comparison of semantic vs lexical features for predicting whether a chunk comes from BJP or INC.

### 6. New Paragraph Prediction
The notebook includes a helper function to classify an unseen paragraph and return prediction probabilities.

## Installation

Create a Python environment and install the required packages:

```bash
pip install numpy pandas tqdm matplotlib seaborn sentence-transformers scikit-learn umap-learn
```

## Imports Used

```python
import os
import numpy as np
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns

from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_distances
import umap
```

## How to Run

1. Place the manifesto `.txt` files in the `data/` directory.
2. Open the notebook.
3. Run the cells in sequence.
4. Review the generated plots and printed classification results.

## Example Workflow

### Load and chunk text
The notebook reads each manifesto file and splits it into chunks for downstream modeling.

### Encode with SentenceTransformer
Each chunk is embedded into a dense vector space using a pretrained transformer model.

### Visualize with UMAP
The chunk embeddings are projected into 2D to inspect whether political language clusters by party or time period.

### Compute rhetorical drift
Centroids are computed for each manifesto year and party, then cosine distance is used to quantify changes in rhetoric across elections.

### Compare classifiers
The notebook evaluates whether semantic embeddings outperform TF-IDF features for party prediction.

## Results

From the notebook output:

- BERT-style sentence embeddings outperform the TF-IDF baseline for classification.
- UMAP helps visually inspect separation between manifesto chunks.
- Rhetorical drift provides an interpretable way to compare manifesto evolution over time.

## Known Issue

The rhetorical drift section may fail with a `KeyError: ('BJP', '2019')` if the 2019 manifesto files are not present in the `data/` folder.

To fix this:

- Add the missing 2019 text files, or
- Modify the drift-analysis code to only use years that are available

## Possible Improvements

- Add support for more parties and election years
- Save chunk metadata to CSV for easier inspection
- Use a stronger embedding model such as `all-mpnet-base-v2`
- Add confusion matrices and more classification metrics
- Turn the notebook into a reusable Python script or package
- Add interactive plots with Plotly

## Project Structure

```bash
.
├── data/
│   ├── BJP_2009.txt
│   ├── BJP_2014.txt
│   ├── INC_2009.txt
│   ├── INC_2014.txt
│   ├── BJP_2019.txt        # optional but needed for drift section
│   └── INC_2019.txt        # optional but needed for drift section
├── notebook.ipynb
├── 1MPNet_umap_scatter_custom.png
├── 1MPNet_rhetorical_drift_corrected.png
└── README.md
```

## Use Case

This project is useful for:

- Political text analysis
- NLP-based rhetoric comparison
- Exploring semantic similarity across long-form documents
- Demonstrating transformer embeddings on real-world text corpora

## License

Add a license here if you plan to publish or share the project publicly.
