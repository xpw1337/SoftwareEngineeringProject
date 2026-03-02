# Synthetic Data Generation: A Comparative Study

> **Generating Synthetic Data using Data Augmentation** — A comparative analysis of **CTGAN**, **SMOTE-TOMEK**, and **DataSynthesizer** for tabular and imbalanced data.

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)

---

## Overview

This Software Engineering project implements and compares three synthetic data generation algorithms in Python:

| Algorithm | Use Case | Dataset |
|-----------|----------|---------|
| **CTGAN** (Conditional Tabular GAN) | Generative synthetic tabular data | `insurance.csv` |
| **SMOTE-TOMEK** | Balancing imbalanced data (oversampling + cleaning) | `insurance.csv` |
| **DataSynthesizer** | Privacy-preserving synthetic data (differential privacy) | `adult_ssn.csv` |

The goal is to evaluate how well each method preserves statistical properties of the original data and to support informed choices for **data augmentation**, **privacy-preserving analytics**, and **ML model training** on limited or sensitive data.

---

## Authors

- **Arijit Kulkarni** (K029)
- **Parshwa Jani** (K025)
- **Jeet Desai** (K010)

---

## Project Structure

```
SoftwareEngineeringProject/
├── README.md
├── ProjectWriteup.pdf          # Full project report
└── Project/
    ├── CTGAN/
    │   ├── CTGAN_Insurance_Self.ipynb   # CTGAN pipeline on insurance data
    │   ├── insurance.csv
    │   └── samples.csv                  # Generated synthetic samples
    ├── SMOTE-TOMEK/
    │   ├── insurance.csv
    │   ├── insurance_coded.csv         # Encoded for SMOTE-TOMEK
    │   └── insurance_smote_tomek.csv   # Balanced dataset
    ├── DataSynthesizer/
    │   ├── adult_ssn.csv
    │   └── description.json            # Schema / metadata
    └── [image augmentation scripts]   # Supplementary: randomflip, randomrotate, etc.
```

---

## Algorithms at a Glance

### 1. CTGAN (Conditional Tabular GAN)

- **Purpose:** Generate synthetic tabular data that mimics the original distribution.
- **Idea:** GAN tailored for mixed discrete/continuous columns; supports conditional sampling.
- **Output:** New rows that preserve correlations and marginal distributions (e.g. `samples.csv`).

### 2. SMOTE-TOMEK

- **Purpose:** Handle **class imbalance** (e.g. rare “smoker” class in insurance data).
- **Idea:** SMOTE oversamples the minority class; Tomek links remove borderline majority samples.
- **Output:** A balanced dataset (e.g. `insurance_smote_tomek.csv`) for more robust model training.

### 3. DataSynthesizer

- **Purpose:** Generate synthetic data with **privacy guarantees** (differential privacy).
- **Idea:** Learns distributions and correlations from the original data and samples under privacy constraints.
- **Output:** Synthetic datasets (e.g. from `adult_ssn.csv`) suitable for sharing or analysis without exposing real records.

---

## Getting Started

### Prerequisites

- Python 3.7+
- Jupyter (for the CTGAN notebook)

### Installation

```bash
# Clone the repository
git clone https://github.com/xpw1337/SoftwareEngineeringProject.git
cd SoftwareEngineeringProject
```

**CTGAN:**

```bash
pip install ctgan pandas
```

**SMOTE-TOMEK:**

```bash
pip install imbalanced-learn pandas table-evaluator
```

**DataSynthesizer:**

```bash
pip install DataSynthesizer pandas
```

### Running the CTGAN Pipeline

1. Open `Project/CTGAN/CTGAN_Insurance_Self.ipynb` in Jupyter.
2. Ensure `insurance.csv` is in the same folder (or adjust paths).
3. Run all cells to train the model and generate `samples.csv`.

SMOTE-TOMEK and DataSynthesizer code and usage are described in **ProjectWriteup.pdf**.

---

## Evaluation

The project compares synthetic vs. original data using:

- **Statistical similarity** (distributions, correlations)
- **Data utility** for downstream tasks
- **Privacy vs. utility** trade-offs where applicable

Details, plots, and conclusions are in **ProjectWriteup.pdf**.

---

## Report

Full methodology, results, and discussion: **[ProjectWriteup.pdf](ProjectWriteup.pdf)**

---

## Repository

**GitHub:** [https://github.com/xpw1337/SoftwareEngineeringProject](https://github.com/xpw1337/SoftwareEngineeringProject)

---

## License

This project is for educational purposes (Software Engineering course).
