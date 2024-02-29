# Tipo de cambio actual de euros a dólares
tipo_de_cambio = 1.08
# Solicitar al usuario la cantidad en euros
euros = float(input("Ingrese la cantidad de euros a covertir: "))
#Convertimos euros a dolares
dolares = euros * tipo_de_cambio
#Mostrar el resultado
print(f"{euros} euros son {dolares} dolares")