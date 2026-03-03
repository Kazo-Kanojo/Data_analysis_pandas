import pandas as pd

df = pd.read_csv('../data/vendas_loja.csv')
df['valor_comissao'] = df['comissao_percentual'] * df['preco_venda']

#descobrir o vendedor com a maior comisão em uma unica venda

comissao_maxima = df['valor_comissao'].max()

filtro_venda = df[df['valor_comissao'] == comissao_maxima]

vendedor_top = filtro_venda['vendedor'].values[0]

print(df.to_string())
print(vendedor_top)
