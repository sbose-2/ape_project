# src/data_utils.py
import pandas as pd
import os

def load_csv(path, **read_csv_kwargs):
    """Load a CSV into a pandas DataFrame with a helpful error message."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} does not exist.")
    return pd.read_csv(path, **read_csv_kwargs)

def save_csv(df, path, index=False):
    """Save DataFrame to CSV, creating directories if needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=index)

def standardize_columns(df, lower=True, strip=True, replace_spaces=True):
    """Normalize column names: strip, lower, replace spaces with underscores."""
    cols = df.columns
    if strip:
        cols = [c.strip() for c in cols]
    if lower:
        cols = [c.lower() for c in cols]
    if replace_spaces:
        cols = [c.replace(" ", "_") for c in cols]
    df = df.copy()
    df.columns = cols
    return df

def ensure_animal_and_day(df, id_col="animalid", day_col="day"):
    """Ensure animal id is string and day is numeric (int or float)."""
    df = df.copy()
    if id_col in df.columns:
        df[id_col] = df[id_col].astype(str)
    if day_col in df.columns:
        df[day_col] = pd.to_numeric(df[day_col], errors="coerce")
    return df

def merge_on_animal_day(dfs, how="outer", on=["animalid", "day"]):
    """
    Merge a list of dataframes on animalid & day.
    dfs: list of pd.DataFrame
    """
    if not dfs:
        return None
    merged = dfs[0].copy()
    for df in dfs[1:]:
        merged = merged.merge(df, on=on, how=how)
    return merged

def summarize_df(df):
    """Return a simple summary (shape, missingness, dtypes)."""
    return {
        "shape": df.shape,
        "dtypes": df.dtypes.to_dict(),
        "missing_per_column": df.isnull().sum().to_dict(),
    }
