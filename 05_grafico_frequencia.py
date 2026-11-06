"""Gráfico de frequência dos tipos de atendimento."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    dados = pd.read_csv(BASE_DIR / "data" / "dados_frequencia.csv")
    frequencias = dados["tipo_atendimento"].value_counts().sort_values()

    fig, ax = plt.subplots(figsize=(10, 6))
    barras = ax.barh(
        frequencias.index,
        frequencias.values,
        color="#F97316",
        edgecolor="white",
    )
    ax.bar_label(barras, padding=4)
    ax.set_title("Frequência dos tipos de atendimento")
    ax.set_xlabel("Quantidade de chamados")
    ax.set_ylabel("Tipo de atendimento")
    ax.set_xlim(0, frequencias.max() * 1.15)
    ax.grid(axis="x", alpha=0.25)

    fig.tight_layout()
    saida = BASE_DIR / "graficos" / "grafico_frequencia.png"
    saida.parent.mkdir(exist_ok=True)
    fig.savefig(saida, dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
