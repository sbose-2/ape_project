# src/viz_utils.py
import matplotlib.pyplot as plt
import seaborn as sns
import os

def _ensure_results_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def plot_timecourse(df, x="day", y="value", hue="group", title=None, savepath=None):
    """
    Lineplot with points for repeated measures.
    df: DataFrame with columns x, y, hue.
    """
    plt.figure(figsize=(7,4))
    sns.lineplot(data=df, x=x, y=y, hue=hue, estimator="mean", ci="sd", marker="o")
    plt.xlabel(x)
    plt.ylabel(y)
    if title:
        plt.title(title)
    plt.tight_layout()
    if savepath:
        _ensure_results_dir(savepath)
        plt.savefig(savepath, dpi=300, bbox_inches="tight")
    plt.show()

def plot_group_boxplot(df, x="group", y="value", title=None, savepath=None):
    plt.figure(figsize=(6,4))
    sns.boxplot(data=df, x=x, y=y)
    sns.stripplot(data=df, x=x, y=y, color="0.3", size=3, jitter=True)
    if title:
        plt.title(title)
    plt.tight_layout()
    if savepath:
        _ensure_results_dir(savepath)
        plt.savefig(savepath, dpi=300, bbox_inches="tight")
    plt.show()

def plot_km(kmf_dict, title="Kaplan-Meier", savepath=None):
    """
    Accept a dict of label -> lifelines.KaplanMeierFitter (already fit),
    and plot them together.
    """
    plt.figure(figsize=(7,5))
    for label, kmf in kmf_dict.items():
        kmf.plot_survival_function(label=label)
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Survival probability")
    plt.tight_layout()
    if savepath:
        _ensure_results_dir(savepath)
        plt.savefig(savepath, dpi=300, bbox_inches="tight")
    plt.show()
