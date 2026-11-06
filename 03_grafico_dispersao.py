"""Gráfico de dispersão entre altura e peso, separado por sexo."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    dados = pd.read_csv(BASE_DIR / "data" / "dados_dispersao.csv")
    cores = {"Feminino": "#EC4899", "Masculino": "#2563EB"}

    fig, ax = plt.subplots(figsize=(10, 6))
    for sexo, grupo in dados.groupby("sexo", sort=False):
        ax.scatter(
            grupo["altura_cm"],
            grupo["peso_kg"],
            label=sexo,
            color=cores.get(sexo, "#64748B"),
            alpha=0.75,
            edgecolor="white",
            s=55,
        )

    ax.set_title("Relação entre altura e peso")
    ax.set_xlabel("Altura (cm)")
    ax.set_ylabel("Peso (kg)")
    ax.legend(title="Sexo")
    ax.grid(alpha=0.25)

    fig.tight_layout()
    saida = BASE_DIR / "graficos" / "grafico_dispersao.png"
    saida.parent.mkdir(exist_ok=True)
    fig.savefig(saida, dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
