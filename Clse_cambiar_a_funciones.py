
def pedir_base():
    return float(input("Ingrese la base del triangulo: "))

def pedir_altura():
    return float(input("Ingrese la altura del triangulo: "))

def calcular_area(base, altura):
    return base * altura / 2

def mostrar_area(area):
    print("El area del triangulo es: ", area)

def main():
    base = pedir_base()
    altura = pedir_altura()
    area = calcular_area(base, altura)
    mostrar_area(area)

main()
