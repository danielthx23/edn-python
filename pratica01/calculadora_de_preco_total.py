"""
4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. 
* Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3

* O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""

produtos = [{
    "nome": "Cadeira Infantil",
    "preco_unitario": 12.40,
    "quantidade": 3
},
{
    "nome": "Mesa de Jantar",
    "preco_unitario": 150.00,
    "quantidade": 1
}]

preco_total = 0

print("\nDetalhes da Compra\n---------------------------\n")

for produto in produtos:
    preco_total += produto['preco_unitario'] * produto['quantidade']   
    print(f"""Produto: {produto['nome']}
Preço Unitário: R$ {produto['preco_unitario']:.2f}
Quantidade: {produto['quantidade']}
""")

print(f"Preço Total: R$ {preco_total:.2f}")