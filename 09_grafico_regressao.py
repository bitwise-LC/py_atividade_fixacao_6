"""Dispersão com regressão linear entre renda mensal e gasto mensal."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    dados = pd.read_csv(BASE_DIR / "data" / "dados_regressao.csv")
    x = dados["renda_mensal"].to_numpy()
    y = dados["gasto_mensal"].to_numpy()

    coeficiente_angular, intercepto = np.polyfit(x, y, 1)
    x_reta = np.linspace(x.min(), x.max(), 200)
    y_reta = coeficiente_angular * x_reta + intercepto
    r_quadrado = np.corrcoef(x, y)[0, 1] ** 2

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(
        x,
        y,
        color="#2563EB",
        alpha=0.65,
        edgecolor="white",
        label="Observações",
    )
    ax.plot(
        x_reta,
        y_reta,
        color="#DC2626",
        linewidth=2.5,
        label=f"Regressão linear (R² = {r_quadrado:.3f})",
    )
    ax.set_title("Relação entre renda mensal e gasto mensal")
    ax.set_xlabel("Renda mensal (R$)")
    ax.set_ylabel("Gasto mensal (R$)")
    ax.legend()
    ax.grid(alpha=0.25)

    fig.tight_layout()
    saida = BASE_DIR / "graficos" / "grafico_regressao.png"
    saida.parent.mkdir(exist_ok=True)
    fig.savefig(saida, dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
