"""
4- Conversor de Moedas (para Reais - BRL)  
Crie um programa que mostra a cotação atual de moedas estrangeiras em relação ao Real. O programa deve:

* Solicitar ao usuário o código da moeda estrangeira (ex: USD, EUR, GBP).  
* Acessar a API: "https://economia.awesomeapi.com.br/last/{moeda}-BRL".  
* Exibir a cotação atual, o valor máximo, o valor mínimo e a data/hora da última atualização.  
* Informar ao usuário se o código da moeda for inválido ou houver falha na conexão.  

Dica: A conversão da data/hora pode ser feita com o módulo `datetime`.
"""

import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY_AWESOME_API = os.getenv("API_KEY_AWESOME_API")

def consultar_cotacao(moeda):
    try:
        url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL?token={API_KEY_AWESOME_API}"
        response = requests.get(url)
        response.raise_for_status()
        
        dados = response.json()
        par_moeda = f"{moeda}BRL"

        if par_moeda not in dados:
            print("Código da moeda inválido. Verifique o código digitado.")
            return None
        
        cotacao = dados[par_moeda]
        return {
            "cotacao": float(cotacao['bid']),
            "maximo": float(cotacao['high']),
            "minimo": float(cotacao['low']),
            "data_hora": datetime.strptime(cotacao['create_date'], '%Y-%m-%d %H:%M:%S')
        }
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None

moeda_usuario = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").upper()

cotacao_moeda = consultar_cotacao(moeda_usuario)

if cotacao_moeda:
    print("\nCotação da Moeda:")
    print(f"Cotação Atual: R$ {cotacao_moeda['cotacao']:.2f}")
    print(f"Valor Máximo: R$ {cotacao_moeda['maximo']:.2f}")
    print(f"Valor Mínimo: R$ {cotacao_moeda['minimo']:.2f}")
    print(f"Última Atualização: {cotacao_moeda['data_hora'].strftime('%d/%m/%Y %H:%M:%S')}")
else:
    print("Não foi possível obter a cotação da moeda.")
