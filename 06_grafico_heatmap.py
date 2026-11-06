"""Heatmap do movimento de clientes por dia e horário."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


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
    tabela = dados.pivot(
        index="dia_semana", columns="horario", values="movimento_clientes"
    ).reindex(ORDEM_DIAS)

    fig, ax = plt.subplots(figsize=(11, 6))
    imagem = ax.imshow(tabela, cmap="YlOrRd", aspect="auto")
    ax.set_xticks(range(len(tabela.columns)), labels=tabela.columns)
    ax.set_yticks(range(len(tabela.index)), labels=tabela.index)
    ax.set_title("Movimento de clientes por dia e horário")
    ax.set_xlabel("Horário")
    ax.set_ylabel("Dia da semana")

    limite_cor = tabela.to_numpy().max() * 0.55
    for linha in range(tabela.shape[0]):
        for coluna in range(tabela.shape[1]):
            valor = tabela.iloc[linha, coluna]
            ax.text(
                coluna,
                linha,
                f"{valor:.0f}",
                ha="center",
                va="center",
                color="white" if valor > limite_cor else "#111827",
                fontsize=9,
            )

    barra_cor = fig.colorbar(imagem, ax=ax)
    barra_cor.set_label("Movimento de clientes")
    fig.tight_layout()

    saida = BASE_DIR / "graficos" / "grafico_heatmap.png"
    saida.parent.mkdir(exist_ok=True)
    fig.savefig(saida, dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
