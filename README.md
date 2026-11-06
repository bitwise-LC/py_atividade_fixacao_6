# Atividade de Fixação 06 — Gráficos

Este projeto contém um script independente para cada arquivo CSV fornecido na
atividade. Todos os scripts utilizam caminhos relativos à própria pasta, exibem
o gráfico e salvam uma cópia em PNG dentro de `graficos/`.

## Gráficos criados

| Script | Arquivo de dados | Visualização |
|---|---|---|
| `01_grafico_barras.py` | `dados_barras.csv` | Barras agrupadas por categoria e região |
| `02_grafico_boxplot.py` | `dados_boxplot.csv` | Distribuição salarial por departamento |
| `03_grafico_dispersao.py` | `dados_dispersao.csv` | Altura × peso, separado por sexo |
| `04_grafico_distribuicao.py` | `dados_distribuicao.csv` | Histograma de idade |
| `05_grafico_frequencia.py` | `dados_frequencia.csv` | Frequência de tipos de atendimento |
| `06_grafico_heatmap.py` | `dados_heatmap.csv` | Movimento por dia e horário |
| `07_grafico_linhas.py` | `dados_linhas.csv` | Evolução das vendas por loja |
| `08_grafico_pizza.py` | `dados_pizza.csv` | Faturamento por canal |
| `09_grafico_regressao.py` | `dados_regressao.csv` | Dispersão com regressão linear |

## Preparação do ambiente

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Execução

Cada gráfico pode ser executado separadamente. Exemplo:

```bash
python 01_grafico_barras.py
python 02_grafico_boxplot.py
python 03_grafico_dispersao.py
```

Repita o comando para os demais scripts. Os nove PNGs resultantes ficarão na
pasta `graficos/`, prontos para conferência e inclusão no repositório do GitHub.
