import tkinter as tk
class TrianguloApp:
    def __init__(self, ventana):
        self.ventana = ventana
   

        self.etiqueta1 = tk.Label(ventana, text="Ingrese la base:")
        self.etiqueta1.pack()

        self.entrada1 = tk.Entry(ventana)
        self.entrada1.pack()

        self.etiqueta2 = tk.Label(ventana, text="Ingrese la altura:")
        self.etiqueta2.pack()

        self.entrada2 = tk.Entry(ventana)
        self.entrada2.pack()

        self.boton = tk.Button(ventana, text="Calcular Área", command=self.calcular_area)
        self.boton.pack()

        self.resultado_label = tk.Label(ventana, text="")
        self.resultado_label.pack()

    def calcular_area(self):
        try:
            base = float(self.entrada1.get())
            altura = float(self.entrada2.get())
            area = (base * altura) / 2
            self.resultado_label.config(text="El área del triángulo es: " + str(area))
        except ValueError:
            self.resultado_label.config(text="Error: Solo números válidos permitidos")
ventana=tk.Tk()
ventana.title("Area del triangulo")
app = TrianguloApp(ventana)

ventana.mainloop()
