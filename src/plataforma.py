import pandas as pd

df = pd.read_csv('../data/plataforma_streaming.csv')
print(df.to_string())

#descobrindo a nota do filme Aventuras no espaço
#primeiro é feito um filtro dentro do df para encontrar a linha do filme
filtro = df[df['titulo'] == 'Aventuras no Espaco']


#com o filtro feito nos colocamos a nota que desejamos encontrar
nota_filme = filtro['nota_publico'].values[0]

print(nota_filme)

#Objetivo descobrir o titulo. lançado em 2021, e é uma série

filtro_duplo = df[(df['tipo'] == 'Serie') & (df['ano_lancamento'] == 2021)]

titulo_filme = filtro_duplo['titulo'].values[0]

print(titulo_filme)


#Descobrindo qual o filme com a maior nota publico de toda a tabela para descobrir a categoria


filtro_filme = df[df['tipo'] == 'Filme']

nota_max_filme = filtro_filme['nota_publico'].max()

linha_melhor_filme = filtro_filme[filtro_filme['nota_publico'] == nota_max_filme]

categoria = linha_melhor_filme['categoria']

print(categoria)


