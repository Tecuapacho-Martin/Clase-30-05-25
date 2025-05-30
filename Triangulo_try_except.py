
class Triangulo:
    def pedir_datos(self):
        try:
         self.base=float(input("Ingrese la base del triangulo: "))
         self.altura=float(input("Ingrese la altura del triangulo: "))
         self.area=self.base*self.altura/2
         print("El area del triangulo es: ", self.area)
        except ValueError:
            print("Ingrese numeros, no letras o caracteres")
s=Triangulo()
s.pedir_datos()
