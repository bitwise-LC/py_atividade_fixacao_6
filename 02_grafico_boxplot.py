"""Boxplot da distribuição salarial por departamento."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    dados = pd.read_csv(BASE_DIR / "data" / "dados_boxplot.csv")
    departamentos = dados["departamento"].drop_duplicates().tolist()
    salarios = [
        dados.loc[dados["departamento"] == departamento, "salario"]
        for departamento in departamentos
    ]

    fig, ax = plt.subplots(figsize=(10, 6))
    caixas = ax.boxplot(
        salarios,
        tick_labels=departamentos,
        patch_artist=True,
        medianprops={"color": "#991B1B", "linewidth": 2},
    )
    cores = ["#93C5FD", "#6EE7B7", "#FCD34D", "#C4B5FD"]
    for caixa, cor in zip(caixas["boxes"], cores):
        caixa.set_facecolor(cor)

    ax.set_title("Distribuição salarial por departamento")
    ax.set_xlabel("Departamento")
    ax.set_ylabel("Salário (R$)")
    ax.grid(axis="y", alpha=0.25)

    fig.tight_layout()
    saida = BASE_DIR / "graficos" / "grafico_boxplot.png"
    saida.parent.mkdir(exist_ok=True)
    fig.savefig(saida, dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
