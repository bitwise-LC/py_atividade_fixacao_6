"""Gráfico de linhas das vendas diárias por loja."""

from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    dados = pd.read_csv(
        BASE_DIR / "data" / "dados_linhas.csv", parse_dates=["data"]
    )
    cores = {"Loja A": "#2563EB", "Loja B": "#F97316"}

    fig, ax = plt.subplots(figsize=(12, 6))
    for loja, grupo in dados.groupby("loja", sort=False):
        grupo = grupo.sort_values("data")
        ax.plot(
            grupo["data"],
            grupo["vendas"],
            marker="o",
            markersize=3,
            linewidth=1.8,
            label=loja,
            color=cores.get(loja),
        )

    ax.set_title("Evolução das vendas diárias por loja")
    ax.set_xlabel("Data")
    ax.set_ylabel("Vendas")
    ax.set_xlim(dados["data"].min(), dados["data"].max())
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=10))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))
    ax.legend(title="Loja")
    ax.grid(alpha=0.25)
    fig.autofmt_xdate()

    fig.tight_layout()
    saida = BASE_DIR / "graficos" / "grafico_linhas.png"
    saida.parent.mkdir(exist_ok=True)
    fig.savefig(saida, dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
