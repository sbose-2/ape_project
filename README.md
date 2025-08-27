# APE Project: Biostatistical Characterization of Pulmonary Disease Models

This repository contains code, data workflows, and analysis notebooks for the Applied Practice Experience (APE).  
Focus: biostatistical analysis of immune, histological, and clinical outcomes in murine pulmonary disease models (PR8 influenza and bleomycin-induced fibrosis).

## 📂 Repo Structure
- `data/raw/` → unmodified source datasets  
- `data/processed/` → cleaned, analysis-ready datasets  
- `src/` → reusable Python modules (cleaning, visualization, stats)  
- `notebooks/` → interactive workflows for cleaning, EDA, and modeling  
- `results/` → figures and tables auto-saved by notebooks  
- `docs/` → draft report text, manuscript-ready outputs  

## ⚡ Quickstart
```bash
# Create environment
conda create -n ape python=3.11 -y
conda activate ape
pip install -r requirements.txt

# Add Jupyter kernel
pip install ipykernel
python -m ipykernel install --user --name=ape --display-name "Python (ape)"
