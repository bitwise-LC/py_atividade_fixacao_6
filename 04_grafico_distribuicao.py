"""Histograma da distribuição de idade dos clientes."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    dados = pd.read_csv(BASE_DIR / "data" / "dados_distribuicao.csv")

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(
        dados["idade"],
        bins=12,
        color="#14B8A6",
        edgecolor="white",
        linewidth=1.2,
    )
    ax.axvline(
        dados["idade"].mean(),
        color="#DC2626",
        linestyle="--",
        linewidth=2,
        label=f"Média: {dados['idade'].mean():.1f} anos",
    )
    ax.set_title("Distribuição de idade dos clientes")
    ax.set_xlabel("Idade")
    ax.set_ylabel("Quantidade de clientes")
    ax.legend()
    ax.grid(axis="y", alpha=0.25)

    fig.tight_layout()
    saida = BASE_DIR / "graficos" / "grafico_distribuicao.png"
    saida.parent.mkdir(exist_ok=True)
    fig.savefig(saida, dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
