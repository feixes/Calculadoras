from tkinter import *

root = Tk()
miFrame = Frame(root)
miFrame.pack()

digitoDisplay = StringVar()
operacion = ""
guardarOperacion = ""
resultado = 0
coma = False

digitoDisplay.set("0")

display = Entry(miFrame, textvariable=digitoDisplay, font="Arial 15")
# columnspan para indicar que debe ocupar 3 columnas.
# también se puede crear con 2 frames
display.grid(row=1, column=1, columnspan=4, pady=10)
display.config(bg="black", fg="#00db00", justify="right", width=15)
#----------------funcion alternativa coma------


def pulsacionComa():
    contador = 0

    for i in digitoDisplay.get():
        if i == ".":
            contador += 1

    if contador == 0:
        digitoDisplay.set(digitoDisplay.get() + ".")


#---------------pulsaciones teclas-------


# si añadimos un parámetro, al iniciar el programa se pone por defecto el valor del parametro
# en el command se lo devemos pasar como una función lambda
def pulsacionesTeclas(numPulsado):
    global operacion, guardarOperacion, coma
    if operacion != "":
        digitoDisplay.set(numPulsado)
        guardarOperacion = operacion
        operacion = ""
    else:
        if numPulsado == "0" and digitoDisplay.get() == "0":
            digitoDisplay.set("0")
        elif numPulsado == "." and digitoDisplay.get() == "0":
            digitoDisplay.set(digitoDisplay.get() + numPulsado)
            coma = True
        elif numPulsado != "0" and digitoDisplay.get() == "0":
            digitoDisplay.set(numPulsado)
        # elif numPulsado == "." and coma == False:
        #     digitoDisplay.set(digitoDisplay.get() + numPulsado)
        #     coma = True
        else:
            digitoDisplay.set(digitoDisplay.get() + numPulsado)
        # elif coma == True and numPulsado != ".":
        #     digitoDisplay.set(digitoDisplay.get() + numPulsado)
        # elif numPulsado != "." and coma == False:
        #     digitoDisplay.set(digitoDisplay.get() + numPulsado)


#------------operaciones----------------


def igual():
    global guardarOperacion, resultado
    if guardarOperacion == "suma":
        if (resultado + float(digitoDisplay.get())).is_integer():
            digitoDisplay.set(int(float(digitoDisplay.get()) + resultado))
        else:
            digitoDisplay.set(float(digitoDisplay.get()) + resultado)
    if guardarOperacion == "resta":
        if (resultadoResta - float(digitoDisplay.get())).is_integer():
            digitoDisplay.set(resultadoResta - int(float(digitoDisplay.get())))
        else:
            digitoDisplay.set(resultadoResta - float(digitoDisplay.get()))
    if guardarOperacion == "mult":
        if (resultadoMult * float(digitoDisplay.get())).is_integer():
            digitoDisplay.set(int(float(digitoDisplay.get()) * resultadoMult))
        else:
            digitoDisplay.set(float(digitoDisplay.get()) * resultadoMult)
    if guardarOperacion == "division":
        if (resultadoDiv / float(digitoDisplay.get())).is_integer():
            digitoDisplay.set(resultadoDiv / int(float(digitoDisplay.get())))
        else:
            digitoDisplay.set(resultadoDiv / float(digitoDisplay.get()))
    resultado = 0


def suma(num):
    # global porque estamos usando una variable fuera de la función
    global operacion, resultado
    operacion = "suma"
    resultado += float(num)
    if resultado.is_integer():
        digitoDisplay.set(int(resultado))
    else:
        digitoDisplay.set(resultado)


resultadoResta = 0
numRestas = 0


def resta(num):
    # global porque estamos usando una variable fuera de la función
    global operacion, resultadoResta, numRestas
    operacion = "resta"
    if numRestas != 0:
        resultadoResta -= float(num)
    else:
        resultadoResta = float(num)
    if resultadoResta.is_integer():
        digitoDisplay.set(int(resultadoResta))
    else:
        digitoDisplay.set(resultadoResta)
    numRestas += 1


resultadoMult = 1


def multiplicacion(num):
    # global porque estamos usando una variable fuera de la función
    global operacion, resultadoMult
    operacion = "mult"
    resultadoMult *= float(num)
    if resultadoMult.is_integer():
        digitoDisplay.set(int(resultadoMult))
    else:
        digitoDisplay.set(resultadoMult)


resultadoDiv = 1

denominador = 1
numDivisiones = 0


def division(num):
    # global porque estamos usando una variable fuera de la función
    global operacion, resultadoDiv, denominador, numDivisiones
    operacion = "division"
    if numDivisiones != 0:
        resultadoDiv = float(resultadoDiv) / float(num)
    else:
        resultadoDiv = float(num) / 1

    if resultadoDiv.is_integer():
        digitoDisplay.set(int(resultadoDiv))
    else:
        digitoDisplay.set(resultadoDiv)

    numDivisiones += 1


#-----------primera fila--------------

#para las pulsaciones de tecla en los botones, debemos usar funciones lambda.
#si no se usa, se ejecuta directamente la función y no se puede volver a usar
#el constructor de la clase button, no permite que en la clase command se pasen parámetros

boton7 = Button(miFrame,
                text="7",
                width=5,
                command=lambda: pulsacionesTeclas("7"))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame,
                text="8",
                width=5,
                command=lambda: pulsacionesTeclas("8"))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame,
                text="9",
                width=5,
                command=lambda: pulsacionesTeclas("9"))
boton9.grid(row=2, column=3)
botondiv = Button(miFrame,
                  text="/",
                  width=5,
                  command=lambda: division(digitoDisplay.get()))
botondiv.grid(row=2, column=4)

#-----------segunda fila--------------

boton4 = Button(miFrame,
                text="4",
                width=5,
                command=lambda: pulsacionesTeclas("4"))
boton4.grid(row=3, column=1)
boton5 = Button(miFrame,
                text="5",
                width=5,
                command=lambda: pulsacionesTeclas("5"))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame,
                text="6",
                width=5,
                command=lambda: pulsacionesTeclas("6"))
boton6.grid(row=3, column=3)
botonmult = Button(miFrame,
                   text="x",
                   width=5,
                   command=lambda: multiplicacion(digitoDisplay.get()))
botonmult.grid(row=3, column=4)

#-----------tercera fila--------------

boton1 = Button(miFrame,
                text="1",
                width=5,
                command=lambda: pulsacionesTeclas("1"))
boton1.grid(row=4, column=1)
boton2 = Button(miFrame,
                text="2",
                width=5,
                command=lambda: pulsacionesTeclas("2"))
boton2.grid(row=4, column=2)
boton3 = Button(miFrame,
                text="3",
                width=5,
                command=lambda: pulsacionesTeclas("3"))
boton3.grid(row=4, column=3)
botonresta = Button(miFrame,
                    text="-",
                    width=5,
                    command=lambda: resta(digitoDisplay.get()))
botonresta.grid(row=4, column=4)

#-----------cuarta fila--------------

boton0 = Button(miFrame,
                text="0",
                width=5,
                command=lambda: pulsacionesTeclas("0"))
boton0.grid(row=5, column=1)
botoncoma = Button(miFrame, text=".", width=5, command=lambda: pulsacionComa())
botoncoma.grid(row=5, column=2)
botonsuma = Button(miFrame,
                   text="+",
                   width=5,
                   command=lambda: suma(digitoDisplay.get()))
botonsuma.grid(row=5, column=3)
botonigual = Button(miFrame, text="=", width=5, command=lambda: igual())
botonigual.grid(row=5, column=4)

root.mainloop()
