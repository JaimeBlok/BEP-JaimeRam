# Exploit Database Analysis 2020-Present

This project analyzes open source exploits from ExploitDB (2020-present), enriches them with OSV data, and splits them based on Vulncheck KEV.

## Requirements

- Python 3.7+
- Jupyter Notebook
- Internet connection (for OSV API and ExploitDB/KEV downloads)

## Usage

1. Open `exploit_analysis.ipynb` in Jupyter Notebook
2. Run all cells in order
   - The notebook will automatically:
     - Download ExploitDB data
     - Query OSV API for vulnerability information
     - Download KEV data
     - Perform all analyses
3. **Note**: The OSV API is used to enrich the data - no local database needed!

## Output

The notebook generates:
- `files_exploits.csv` - Raw ExploitDB data
- `kev_data.json` - KEV vulnerability data
- `exploits_found_in_kev.csv` - Exploits found in KEV
- `exploits_not_found_in_kev.csv` - Exploits not found in KEV
- Visualizations (PNG files)

## Structure

1. **Step 1**: Install packages
2. **Step 2**: Extracting exploit code from open source (2020-present)
3. **Step 3**: Enriching with OSV data (queries OSV API for each CVE found)
4. **Step 4**: Splitting into KEV and non-KEV group
5. **Step 5**: Analysis of both groups
6. **Step 6**: Visualizations
7. **Step 7**: Advanced analyses

## OSV API Integration

The notebook uses the OSV (Open Source Vulnerabilities) API to enrich ExploitDB data with:
- Vulnerability summaries
- Severity scores
- Affected packages/ecosystems
- References and additional metadata

The API is queried automatically for all CVE IDs found in the ExploitDB dataset.

## Questions?

If you have questions about the OSV database location or other aspects, let me know!

