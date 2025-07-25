"""
1- Calculadora de Gorjeta
Crie um programa que calcula o valor da gorjeta a partir do total da conta e da porcentagem escolhida. Use as instruções abaixo:

* Defina o valor da conta (ex: R$ 100,00).  
* Informe a porcentagem da gorjeta (ex: 10%, 15%, 20%).  
* O programa deve calcular o valor correspondente e exibir o resultado com duas casas decimais.
"""

def calcular_gorjeta(valor_conta, porcentagem):
    return valor_conta * (porcentagem / 100)

valor_conta = float(input("Digite o valor da conta (ex: 100.00): "))
porcentagem_gorjeta = int(input("Digite a porcentagem da gorjeta (ex: 10, 15, 20): "))

gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)

print(f"\nValor da conta: R$ {valor_conta:.2f}")
print(f"Porcentagem da gorjeta: {porcentagem_gorjeta}%")
print(f"Valor da gorjeta: R$ {gorjeta:.2f}")