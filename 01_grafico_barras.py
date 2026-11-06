"""Gráfico de barras agrupadas das vendas médias por categoria e região."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    dados = pd.read_csv(BASE_DIR / "data" / "dados_barras.csv")
    tabela = dados.pivot(
        index="categoria", columns="regiao", values="vendas_medias"
    )

    fig, ax = plt.subplots(figsize=(11, 6))
    tabela.plot(
        kind="bar",
        ax=ax,
        color=["#2563EB", "#10B981", "#F59E0B", "#8B5CF6"],
        edgecolor="white",
    )
    ax.set_title("Vendas médias por categoria e região")
    ax.set_xlabel("Categoria")
    ax.set_ylabel("Vendas médias")
    ax.tick_params(axis="x", rotation=0)
    ax.legend(title="Região", ncols=2)
    ax.grid(axis="y", alpha=0.25)

    fig.tight_layout()
    saida = BASE_DIR / "graficos" / "grafico_barras.png"
    saida.parent.mkdir(exist_ok=True)
    fig.savefig(saida, dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
