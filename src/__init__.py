# src/__init__.py
"""
Simple package initializer for the ape_project.src package.
Exports commonly used functions for convenience.
"""

from .data_utils import load_csv, save_csv, standardize_columns, merge_on_animal_day
from .viz_utils import plot_timecourse, plot_group_boxplot, plot_km
from .stats_utils import fit_mixedlm, fit_coxph, summarize_df

__all__ = [
    "load_csv",
    "save_csv",
    "standardize_columns",
    "merge_on_animal_day",
    "plot_timecourse",
    "plot_group_boxplot",
    "plot_km",
    "fit_mixedlm",
    "fit_coxph",
    "summarize_df",
]
