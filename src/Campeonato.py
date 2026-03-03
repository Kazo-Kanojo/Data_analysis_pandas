import pandas as pd

df = pd.read_csv('../data/campeonato_esports.csv')

#Objetivo encontrar o jogador com a maior media de abates.

df['media_abates'] = df['total_abates'] / df['partidas_jogadas']

maior_media = df['media_abates'].max()

#FILTRO PARA ENCONTRAR A MAIOR MEDIA
filtro = df[df['media_abates'] == maior_media]

#PASSANDO O FILTRO PARA ENCONTARR A MAIOR MEDIA ENTRE OS JOGADORES
top_player = filtro['jogador'].values[0]


print(df.to_string())
print(top_player)
