# Wind Farm Socioeconomic Geospatial Analysis

**Understanding the Influence of Socioeconomic and Housing Characteristics on Wind Farm Development in Iowa, Oklahoma, and Texas**

![Python](https://img.shields.io/badge/Python-3.12-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## Overview

This project recreates and modernizes a Master's research study examining how socioeconomic and housing characteristics influence the development of wind farms across Iowa, Oklahoma, and Texas. Using modern data science and geospatial techniques, the project builds a reproducible pipeline from raw public data to predictive modeling and spatial visualization.

**Research Question:**  
What socioeconomic and housing factors are associated with the presence of wind farms at the census tract level?

---

## Key Findings

- Tracts with wind farms tend to have **lower median home values** and **lower population density**.
- **Higher median household income** is positively associated with wind farm presence after controlling for other factors.
- Areas with **older housing stock** and lower recent development are more likely to host wind farms.
- A logistic regression model achieved a **ROC-AUC of 0.830**, demonstrating good discriminative power.

---

## Methodology

1. **Data Acquisition**
   - US Wind Turbine Database (USWTDB v8.3)
   - American Community Survey (ACS) 2022 5-Year Estimates (Tract level)
   - Census TIGER/Line shapefiles via `pygris`

2. **Feature Engineering**
   - Created derived features: `% recent housing`, `housing density`, and `income vs home value ratio`

3. **Modeling**
   - Improved Logistic Regression with `class_weight="balanced"`
   - Compared against HistGradientBoostingClassifier

4. **Evaluation**
   - Accuracy: **0.737**
   - ROC-AUC: **0.830**

---

## Visualizations

### Feature Importance
![Feature Importance](notebooks/figures/feature_importance.png)

### ROC Curve
![ROC Curve](notebooks/figures/roc_curve.png)

### Confusion Matrix
![Confusion Matrix](notebooks/figures/confusion_matrix.png)

---

## Project Structure
windfarm_socioecon_geospatial_analysis/
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
├── notebooks/
│   ├── 01_data_acquisition_uswtdb.ipynb
│   ├── 02_uswtdb_sql_inspection.ipynb
│   ├── 03_load_census_tracts_and_acs.ipynb
│   ├── 04_spatial_join.ipynb
│   └── 05_modeling_and_visualization.ipynb
├── src/                  # (Future) modular Python package
├── docs/
├── figures/
├── README.md
└── requirements.txt

## How to Reproduce

```bash
# 1. Clone the repository
git clone https://github.com/jakemammenwx/windfarm_socioecon_geospatial_analysis.git
cd windfarm_socioecon_geospatial_analysis

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate          # macOS/Linux
# .venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run notebooks in order (recommended)
jupyter notebook
```

Note: Some notebooks require downloading ACS data manually from data.census.gov due to API limitations.