from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Gner(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.grid()
        self.widgets()

    def widgets(self):

        self.Tnombre = Label(self, text = "Pon el nombre del cliente")
        #self.Tnombre = place(x = 100, y = 200)
        #self.Tnombre.config(fg="blue", font=("Verdana", 24))
         
        #self.Tnombre.pack()
        #self.Tnombre.grid(column=10,row=8)
        


Generator = Tk() #Genero una ventana
Generator.geometry("850x500") #Le doy tamaño a la ventana
Generator.title("Reconocimientos EasyTam") #Le doy titulo
Generator.resizable(False,False) #Le doy la instruccion que no deje modificar el tamaño

#Calculator.config(cursor="pencil")
root = Gner(Generator).grid()
Generator.mainloop() #Hago que aparezca la ventana