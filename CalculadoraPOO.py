from tkinter import *
import re

raiz = Tk()


class Calculadora():
    def __init__(self, ventana):
        # Creamos una raiz en self.ventana
        self.ventana = ventana
        self.ventana.title = ("Calculadora POO")

        self.operacion = ""

        # Agregar display
        self.display = Entry(ventana, font="Arial 22")
        # Ubicar el display y estilos
        self.display.grid(row=1, column=0, columnspan=4, pady=10)
        self.display.config(bg="black",
                            fg="#00db00",
                            justify="right",
                            width=25)

        # Creación de botones. Usamos integer ya que rescataremos el texto y el valor del botón de este parámetro
        boton7 = self.colocarBoton(7)
        boton8 = self.colocarBoton(8)
        boton9 = self.colocarBoton(9)
        # Variable bool para indicar que debe mostrar o no en pantalla el simbolo de la operación
        botonDividir = self.colocarBoton("/")
        #--------------------------------------------------------------------------------------------
        boton4 = self.colocarBoton(4)
        boton5 = self.colocarBoton(5)
        boton6 = self.colocarBoton(6)
        # Variable bool para indicar que debe mostrar o no en pantalla el simbolo de la operación
        # Para el botón de multiplicar podemos usuar código unicode para representarlo.
        # Usamos una expresion regular (HAY QUE IMPORTAR re) en la funcion de pulsación
        # u"\codigoUnicode"
        botonMultiplicar = self.colocarBoton(u"\u00D7")

        #-------------solución sencialla al boton de multiplicar-------------------------------------

        #botonMultiplicar=self.colocarBoton("*")
        #botonMultiplicar.config(text="x")
        # aunque pulsemos x en pantalla saldrá *

        #--------------------------------------------------------------------------------------------
        boton1 = self.colocarBoton(1)
        boton2 = self.colocarBoton(2)
        boton3 = self.colocarBoton(3)
        # Variable bool para indicar que debe mostrar o no en pantalla el simbolo de la operación
        botonRestar = self.colocarBoton("-")
        #--------------------------------------------------------------------------------------------
        boton0 = self.colocarBoton(0)
        botonComa = self.colocarBoton(".")
        botonIgual = self.colocarBoton("=", mostrar=False)
        # Variable bool para indicar que debe mostrar o no en pantalla el simbolo de la operación
        botonSumar = self.colocarBoton("+")
        #--------------------------------------------------------------------------------------------

        botones = [
            boton7,
            boton8,
            boton9,
            botonDividir,
            boton4,
            boton5,
            boton6,
            botonMultiplicar,
            boton1,
            boton2,
            boton3,
            botonRestar,
            boton0,
            botonComa,
            botonIgual,
            botonSumar,
        ]

        contador = 0

        for fila in range(2, 6):
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna)
                contador += 1

    #creamos el métrodo colocarBoton, con mostrar=True, de esta forma será opcional. Si no le pasamos nada, lo tendrá en True
    def colocarBoton(self, valor, mostrar=True, ancho=9, alto=2):
        return Button(self.ventana,
                      text=valor,
                      width=ancho,
                      height=alto,
                      font=("Helvetica", 15),
                      command=lambda: self.pulsacionesTeclas(valor, mostrar))

    def pulsacionesTeclas(self, valor, mostrar):
        if mostrar:
            # en operacion concatenamos los valores numericos con los simbolos de operacion
            # ejemplo, pulsamos 5, +, 2 y 3, operación tendrá guardado "5+23"
            self.operacion += str(valor)
            self.mostrarPantalla(valor)
        # si pulsamos el boton del igual, se debe mantener en false
        elif not mostrar and valor == "=":
            # en el caso de la multiplicación, debe sustituir el codigo unicode por *, ANTES DE BORRAR LA PANTALLA
            # expresión regular. HAY QUE IMPORTAR re
            # re.sub(que queremos sustiuir, por lo que lo vamos a sustituir, donde lo va a guardar)
            self.operacion = re.sub(u"\u00D7", "*", self.operacion)
            # primero debemos eliminar lo que tengamos en pantalla
            self.borrarPantalla()
            # eval() evalua un string y realiza la operación que tenga dentro
            # con eval() no nos hace falta crear una función para cada operación
            self.mostrarPantalla(str(eval(self.operacion)))
        else:
            pass

    def mostrarPantalla(self, valor):
        # No hemos creado ninguna variable Stringvar(), por lo que no podmeos usar .set()
        # .insert(indice, string) Como índice podemos usar END para replicar el comportamiento de .set()
        # índice hace referencia a la posición dentro del Entry donde se coloca el string
        self.display.insert(END, valor)

    # necesitamos que antes de mostrar el resultado en pantalla, se borre lo que tiene en ese momento.
    # También servirá para el botón de C o CE
    def borrarPantalla(self):
        # .delete() permite escoger el primer o último carácter que queremos borrar
        # debemos indicar el primer carácter que borra y el último, 0, END para borrar todo
        self.display.delete(0, END)


miCalculadora = Calculadora(raiz)

raiz.mainloop()