"""
1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o 
em uma das seguintes categorias: 

*Criança (0-12 anos), 
*Adolescente (13-17 anos), 
*Adulto (18-59 anos) ou 
*Idoso (60 anos ou mais).
"""

idade = int(input("\nInsira sua idade: "))
categoria = ""

if idade > 0 and idade <= 12:
    categoria = "Criança"
elif idade >= 13 and idade <= 17:
    categoria = "Adolescente"
elif idade >= 18 and idade <= 59:
    categoria = "Adulto"
elif idade >= 60:
    categoria = "Idoso"
else:
    print("\nIdade inválida. Por favor, insira uma idade positiva.")
    exit()

print(f"\nClassificação de Idade\n---------------------------")
print(f"Idade: {idade} anos")
print(f"Categoria: {categoria}")