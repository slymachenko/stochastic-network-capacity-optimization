"""Utility helpers shared across notebooks and scripts."""

import matplotlib.pyplot as plt
from pathlib import Path

from typing import Optional

def apply_plot_style() -> None:
    """Apply a plotting style across all figures."""
    if "seaborn-v0_8-whitegrid" in plt.style.available:
        plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update(
        {
            "figure.dpi": 120,
            "axes.titlesize": 12,
            "axes.labelsize": 11,
            "legend.fontsize": 10,
            "grid.alpha": 0.3,
            "grid.linestyle": "-",
            "lines.linewidth": 2,
        }
    )

def setup_axes(
    ax,
    *,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    legend: bool = False,
    legend_kwargs: Optional[dict] = None,
) -> None:
    """Apply common axis settings."""
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title)

    ax.grid(alpha=0.3)

    if legend:
        ax.legend(**(legend_kwargs or {}))

def finalize_figure(fig, save_path: Optional[str | Path] = None, *, dpi: int = 300, show: bool = True) -> None:
    """Apply final layout and save/show the figure."""
    fig.tight_layout()

    if save_path is not None:
        save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(save_path, dpi=dpi, bbox_inches="tight")

    if show:
        plt.show()
