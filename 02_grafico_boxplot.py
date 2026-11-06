"""Boxplot da distribuição salarial por departamento."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    dados = pd.read_csv(BASE_DIR / "data" / "dados_boxplot.csv")
    sns.set_theme(style="whitegrid")

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(
        data=dados,
        x="departamento",
        y="salario",
        hue="departamento",
        palette="Pastel1",
        legend=False,
        ax=ax,
    )
    ax.set_title("Distribuição salarial por departamento")
    ax.set_xlabel("Departamento")
    ax.set_ylabel("Salário (R$)")

    fig.tight_layout()
    saida = BASE_DIR / "graficos" / "grafico_boxplot.png"
    saida.parent.mkdir(exist_ok=True)
    fig.savefig(saida, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
