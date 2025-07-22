"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20   

desconto = (porcentagem_desconto / 100) * preco_original
preco_final = preco_original - desconto

print("\nCalculadora de Desconto\n---------------------------\n")
print(f"Produto: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Porcentagem de Desconto: {porcentagem_desconto}%")
print(f"Valor do Desconto: R$ {desconto:.2f}")
print(f"Preço Final: R$ {preco_final:.2f}")
print("\n---------------------------")