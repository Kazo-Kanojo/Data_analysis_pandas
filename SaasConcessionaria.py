'''treinando alguns metodos do pnadas

# Conta quantos veículos existem de cada marca na coluna 'marca'

ranking_marcas = df['marca'].value_counts()
print(ranking_marcas)
=============================================================================================

# 1. Agrupar pela coluna 'loja'
# 2. Selecionar a coluna que queremos calcular ('preco')
# 3. Escolher a matemática: .sum() (soma), .mean() (média), .max() (máximo)

faturamento_por_loja = df.groupby('loja')['preco'].sum()
print(faturamento_por_loja)
============================================================================================

Ordenando o faturamento do maior para o menor
faturamento_ordenado = faturamento_por_loja.sort_values(ascending=False)

'''



import pandas as pd

df = pd.read_csv("saas_concessionarias.csv")

print(df.to_string())

#Descobrir qual marca de carro rendeu mais dinherio para ele.

filtro_vendido = df[(df['status'] == 'Vendido') & (df['nome_loja'] == 'Loja Centro')]

faturamento_por_loja = filtro_vendido.groupby('marca')['preco'].sum()

organizador = faturamento_por_loja.sort_values(ascending=False)

top_marca = organizador.idxmax()

print(f'A marca que mais vendeu da loja centro é a {top_marca}')
