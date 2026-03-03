# 🐼 Análise de Dados e Business Intelligence com Pandas

Este repositório contém uma coleção de projetos práticos e scripts em Python utilizando a biblioteca **Pandas**. O foco principal é a manipulação de dados, extração de insights de negócios e cálculos de KPIs a partir de bases de dados variadas.

## 🎯 Habilidades Demonstradas
Durante o desenvolvimento destes scripts, foram aplicadas as seguintes técnicas de Data Science:
- **Importação e Limpeza de Dados:** Leitura de arquivos `.csv`.
- **Filtros e Máscaras Booleanas:** Buscas com múltiplas condições lógicas (ex: `&`, `|`).
- **Engenharia de Recursos (Feature Engineering):** Criação de novas métricas a partir de colunas existentes (ex: cálculo de médias, cálculo de lucro e comissões).
- **Agrupamentos (Group By):** Geração de relatórios agregados separando dados por categorias.
- **Funções de Agregação e Ordenação:** Uso avançado de `.sum()`, `.mean()`, `.max()`, `.min()`, `.sort_values()`, `.idxmax()` e `.idxmin()`.

## 📂 Visão Geral dos Projetos

Os scripts simulam o backend analítico de diversos sistemas e contextos do mundo real:

### 🚗 Ecossistema de Concessionárias e SaaS
Módulos focados em inteligência financeira para gestão de veículos:
* **`SaasConcessionaria.py`**: Análise de faturamento por loja e identificação da marca mais rentável utilizando `.groupby()`.
* **`fechamento.py`**: Cálculo de lucro líquido (Preço de Venda - Preço de Compra) e identificação do vendedor destaque do mês.
* **`Vendas.py`**: Cálculo automático do valor de comissão de vendedores com base no percentual individual.
* **`SistemaVeiculo.py` e `estoque.py`**: Análise descritiva de estoque, identificando veículos mais rodados, mais baratos e calculando o patrimônio total de carros vendidos.

### ⚽ IoT e Telemetria (Projeto Passa a Bola)
* **`telemetria_passaBola.py`**: Script de monitoramento de hardware. Filtra ruídos de conexão (`teste_conexao`) e calcula a média de gasto de bateria de cronômetros baseados em ESP32 durante partidas oficiais, identificando qual dispositivo apresenta a pior performance energética.

### 🎮 eSports e Entretenimento
* **`Campeonato.py`**: Lógica para encontrar o MVP de um torneio calculando a média de abates por partida.
* **`plataforma.py`**: Filtros de catálogo de streaming para encontrar os filmes de maior nota do público.
* **`carnaval.py`**: Análise de dados públicos correlacionando o número de pessoas com as taxas de incidentes e furtos, calculando percentuais de segurança.

## 🚀 Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/Kazo-Kanojo/Data_analysis_pandas.git)

2. instale o pandas:
 ```bash
    pip install pandas
