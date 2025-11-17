"""Utility plots for exploratory analysis."""

from __future__ import annotations

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


sns.set_style("whitegrid")


def plot_rating_distribution(df: pd.DataFrame):
    if "overall" not in df.columns:
        raise ValueError("Column 'overall' not present")
    plt.figure(figsize=(7, 4))
    sns.countplot(x="overall", data=df, palette="viridis")
    plt.title("Ratings distribution")
    return plt.gca()


def plot_cluster_sizes(labels):
    series = pd.Series(labels)
    counts = series.value_counts().sort_index()
    plt.figure(figsize=(10, 4))
    counts.plot(kind="bar", color="#0b7fab")
    plt.title("Cluster sizes")
    plt.xlabel("Cluster id")
    plt.ylabel("# Reviews")
    return plt.gca()


__all__ = ["plot_rating_distribution", "plot_cluster_sizes"]
