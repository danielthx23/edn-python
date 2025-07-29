"""
4- Leitura e Escrita de Arquivo JSON  
Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON. Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo. Para isso:

* Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).  
* Solicite ao usuário o nome do arquivo JSON.  
* Salve os dados no arquivo usando o módulo `json`.  
* Após salvar, leia o mesmo arquivo e imprima os dados carregados.  
* Trate possíveis erros como ausência do arquivo ou problemas na escrita.

Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo.
"""

import json

def salvar_json(nome_arquivo, dados):
    try:
        with open(f'./pratica07/arquivos/{nome_arquivo}', mode='w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, indent=4)
        print(f'Dados salvos com sucesso em {nome_arquivo}')
    except Exception as e:
        print(f'Erro ao escrever o arquivo: {e}')
        
def ler_json(nome_arquivo):
    try:
        with open(f'./pratica07/arquivos/{nome_arquivo}', mode='r', encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
            print('Dados carregados do arquivo:')
            print(dados)
    except FileNotFoundError:
        print(f'Arquivo {nome_arquivo} não encontrado.')
    except Exception as e:
        print(f'Erro ao ler o arquivo: {e}')

def main():
    nome_arquivo = input('Digite o nome do arquivo JSON (ex: pessoa.json): ')
    
    dados = {
        'nome': 'Daniel',
        'idade': 19,
        'cidade': 'São Paulo'
    }
    
    salvar_json(nome_arquivo, dados)
    ler_json(nome_arquivo)

if __name__ == '__main__':
    main()