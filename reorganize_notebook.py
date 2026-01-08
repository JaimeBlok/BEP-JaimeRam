#!/usr/bin/env python3
"""
Script to help reorganize the notebook by updating all save paths
This is a helper script - manual review still needed
"""

import json
import re

# Mapping of file patterns to output directories
file_mappings = {
    'files_exploits.csv': 'outputs/step1_data_extraction/',
    'exploits_found_in_kev.csv': 'outputs/step3_kev_splitting/',
    'exploits_not_found_in_kev.csv': 'outputs/step3_kev_splitting/',
    'kev_data.json': 'outputs/step3_kev_splitting/',
    'kev_check_results.json': 'outputs/step3_kev_splitting/',
    'semantic_similarity_results.json': 'outputs/step4_similarity_analysis/',
    'similarity_matrix.csv': 'outputs/step4_similarity_analysis/',
    'top_similarity_pairs': 'outputs/step4_similarity_analysis/',
    'high_similarity_pairs': 'outputs/step4_similarity_analysis/',
    'non_kev_candidates': 'outputs/step4_similarity_analysis/',
    'feature_correlations.csv': 'outputs/step5_metadata_analysis/',
    'feature_importance': 'outputs/step5_metadata_analysis/',
    'platform_statistics': 'outputs/step5_metadata_analysis/',
    'vulnerability_type_statistics': 'outputs/step5_metadata_analysis/',
    '.png': 'outputs/step6_visualizations/',
}

print("This script helps identify files that need path updates.")
print("Manual review and update of the notebook is still required.")
print("\nFile mappings:")
for pattern, directory in file_mappings.items():
    print(f"  {pattern:40s} -> {directory}")

