"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

temperatura = float(input("\nInsira a temperatura: "))
unidade_origem = input("Unidade de destino (C para Celsius, F para Fahrenheit, K para Kelvin): ")
unidade_destino = input("Unidade de destino (C para Celsius, F para Fahrenheit, K para Kelvin): ")
temperatura_convertida = 0

if unidade_origem.upper() == 'C':
    if unidade_destino.upper() == 'F':
        temperatura_convertida = (temperatura * 9/5) + 32
    elif unidade_destino.upper() == 'K':
        temperatura_convertida = temperatura + 273.15
    else:
        print("Unidade de destino inválida.")
elif unidade_origem.upper() == 'F':
    if unidade_destino.upper() == 'C':
        temperatura_convertida = (temperatura - 32) * 5/9
    elif unidade_destino.upper() == 'K':
        temperatura_convertida = (temperatura - 32) * 5/9 + 273.15
    else:
        print("Unidade de destino inválida.")
elif unidade_origem.upper() == 'K':
    if unidade_destino.upper() == 'C':
        temperatura_convertida = temperatura - 273.15
    elif unidade_destino.upper() == 'F':
        temperatura_convertida = (temperatura - 273.15) * 9/5 + 32
    else:
        print("Unidade de destino inválida.")

print("\nConversor de Temperatura\n---------------------------")
print(f"Temperatura: {temperatura:.2f}° {unidade_origem.upper()}")
print(f"Temperatura convertida: {temperatura_convertida:.2f}° {unidade_destino.upper()}")