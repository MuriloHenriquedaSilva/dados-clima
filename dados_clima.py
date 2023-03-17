import pandas as pd
from datetime import datetime


# a) Leitura do arquivo
dados = pd.read_csv('C:/Users/muril/Desktop/Dados_Clima/ArquivoDadosProjeto.csv', sep=';')
print('Dados carregados:')
print(dados)


# b) Visualização de dados de precipitação
while True:
    try:
        ano_mes = input('Digite o ano e mês desejados (yyyy-mm): ')
        ano, mes = map(int, ano_mes.split('-'))
        datetime(ano, mes, 1)  # Verifica se a data é válida
        break
    except ValueError:
        print('Data inválida. Tente novamente.')

print(f'Precipitação em {mes}/{ano}:')

for _, dado in dados.iterrows():
    data = datetime.strptime(dado['data'], '%d/%m/%Y')
    if data.year == ano and data.month == mes:
        precipitacao = dado['precip']
        print(f'{data.day}/{mes}/{ano}: {precipitacao}')


# c) Visualização de dados de temperatura
while True:
    try:
        ano_str = input('Digite o ano desejado: ')
        ano = int(ano_str)
        datetime(ano, 1, 1)  # Verifica se o ano é válido
        break
    except ValueError:
        print('Ano inválido. Tente novamente.')

primeiros_7_dias = dados[dados['data'].str.match(f'0[1-7]/\d{{2}}/{ano_str}')]
temperaturas_max = primeiros_7_dias['maxima'].tolist()
print(f'Temperatura máxima em cada um dos primeiros 7 dias de cada mês de {ano}: {temperaturas_max}')
