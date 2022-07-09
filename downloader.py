from pytube import Youtube
from tkinter import *
from tkinter import messagebox as Messsagebox

def accion():
    enlace = videos.get()
    videos = Youtube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download()

def popup():
    Messsagebox.showinfo("Sobre mi", "Alexis Lema")

#contruccion de la interfaz
root = Tk()
root.config(bd-15)
root.title("Youtube Downloader")

imagen = PhotoImage(file("youtube.png"))
foto = Label(root, image=imagen, bd=0)
foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu = menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Para más Información", menu=helpmenu)
helpmenu.add_command(label="Informacion del Autor", command=popup)
menubar.add_command(label="Salir", command=root.destroy)

instrucciones = Label(root, text="Programa en Python para descargar videos de Youtube\n")
instrucciones.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1,column=1)

boton = Button(root, text="Descargar", command=accion)
boton.grid(row=2,column=1)

root.mainloop()


