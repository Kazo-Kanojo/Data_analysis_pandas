import pandas as pd

df = pd.read_csv("fechamento.csv")
print(df.to_string())

#Encontarr o vendedor que gerou o maior lucro TOTAL apenas com os carros ja vendidos
df['lucro_total'] = df['preco_venda'] - df['preco_compra']

filtro_vendido = df[df['status'] == 'Vendido']

vendedores_lucro = filtro_vendido.groupby('vendedor')['lucro_total'].sum()

organizador = vendedores_lucro.sort_values(ascending=False)

top_vendedor = organizador.idxmax()

print()

print(top_vendedor)