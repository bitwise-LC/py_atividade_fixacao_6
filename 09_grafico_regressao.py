"""Dispersão com regressão linear entre renda mensal e gasto mensal."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    dados = pd.read_csv(BASE_DIR / "data" / "dados_regressao.csv")
    sns.set_theme(style="whitegrid")
    x = dados["renda_mensal"].to_numpy()
    y = dados["gasto_mensal"].to_numpy()

    r_quadrado = np.corrcoef(x, y)[0, 1] ** 2

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.regplot(
        data=dados,
        x="renda_mensal",
        y="gasto_mensal",
        scatter_kws={"alpha": 0.65, "s": 45},
        line_kws={"linewidth": 2.5},
        color="#DC2626",
        ax=ax,
    )
    ax.set_title("Relação entre renda mensal e gasto mensal")
    ax.set_xlabel("Renda mensal (R$)")
    ax.set_ylabel("Gasto mensal (R$)")
    ax.text(
        0.03,
        0.95,
        f"R² = {r_quadrado:.3f}",
        transform=ax.transAxes,
        va="top",
        bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.8},
    )

    fig.tight_layout()
    saida = BASE_DIR / "graficos" / "grafico_regressao.png"
    saida.parent.mkdir(exist_ok=True)
    fig.savefig(saida, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
