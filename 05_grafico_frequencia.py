"""Gráfico de frequência dos tipos de atendimento."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    dados = pd.read_csv(BASE_DIR / "data" / "dados_frequencia.csv")
    sns.set_theme(style="whitegrid")
    ordem = dados["tipo_atendimento"].value_counts().index

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(
        data=dados,
        y="tipo_atendimento",
        order=ordem,
        hue="tipo_atendimento",
        palette="Blues_r",
        legend=False,
        ax=ax,
    )
    for conjunto in ax.containers:
        ax.bar_label(conjunto, padding=4)
    ax.set_title("Frequência dos tipos de atendimento")
    ax.set_xlabel("Quantidade de chamados")
    ax.set_ylabel("Tipo de atendimento")
    ax.set_xlim(0, dados["tipo_atendimento"].value_counts().max() * 1.15)

    fig.tight_layout()
    saida = BASE_DIR / "graficos" / "grafico_frequencia.png"
    saida.parent.mkdir(exist_ok=True)
    fig.savefig(saida, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
