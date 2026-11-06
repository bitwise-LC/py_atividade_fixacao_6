"""Heatmap do movimento de clientes por dia e horário."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


BASE_DIR = Path(__file__).resolve().parent
ORDEM_DIAS = [
    "Segunda",
    "Terça",
    "Quarta",
    "Quinta",
    "Sexta",
    "Sábado",
    "Domingo",
]


def main() -> None:
    dados = pd.read_csv(BASE_DIR / "data" / "dados_heatmap.csv")
    sns.set_theme(style="white")
    tabela = dados.pivot(
        index="dia_semana", columns="horario", values="movimento_clientes"
    ).reindex(ORDEM_DIAS)

    fig, ax = plt.subplots(figsize=(11, 6))
    sns.heatmap(
        tabela,
        annot=True,
        fmt="d",
        cmap="YlOrRd",
        linewidths=0.5,
        cbar_kws={"label": "Movimento de clientes"},
        ax=ax,
    )
    ax.set_title("Movimento de clientes por dia e horário")
    ax.set_xlabel("Horário")
    ax.set_ylabel("Dia da semana")
    fig.tight_layout()

    saida = BASE_DIR / "graficos" / "grafico_heatmap.png"
    saida.parent.mkdir(exist_ok=True)
    fig.savefig(saida, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
