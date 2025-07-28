"""
2- Gerador de Usuário Aleatório  
Crie um programa que acessa uma API pública e exibe informações de um usuário fictício. Para isso:

* Use a API pública "https://randomuser.me/api/" para obter dados aleatórios.  
* Mostre na tela: nome completo, e-mail e país do usuário.  
* O programa deve tratar possíveis erros de conexão ou falha na API.  

Dica: Utilize o módulo `requests` para fazer a requisição e o método `.json()` para acessar os dados.
"""

import requests

def obter_usuario_aleatorio():
    try:
        response = requests.get("https://randomuser.me/api/")
        response.raise_for_status()  
        dados = response.json()
        
        usuario = dados['results'][0]
        nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        return nome_completo, email, pais
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None, None, None
    
nome_completo, email, pais = obter_usuario_aleatorio()
if nome_completo and email and pais:
    print(f"\nNome Completo: {nome_completo}")
    print(f"E-mail: {email}")
    print(f"País: {pais}")