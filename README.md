# Exploit Database Analysis: Open Source Exploits and KEV Comparison

This project analyzes open-source exploits from ExploitDB (2020-present), enriches them with OSV (Open Source Vulnerabilities) data, and compares them with the Vulncheck KEV (Known Exploited Vulnerabilities) database using semantic similarity analysis.

## Overview

The analysis pipeline:
1. Extracts open-source exploits from ExploitDB (2020-present)
2. Enriches exploit data with OSV vulnerability information via API
3. Splits exploits into two groups: found in KEV vs. not found in KEV
4. Performs semantic similarity analysis on exploit code
5. Identifies predictors for high similarity scores using metadata features

## Features

- **Open Source Exploit Extraction**: Filters ExploitDB for open-source exploits from 2020 onwards
- **OSV API Integration**: Enriches exploits with vulnerability data from OSV database
- **KEV Comparison**: Uses Vulncheck KEV API to identify actively exploited vulnerabilities
- **Semantic Similarity Analysis**: Compares exploit code using sentence transformers to find similar patterns
- **Metadata Feature Analysis**: Identifies which metadata features (platform, vulnerability type, CVE presence) predict high similarity
- **Comprehensive Visualizations**: Generates detailed plots and heatmaps for analysis

## Requirements

- Python 3.7+
- Jupyter Notebook or JupyterLab
- Internet connection (for API calls)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/JaimeBlok/BEP-JaimeRam.git
cd BEP-JaimeRam
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Open `exploit_analysis.ipynb` in Jupyter Notebook
2. Run all cells in order
3. The notebook will automatically:
   - Download ExploitDB data
   - Query OSV API for vulnerability information
   - Download KEV data from Vulncheck API
   - Perform semantic similarity analysis
   - Generate visualizations and analysis results

## Project Structure

```
.
├── exploit_analysis.ipynb          # Main analysis notebook
├── README.md                        # This file
├── requirements.txt                 # Python dependencies
└── .gitignore                       # Git ignore rules
```

## Analysis Steps

The notebook is organized into the following steps:

1. **Package Installation**: Installs required Python packages
2. **Extracting Exploit Code from Open Source (2020-Present)**: Downloads and filters ExploitDB data
3. **Enriching with OSV Data**: Queries OSV API to enrich exploits with vulnerability information
4. **Splitting into KEV and Non-KEV Group**: Separates exploits based on Vulncheck KEV database
5. **Analysis of Both Groups**: Performs statistical and comparative analysis
6. **Semantic Similarity Analysis**: Compares exploit code using embeddings
7. **Metadata Feature Analysis**: Identifies predictors for high similarity scores
8. **Vulnerability Type & Platform Analysis**: Deep dive into specific predictors

## Key Findings

The analysis provides insights into:
- Which non-KEV exploits have high similarity to KEV exploits (potential candidates for KEV inclusion)
- Which vulnerability types and platforms are best predictors for high similarity
- Statistical significance of different metadata features
- Platform-vulnerability type combinations that predict high similarity

## Output Files

When you run the notebook, it generates:
- CSV files with analysis results
- JSON files with similarity data
- PNG visualizations of all analyses
- Statistical summaries and feature importance rankings

## API Keys

The notebook uses:
- **Vulncheck API**: Requires API key (already included in notebook)
- **OSV API**: Public API, no key required
- **ExploitDB**: Public GitLab repository

## License

This project is part of a Bachelor's End Project (BEP).

## Author

Jaime Ram - 5558581

## Acknowledgments

- ExploitDB for providing exploit data
- OSV (Google) for vulnerability information
- Vulncheck for KEV database access
