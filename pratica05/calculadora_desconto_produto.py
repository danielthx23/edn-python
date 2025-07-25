"""
3- Calculadora de Desconto em Produto
Desenvolva um programa que aplica um desconto sobre o preço de um produto. O programa deve:

* Solicitar o preço original do produto.  
* Solicitar o percentual de desconto desejado.  
* Calcular e exibir o preço final com desconto, arredondado para duas casas decimais.
"""

def calcular_desconto(preco_original, percentual_desconto):
    desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - desconto
    return round(preco_final, 2)

preco_original = float(input("Digite o preço original do produto: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

preco_final = calcular_desconto(preco_original, percentual_desconto)

print(f"\nPreço original: R$ {preco_original:.2f}")
print(f"Percentual de desconto: {percentual_desconto}%")
print(f"Preço final com desconto: R$ {preco_final:.2f}")
