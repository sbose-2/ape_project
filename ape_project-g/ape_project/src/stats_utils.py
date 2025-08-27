# src/stats_utils.py
import statsmodels.formula.api as smf
from lifelines import KaplanMeierFitter, CoxPHFitter
import pandas as pd

def fit_mixedlm(df, formula, group_col="animalid", re_formula=None):
    """
    Fit a linear mixed effects model using statsmodels.
    Example formula: 'weight ~ day * group'
    """
    model = smf.mixedlm(formula, data=df, groups=df[group_col], re_formula=re_formula)
    result = model.fit(reml=True, method="lbfgs")
    return result

def fit_coxph(df, duration_col="time", event_col="event", covariates=None):
    """
    Fit a Cox proportional hazards model using lifelines.
    df: DataFrame; covariates: list of column names for covariates
    """
    df = df.copy()
    cols = [duration_col, event_col] + (covariates or [])
    cph = CoxPHFitter()
    cph.fit(df[cols], duration_col=duration_col, event_col=event_col)
    return cph

def build_km_by_group(df, time_col="time", event_col="event", group_col="group"):
    """
    Return a dict: {group_label: fitted_kmf}
    """
    kmf_dict = {}
    for name, sub in df.groupby(group_col):
        kmf = KaplanMeierFitter()
        kmf.fit(sub[time_col], sub[event_col], label=str(name))
        kmf_dict[name] = kmf
    return kmf_dict

def summarize_df(df):
    """Simple summary wrapper available here too."""
    return {
        "shape": df.shape,
        "columns": list(df.columns),
        "missing": df.isnull().sum().to_dict()
    }
