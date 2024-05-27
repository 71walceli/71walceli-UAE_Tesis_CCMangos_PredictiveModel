
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def freq_bar(x, ax=plt, **plt_args):
    x = x.value_counts()
    return ax.bar(x.index.values, x.values, **plt_args)

def range_labels(start, end, size, decimals=None):
    values = np.linspace(start,end,size+1)
    return [f"{i1:.2f}-{i2:.2f}" for i1,i2 in zip(values[:-1],values[1:])]

def freq_bar_ranges(x, size, ax=plt, **plt_args):
    start = x.min()
    end = x.max()
    bins = np.linspace(start,end,size)
    x_bins = pd.DataFrame()
    x_bins["bin"] = np.digitize(x, bins)
    x_bins["value"] = x
    x_counts = x_bins.groupby("bin").size()
    bars = ax.bar(x_counts.index, x_counts, **plt_args)
    labels = range_labels(start,end,size)
    if ax != plt:
        ax.set_xticks(ticks=range(1,size+1), labels=range_labels(start,end,size),rotation=60)
    else:
        plt.xticks(ticks=range(1,size+1), labels=range_labels(start,end,size),rotation=60)
    return bars
