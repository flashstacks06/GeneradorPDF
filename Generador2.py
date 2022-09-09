from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import fitz

Generator = Tk() #Genero una ventana
Generator.geometry("850x500") #Le doy tamaño a la ventana
Generator.title("Reconocimientos EasyTam") #Le doy titulo

##----------------------Imagen------------------------##
Logo = Image.open("Logo.PNG")
resize_logo= Logo.resize((200,100), Image.LANCZOS)
test = ImageTk.PhotoImage(resize_logo)
label1 = Label(image=test)
label1.place(x=20, y=20)

def pos_nombre():
    Recon = fitz.open("Reconocimiento.pdf")  # new or existing PDF
    page = Recon[0]  # new or existing page via doc[n]
    inicio = fitz.Point(450, 300)  # start point of 1st line
    text = user_nombre.get()  #Obtengo el nombre puesto en el entry
    print(text)
    user_nombre.delete(0, "end")   #Le pido que borre lo escrito en el entry
    rc = page.insert_text(inicio,  text, fontname = "helv", fontsize = 24,  rotate = 0)
    print("%i lines printed on page %i." % (rc, page.number))
    Recon.save("text.pdf")


    #Hacer funcion para poder alinear el texto



#Logo = Label(Generator, image = "logo.png")
Tnombre = Label(Generator, text = "Pon el nombre del cliente")
Tnombre.place(x = 30, y = 140)
Tnombre.config(fg="blue", font=("Verdana", 24))

user_nombre = Entry(Generator,width = 70)
user_nombre.place(x = 30,y = 180)

btnreset=Button(Generator,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=4, text="Generar", bg="powder blue",command=pos_nombre)
btnreset.place(x=500, y=250)   




#Calculator.config(cursor="pencil")
#root = Gner(Generator).grid()
Generator.mainloop() #Hago que aparezca la ventana