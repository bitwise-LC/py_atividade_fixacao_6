"""Gráfico de dispersão entre altura e peso, separado por sexo."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    dados = pd.read_csv(BASE_DIR / "data" / "dados_dispersao.csv")
    sns.set_theme(style="whitegrid")

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(
        data=dados,
        x="altura_cm",
        y="peso_kg",
        hue="sexo",
        style="sexo",
        palette="Set2",
        s=70,
        alpha=0.8,
        ax=ax,
    )
    sns.regplot(
        data=dados,
        x="altura_cm",
        y="peso_kg",
        scatter=False,
        color="gray",
        line_kws={"linestyle": "--", "linewidth": 1.8},
        ax=ax,
    )

    ax.set_title("Relação entre altura e peso")
    ax.set_xlabel("Altura (cm)")
    ax.set_ylabel("Peso (kg)")
    ax.legend(title="Sexo")

    fig.tight_layout()
    saida = BASE_DIR / "graficos" / "grafico_dispersao.png"
    saida.parent.mkdir(exist_ok=True)
    fig.savefig(saida, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
