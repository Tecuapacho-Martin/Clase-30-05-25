
def pedir_numero(mensaje):
    return int(input(mensaje))

def sumar(n1, n2):
    return n1 + n2

def main():
    n1 = pedir_numero("Ingrese el primer numero:")
    n2 = pedir_numero("Ingrese el segundo numero:")
    resultado = sumar(n1, n2)
    print("El resultado es: ", resultado)

main()
