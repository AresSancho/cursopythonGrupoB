'''
ejemplo de un juego basado en una aplicacion
de ventanas con python tkinter.
Para mostrar un ejemplo sobre eventos
y diferentes componentes visuales.
'''
from tkinter import *
#tkinter esta disponible por defecto en python
#otro recurso muy usado es pyQt5
x = 0
y = 0
def click_raton(evento):
    global x, y
    #se pone global para poder usar las variables 
    #x e y definidas fuera de la funcion
    x = evento.x
    y = evento.y
    print("x: " + str(x))
    print("y: " + str(y))
    if x >= 746 and x <= 805 and y >= 167 and y <= 228 :
        print("FELICIDADES ADIVINASTE LA PRIMERA DIFERENCIA")
    elif x >= 600 and x <= 664 and y >= 48 and y <= 109:
        print("FELICIDADES ADIVINASTE LA SEGUNDA")
    else:
        print("NO HAS ADIVINADO UNA DIFERENCIA")    
    
#end click_raton
ventana = Tk()
canvas = Canvas(ventana, width = 800, height = 600)
canvas.pack(expand = YES, fill = BOTH )
imagen = PhotoImage(file="imagen.png")
canvas.create_image(0,0,image = imagen, anchor = NW)

ventana.geometry("930x360")
ventana.title("PINCHA PARA ADIVINAR LAS DIFERENCIAS A LA DERECHA")
ventana.bind("<Button 1>",click_raton)

ventana.mainloop()












    

    
    
    
    
    
    
    
    
    
    
    
    
    

