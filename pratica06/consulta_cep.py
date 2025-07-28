"""
3- Consulta de CEP  
Desenvolva um programa que consulta dados de endereço a partir de um CEP brasileiro. Siga os passos abaixo:

* Solicite ao usuário que digite um CEP (apenas números, sem traço).  
* Acesse a API pública do ViaCEP: "https://viacep.com.br/ws/{cep}/json/".  
* Exiba as seguintes informações: logradouro, bairro, cidade, estado e o próprio CEP.  
* Caso o CEP não exista ou haja erro, informe isso de forma clara ao usuário.  

Dica: Use o módulo `requests` e trate exceções com `try/except`.
"""

import requests

def consultar_cep(cep):
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        response.raise_for_status()  
        
        dados = response.json()
        
        if 'erro' in dados:
            print("CEP não encontrado. Verifique o número digitado.")
            return None
        
        return {
            "logradouro": dados.get("logradouro"),
            "bairro": dados.get("bairro"),
            "cidade": dados.get("localidade"),
            "estado": dados.get("uf"),
            "cep": dados.get("cep")
        }
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None
    
cep_usuario = input("Digite o CEP (apenas números): ")
dados_cep = consultar_cep(cep_usuario)

if dados_cep:
    print("\nDados do Endereço:")
    print(f"CEP: {dados_cep['cep']}")
    print(f"Logradouro: {dados_cep['logradouro']}")
    print(f"Bairro: {dados_cep['bairro']}")
    print(f"Cidade: {dados_cep['cidade']}")
    print(f"Estado: {dados_cep['estado']}")

