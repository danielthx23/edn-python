"""
4- Analisador de Números Pares e Ímpares
Desenvolva um programa que classifica números inteiros como pares ou ímpares. O programa deve:

* Solicitar números inteiros até que o usuário digite "fim".  
* Informar se o número digitado é par ou ímpar.  
* Ao final, exibir a quantidade total de números pares e ímpares informados.  
* Tratar entradas inválidas com mensagens de erro apropriadas.  
"""

pares = 0
impares = 0

while True:
    entrada = input("\nInsira um número inteiro (ou digite 'fim' para encerrar): ")

    if entrada.lower() == 'fim':
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"\n{numero} é par.")
            pares += 1
        else:
            print(f"\n{numero} é ímpar.")
            impares += 1
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro válido.")

print(f"\nTotal de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
