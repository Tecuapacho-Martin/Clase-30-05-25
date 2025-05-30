import tkinter as tk

class Suma:
    def __init__(self, ventana):
        self.etiqueta1 = tk.Label(ventana, text="Ingrese el primer numero:")
        self.etiqueta1.pack()

        self.entrada1 = tk.Entry(ventana)
        self.entrada1.pack()

        self.etiqueta2 = tk.Label(ventana, text="Ingrese el segundo numero:")
        self.etiqueta2.pack()

        self.entrada2 = tk.Entry(ventana)
        self.entrada2.pack()

        self.boton = tk.Button(ventana, text="Calcular Suma", command=self.calcular_suma)
        self.boton.pack()

        self.resultado_label = tk.Label(ventana, text="")
        self.resultado_label.pack()

    def calcular_suma(self):
        try:
            n1 = int(self.entrada1.get())
            n2 = int(self.entrada2.get())
            suma = n1 + n2
            self.resultado_label.config(text="El resultado es: " + str(suma))
        except ValueError:
            self.resultado_label.config(text="Error: Solo numeros enteros permitidos")

   
ventana = tk.Tk()
ventana.title("Suma")
app = Suma(ventana)
ventana.mainloop()
  
