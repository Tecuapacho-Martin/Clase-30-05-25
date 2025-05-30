class Suma:
 def __init__(self):
    try:
        self.n1=int(input("Ingrese el primer numero"))
        self.n2=int(input("Ingrese el segundo numero"))
        self.suma=self.n1+self.n2
        print("El resultado es: ",self.suma)
    except ValueError:
       print("Error: Solo numeros enteros permitidos")
s=Suma()       
