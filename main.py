import sys
from analizadorLexico import AnalizadorLexico
from tkinter import *
from tkinter import ttk

def lexico():
    
    cadena=str(my_text.get(1.0, "end"))
    analizador = AnalizadorLexico(cadena)
    
         
    # code for creating table
    
    # Imprimimos unos titulos para mejor entendimiento
    print("\n\n")
    print("Resultado del analisis lexico:")
    print('{:*<75}'.format(""))
    print('{:<30}'.format("Simbolo") + '{:<30}'.format("Tipo") + '{:<5}'.format("Codigo de Tipo"))
    i = 1
    e = Entry(resultados)
    e.insert(END, "Entrada")
    e.grid(row=0, column=0)
    e = Entry(resultados)
    e.insert(END, "Tipo")
    e.grid(row=0, column=1)
    e = Entry(resultados)
    e.insert(END, "Numero")
    e.grid(row=0, column=2)
    # Realizamos un ciclo que continue hasta que el simobolo sea un $
    while analizador.caracter != "$":
        # Analizamos el primer simbolo de la cadena
        analizador.siguienteSimbolo()
        # Imprimimos el simbolo junto al tipo de cadena
        print('{:<30}'.format(analizador.simbolo) + '{:<30}'.format(analizador.tipoCadena(analizador.tipo)) + '{:<5}'.format(str(analizador.tipo)))
        e = Entry(resultados)
        e.insert(END, analizador.simbolo)
        e.grid(row=i, column=0)
        e = Entry(resultados)
        e.insert(END, analizador.tipoCadena(analizador.tipo))
        e.grid(row=i, column=1)
        e = Entry(resultados)
        e.insert(END, str(analizador.tipo))
        e.grid(row=i, column=2)
        i+=1
    # Fin del if-else

root = Tk()
root.title('Analizador lexico')
root.geometry("500x500")


my_text = Text(root, width=50, height=10)
my_text.pack()

button_frame = Frame(root)
button_frame.pack()

clear_button = Button(button_frame, text="Lexicar", command = lexico)
clear_button.grid(row=0, column=0)

resultados = Frame(root)
resultados.pack()

# Create A Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

root.mainloop()