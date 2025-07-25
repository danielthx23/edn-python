"""
2- Verificador de Palíndromos
Crie um programa que verifica se uma palavra ou frase é um palíndromo, ou seja, se pode ser lida da mesma forma de trás para frente, desconsiderando espaços, acentos e pontuação. Para isso:

*Solicite ao usuário uma palavra ou frase.
*Desconsidere letras maiúsculas, espaços e sinais de pontuação.
*Verifique se a frase é um palíndromo.
*Exiba "Sim" se for palíndromo ou "Não" se não for.

Exemplo: A frase "A cara rajada da jararaca" deve ser reconhecida como um palíndromo.
"""

def verificar_palindromo(frase):
    frase = ''.join(caractere.lower() for caractere in frase if caractere.isalnum())
    esquerda = 0 
    direita = len(frase) - 1

    while esquerda < direita:
        if frase[esquerda] != frase[direita]:
            return False
        esquerda += 1
        direita -= 1

    return True

s = input("\nDigite uma palavra ou frase: ")

if verificar_palindromo(s):
    print("\nSim")
else:
    print("\nNão")