import pandas as pd
import json

# Carregando os dados do arquivo JSON (Extract)
with open('dados_clientes.json', 'r') as file:
    data = json.load(file)

# Adicionando mensagens aos clientes (Transform)
for key, cliente in data.items():
    cliente['Mensagem'] = f'Oi, {cliente["Nome"]} Sabia que seus investimentos podem mudar seu futuro financeiro? Seu saldo de investimentos atual: {cliente["SaldoInvestimentos"]}R$, invista.'

# Convertendo de volta para JSON
json_data = json.dumps(data, indent=2)

# Salvando os dados atualizados em um novo arquivo JSON (Loading)
with open('clientes_com_mensagem.json', 'w') as output_file:
    output_file.write(json_data)
