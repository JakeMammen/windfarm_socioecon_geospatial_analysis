# Modernized Wind Farm Socio-Economic Influence Study – Scope Definition
- The purpose of this project is to update the data, demonstrate modern open-source geospatial DS skills, turn the thesis into a strong portfolio piece

## Original Research Objectives (from 2022 thesis)
- The objective of this study is to analyze twelve different socioeconomic variables and one environmental dataset across Iowa, Oklahoma, and Texas to determine if there are any influences on wind farm development. 
- Additionally, this study will determine if there is spatial clustering among wind farms and whether it’s due to a random process. 
- Lastly, the results of this study will show how socioeconomic and environmental characteristics alone don’t provide enough evidence to predict the likelihood of future wind farm development. While there may be numerous studies addressing the impacts of common factors, these studies tend to only focus on each factor individually. 
- Through a widely used mixed methods approach of geospatial and statistical analysis, this study effectively analyzes combined qualitative and quantitative data

## Updated Datasets & Time Period (2026 recreation)
- US Wind Turbine Database: v8.3 (March 2026)
- American Community Survey: 2020–2024 5-year estimates (tract level)
- National Land Cover Database: NLCD 2021 (or Annual NLCD)
- Geographic focus: Iowa, Oklahoma, Texas only

## What Stays the Same vs. What We Modernize
- Same: Core research questions, three-state focus, tract-level socio-economic analysis, CSR/clustering test, land-cover change detection
- Modernized: Full Python pipeline, DuckDB-spatial + GeoParquet, pysal/pointpats, optional lightweight XGBoost layer, interactive Streamlit dashboard + MapLibre/PMTiles option for GitHub Pages

## Portfolio Deliverables
- Professional README with methodology, updated findings, and “how to reproduce”
- Numbered Jupyter notebooks / scripts
- Interactive dashboard (Streamlit)
- High-quality static maps + optional embeddable MapLibre map