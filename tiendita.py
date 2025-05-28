 #Minitienda_tarea

nombre = input("¿Cuál es tu nombre? ")
print(f"\n¡Hola, {nombre}!")

# 2. Cálculo del IMC
peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))
imc = peso / (estatura ** 2)
print(f"\nTu índice de masa corporal es {imc:.2f}")

# 3. Venta de barras de pan
precio_original = 3.49
descuento = 0.60
precio_descuento = precio_original * (1 - descuento)

barras_vendidas = int(input("\n¿Cuántas barras de pan del día anterior has vendido? "))

total = precio_descuento * barras_vendidas

print(f"\nHas vendido {barras_vendidas} barras de pan del día anterior.")
print(f"Precio habitual por barra: {precio_original:.2f} €")
print(f"Descuento por barra: {precio_original - precio_descuento:.2f} €")
print(f"Total a pagar: {total:.2f} €")

# 4. Depósito en cuenta de ahorros
deposito_inicial = float(input("\n¿Cuánto dinero fue depositado en la cuenta de ahorros? "))

# 5. Cálculo de interés compuesto (4% anual durante 3 años)
interes = 0.04
saldo1 = deposito_inicial * (1 + interes)
saldo2 = saldo1 * (1 + interes)
saldo3 = saldo2 * (1 + interes)

print(f"\nHas depositado {deposito_inicial:.2f} € en tu cuenta de ahorros.")
print(f"Saldo después del primer año: {saldo1:.2f} €")
print(f"Saldo después del segundo año: {saldo2:.2f} €")
print(f"Saldo después del tercer año: {saldo3:.2f} €")

# 6. Resumen final
print("\n¡Gracias por usar el sistema!")
