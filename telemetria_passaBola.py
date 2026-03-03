import pandas as pd

df = pd.read_csv('telemetria_passa_a_bola.csv')

print(df.head().to_string())

filtro = df[df['tipo_leitura'] == 'tempo_oficial']

agrupando_partidas = filtro.groupby('id_partida')['bateria_esp32_pct'].mean()

pior_media = agrupando_partidas.idxmin()


print(f"O id com a pior media é {pior_media}")






