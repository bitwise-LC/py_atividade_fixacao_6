"""Gráfico de pizza da participação do faturamento por canal de venda."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    dados = pd.read_csv(BASE_DIR / "data" / "dados_pizza.csv")
    sns.set_theme(style="white")
    cores = sns.color_palette("Set2", n_colors=len(dados))

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
    fig.savefig(saida, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
