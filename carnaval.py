import pandas as pd

df = pd.read_csv('carnaval_seguranca.csv')

filtro = df[df['bloco'] == 'Solteiros e Casados']

coluna_furto = filtro['furtos_celular']
coluna_publico = filtro['publico_estimado']

porcentagem_furto_celular = coluna_furto.values[0] / coluna_publico.values[0] * 100

print(f'A procentagem de furto de celulares é {porcentagem_furto_celular}%')

#Descobrindo valor maximo e minimo
publico_max = df['publico_estimado'].max()
publico_min = df['publico_estimado'].min()

# descobrindo o bloco com o maior publico
filtro_max = df[df['publico_estimado'] == publico_max]

nome_bloco_max = filtro_max['bloco'].values[0]
print(nome_bloco_max)

#Zona com o menor numero de carteiras
furtos_min = df['furtos_carteira'].min()

filtro_furto_min = df[df['furtos_carteira'] == furtos_min]

zona_menor_furto = filtro_furto_min['zona'].values[0]

print(zona_menor_furto)
