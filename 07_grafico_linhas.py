"""Gráfico de linhas das vendas diárias por loja."""

from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    dados = pd.read_csv(
        BASE_DIR / "data" / "dados_linhas.csv", parse_dates=["data"]
    )
    sns.set_theme(style="whitegrid")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(
        data=dados.sort_values("data"),
        x="data",
        y="vendas",
        hue="loja",
        style="loja",
        markers=True,
        dashes=False,
        palette="Set2",
        linewidth=2,
        ax=ax,
    )

    ax.set_title("Evolução das vendas diárias por loja")
    ax.set_xlabel("Data")
    ax.set_ylabel("Vendas")
    ax.set_xlim(dados["data"].min(), dados["data"].max())
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=10))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))
    ax.legend(title="Loja")
    fig.autofmt_xdate()

    fig.tight_layout()
    saida = BASE_DIR / "graficos" / "grafico_linhas.png"
    saida.parent.mkdir(exist_ok=True)
    fig.savefig(saida, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
