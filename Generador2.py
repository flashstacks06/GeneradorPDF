from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from PIL import Image, ImageTk
import fitz
from datetime import datetime
import sys
from tkinter import filedialog as fd

Generator = Tk() #Genero una ventana
Generator.geometry("850x500") #Le doy tamaño a la ventana
Generator.title("Reconocimientos EasyTam") #Le doy titulo

##----------------------Imagen------------------------##
Logo = Image.open("Logo.PNG")
resize_logo= Logo.resize((200,100), Image.LANCZOS)
test = ImageTk.PhotoImage(resize_logo)
label1 = Label(image=test)
label1.place(x=20, y=20)

##-----------------------Hora-------------------------##

fecha = datetime.now().strftime('%d-%m-%Y')
dia = fecha[1:3]
mes = fecha[3:5]
año = fecha[6:10]

if mes == "01": 
    mes = "Enero"

if mes == "02": 
    mes = "Febrero"

if mes == "03": 
    mes = "Marzo"

if mes == "04": 
    mes = "Abril"

if mes == "05": 
    mes = "Mayo"

if mes == "06": 
    mes = "Junio"

if mes == "07": 
    mes = "Julio"

if mes == "08": 
    mes = "Agosto"

if mes == "09": 
    mes = "Septiembre"

if mes == "10": 
    mes = "Octubre"

if mes == "11": 
    mes = "Noviembre"
    
if mes == "12": 
    mes = "Diciembre"
    
print(mes)

def direc_recoms():
    directorio = fd.askdirectory()
    print(directorio)
    return(directorio)

directorio = direc_recoms()   #Meto un retorno en una variable para poderla utilizar en el demas codigo

def pos_nombre():
    Recon = fitz.open("Reconocimiento.pdf")  # new or existing PDF
    page = Recon[0]  # new or existing page via doc[n]
    text = user_nombre.get()  #Obtengo el nombre puesto en el entry
    print(text)
    numero = len(text)
    print(numero)
    factorp_c = 718/42.5
    print(factorp_c)
    carac_p = (numero/2) * factorp_c
    print(carac_p)
    x = 359 - carac_p
    print(x)
    inicio = fitz.Point(x, 340)  # Punto desde donde se pone el texto
    user_nombre.delete(0, "end")   #Le pido que borre lo escrito en el entry
    rc = page.insert_text(inicio,  text, fontname = "helv", fontsize = 35,  rotate = 0)
    print("%i lines printed on page %i." % (rc, page.number))

    #--------Guardar como(funcion pendiente)-------#
    #nombrearch=fd.asksaveasfilename(initialdir = "/",title = "Guardar como",defaultextension='.pdf',filetypes = [("pdf files","*.pdf")] )
    #if nombrearch!='':
    #    archi1=open(nombrearch, "w", encoding="utf-8")
    #    archi1.write(rc)
    #   archi1.close()
    #    mb.showinfo("Información", "Los datos fueron guardados en el archivo.")
    Recon.save(directorio + "/" + text + "_Reconocimiento.pdf")  #Guarda archivo

#Hacer funcion para poder alinear el texto



#Logo = Label(Generator, image = "logo.png")
Tnombre = Label(Generator, text = "Pon el nombre del cliente")
Tnombre.place(x = 30, y = 140)
Tnombre.config(fg="blue", font=("Verdana", 24))

user_nombre = Entry(Generator,width = 70)
user_nombre.place(x = 30,y = 180)

btnreset=Button(Generator,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=4, text="Generar", bg="powder blue",command=pos_nombre)
btnreset.place(x=500, y=250)   

#--------Seleccion Directorio-------#

Dnombre = Label(Generator, text = "Donde guardar?")
Dnombre.place(x = 30, y = 350)
Dnombre.config(fg="blue", font=("Verdana", 15))
directorio_txt=open("directorio.txt","r")
contenido = directorio_txt.read()

if contenido != "":
    directorio == contenido
    print("yupi")
#print(contenido + "popo")
btnreset=Button(Generator, bd=5 ,fg="black",font=('ariel' ,16,'bold'),width=8, text="Examinar", bg="powder blue",command=direc_recoms)
btnreset.place(x=400, y=400)
#print(type(contenido))

if directorio != "":
    Dnombre = Label(Generator, text = directorio)
    directorio_txt=open("directorio.txt","w") 
    directorio_txt.write(directorio)
    directorio_txt.close()
    print("popo")
  
# HACER QUE LEA EL DOCUMENTO DE TEXTO PARA YA NO TENER QUE PEDIR EL DIRECTORIO


Dnombre.place(x = 30, y = 400)
Dnombre.config(fg="blue", font=("Verdana", 10))



#Calculator.config(cursor="pencil")
#root = Gner(Generator).grid()
Generator.mainloop() #Hago que aparezca la ventana