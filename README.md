# Seam Carving

A Python implementation of content-aware image resizing based on the seam carving method by Avidan & Shamir (2007). The project focuses on the backward-energy formulation and includes seam removal, image enlargement, and a simple object removal pipeline.

## Project Overview

The implementation is developed and demonstrated in the notebook `notebooks/seam_carving_lab.ipynb`. It covers the main steps of the seam carving pipeline:

- gradient-based energy map computation
- entropy-based energy map computation
- optimal seam finding with dynamic programming
- vertical and horizontal seam removal
- multiple seam removal
- content-aware image enlargement through seam insertion
- object removal by forcing seams through a rectangular masked region

The notebook also includes qualitative comparisons with standard resizing approaches and a short discussion of cases where seam carving performs poorly.

## Project Structure

```text
seam-carving/
├── assets/
│   └── diagrams/
│       ├── enlargement-pipelines.svg
│       ├── multiple-seam-removal.svg
│       ├── object-removal-pipeline.svg
│       └── optimal-removal-pipeline.svg
├── data/
│   └── input/
│       ├── test_balloon.jpg
│       ├── test_bench.png
│       ├── test_Kanagawa.jpg
│       ├── test_Lenna.png
│       └── test.jpg
├── notebooks/
│   └── seam_carving_lab.ipynb
├── src/
│   ├── __init__.py
│   └── utils.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

```bash
# Clone the repository
git clone https://github.com/SashaPetkovic/seam-carving.git
cd seam-carving

# Create a virtual environment
python -m venv venv

# Activate the environment
# Windows:
.\venv\Scripts\Activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

All experiments and demonstrations are contained in the main notebook:

```bash
jupyter notebook notebooks/seam_carving_lab.ipynb
```

Input images are read from `data/input/`.

## References

- Avidan, S., & Shamir, A. (2007). "Seam Carving for Content-Aware Image Resizing." *ACM Transactions on Graphics (SIGGRAPH 2007)*, 26(3).

## Team

- Sasha Petkovic  - sasha.petkovic@studenti.unitn.it
- Daniele Buondonno - daniele.buondonno@studenti.unitn.it
