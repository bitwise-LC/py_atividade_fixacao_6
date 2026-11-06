"""Gráfico de barras agrupadas das vendas médias por categoria e região."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    dados = pd.read_csv(BASE_DIR / "data" / "dados_barras.csv")
    sns.set_theme(style="whitegrid")

    fig, ax = plt.subplots(figsize=(11, 6))
    sns.barplot(
        data=dados,
        x="categoria",
        y="vendas_medias",
        hue="regiao",
        palette="Set2",
        errorbar=None,
        ax=ax,
    )
    ax.set_title("Vendas médias por categoria e região")
    ax.set_xlabel("Categoria")
    ax.set_ylabel("Vendas médias")
    ax.legend(title="Região", ncols=2)

    fig.tight_layout()
    saida = BASE_DIR / "graficos" / "grafico_barras.png"
    saida.parent.mkdir(exist_ok=True)
    fig.savefig(saida, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
