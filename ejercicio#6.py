# Ingresa los valores del radio y la altura del cilindro
radio = float(input("Ingresa el valor del radio: "))
altura = float(input("Ingresa el valor de la altura: "))

# Calcula el área de la base del cilindro
area_base = 3.14 * radio ** 2

# Calcula el área lateral del cilindro
area_lateral = 2 * 3.14 * radio * altura

# Calcula el área total del cilindro
area_total = area_base + area_lateral

# Calcula el volumen del cilindro
volumen = area_base * altura

print(f"El área total del cilindro es: {area_total:.2f} unidades cuadradas.")
print(f"El volumen del cilindro es: {volumen:.2f} unidades cúbicas.")
