# EStudos para a proxima aula. seguindo a visao que o professor passou no teams.
import pandas as pd

arquivo = "./estoque_loja.csv"

df = pd.read_csv(arquivo)

filtro_duplo = df[(df['marca'] == 'Volkswagen') & (df['status'] == 'Disponível')]

coluna_quilometragem = filtro_duplo['quilometragem']

print(coluna_quilometragem.values[0])