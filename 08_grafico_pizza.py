"""Gráfico de pizza da participação do faturamento por canal de venda."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    dados = pd.read_csv(BASE_DIR / "data" / "dados_pizza.csv")
    cores = ["#2563EB", "#10B981", "#F59E0B", "#8B5CF6", "#EC4899"]

    fig, ax = plt.subplots(figsize=(9, 7))
    ax.pie(
        dados["faturamento"],
        labels=dados["canal_venda"],
        autopct="%1.1f%%",
        startangle=90,
        colors=cores,
        wedgeprops={"edgecolor": "white", "linewidth": 1.5},
    )
    ax.set_title("Participação do faturamento por canal de venda")
    ax.axis("equal")

    fig.tight_layout()
    saida = BASE_DIR / "graficos" / "grafico_pizza.png"
    saida.parent.mkdir(exist_ok=True)
    fig.savefig(saida, dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
