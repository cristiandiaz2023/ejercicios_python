import math

def longitud_circunferencia(radio):
    """
    Calcula la longitud de una circunferencia dado su radio.

    Args:
    radio (float): El radio de la circunferencia.

    Returns:
    float: La longitud de la circunferencia.
    """
    return 2 * math.pi * radio

def area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Args:
    radio (float): El radio del círculo.

    Returns:
    float: El área del círculo.
    """
    return math.pi * radio ** 2

# Solicitar al usuario que ingrese el radio de la circunferencia
radio = float(input("Ingrese el radio de la circunferencia: "))

# Calcular la longitud de la circunferencia y el área del círculo
longitud = longitud_circunferencia(radio)
area = area_circulo(radio)

# Calcular el área del círculo inscrito
area_inscrito = area_circulo(radio / 2)

# Mostrar los resultados
print(f"La longitud de la circunferencia es: {longitud}")
print(f"El área del círculo es: {area}")
print(f"El área del círculo inscrito es: {area_inscrito}")

