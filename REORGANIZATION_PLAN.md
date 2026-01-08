# Reorganization Plan

## Structure
- Step 0: Setup (packages, style, directories)
- Step 1: Data Extraction (ExploitDB download + exploration)
- Step 2: OSV Enrichment (OSV API + exploration)
- Step 3: KEV Splitting (KEV API + split + exploration)
- Step 4: Similarity Analysis (code similarity + exploration)
- Step 5: Metadata Analysis (feature analysis)
- Step 6: Final Visualizations (thesis-ready plots)

## Changes Needed
1. All outputs go to `outputs/stepX_*/` directories
2. Each dataset gets exploration cell with:
   - Variable descriptions
   - Head(5) display
   - Basic statistics plot
   - Overview plot for thesis
3. Simplify all plots (remove fancy styling, keep functional)
4. Reduce file sizes where possible

