import pandas as pd


#desafio descobrir o valor total de vendas
df = pd.read_csv('../data/sistema_veiculos.csv')
print(df.head())

filtro1 = df[(df["status"] == 'Vendido') & (df['loja'] == 'primeiro projeto Loja')]

total_vendas = filtro1['preco'].sum()

print(total_vendas)
#descobrir o ano do carro mais barato vendido
filtro2 = df[(df["status"] == 'Vendido') & (df['loja'] == 'Filial Sul')]

tabela_ordenada = filtro2.sort_values('preco')

ano_barato = tabela_ordenada['ano'].values[0]

print(f'O veiculo mais barato da loja FIlial Sul é do ano de {ano_barato}')

#maior quilometragem entre os carros da loja primeiro projeto loja
print()
filtro3 = df[df['loja'] == 'primeiro projeto Loja']

maior_quilometragem = filtro3['quilometragem'].max()

print(f"A maior quilometragem entre os carros vendidos ou não é de {maior_quilometragem}")