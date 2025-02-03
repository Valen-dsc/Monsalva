from multiprocessing import Value
from pydoc import text
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import scrolledtext
from PIL import Image, ImageTk

a = 1
b = 1
c = 1
d = 1
e = 1
f = 1 
g = 1
h = 1

RAMstate = 0 
DISCscate = 0
CPUstate = 0 

def Internet_Iniciar ():
    global a, RAMstate, DISCscate, CPUstate

    while a == 1:

    
            bar1['value'] += 30
            bar2['value'] += 5
            bar3['value'] += 10
            RAMstate += 30
            DISCscate += 5
            CPUstate += 10

            if RAMstate >= 100:
        
                bar1['value'] -= 30
                bar2['value'] -= 5
                bar3['value'] -= 10
                RAMstate -= 30
                DISCscate -= 5
                CPUstate -= 10

                scroll.insert(INSERT, "El proceso 'Internet' esta en espera       ")
                scroll.insert(INSERT, "Termine programas para liberar recursos    ")
                break
            else:
                a = 0
                scroll.insert(INSERT, "El proceso 'Internet ha iniciado          ")
                BarPer1.configure(text = str(RAMstate) + "%")
                BarPer2.configure(text = str(DISCscate) + "%")
                BarPer3.configure(text = str(CPUstate) + "%")


def Internet_Finalizar():
     global a, RAMstate, DISCscate, CPUstate

     
     while a == 0:

        bar1['value'] -= 30
        bar2['value'] -= 5
        bar3['value'] -= 10
        RAMstate -= 30
        DISCscate -= 5
        CPUstate -= 10
        a = 1
        scroll.insert(INSERT, "El proceso 'Internet' ha finalizado               ")
        BarPer1.configure(text = str(RAMstate) + "%")
        BarPer2.configure(text = str(DISCscate) + "%")
        BarPer3.configure(text = str(CPUstate) + "%")

def Documentos_Iniciar():
    global b, RAMstate, DISCscate, CPUstate
    while b == 1: 
        bar1['value'] += 20
        bar2['value'] += 10
        bar3['value'] += 10
        RAMstate += 20
        DISCscate += 10
        CPUstate += 10

         

        if RAMstate >= 100:
            bar1['value'] -= 20
            bar2['value'] -= 10
            bar3['value'] -= 10
            RAMstate -= 20
            DISCscate -= 10
            CPUstate -= 10   

            scroll.insert(INSERT, "El Proceso 'Documentos' esta en espera        ")
            scroll.insert(INSERT, "Termine programas para liberar recursos       ")
            break

        else:

            b = 0
            scroll.insert(INSERT, "El Proceso 'Documentos' ha iniciado           ")
            BarPer1.configure(text = str(RAMstate) + "%")
            BarPer2.configure(text = str(DISCscate) + "%")
            BarPer3.configure(text = str(CPUstate) + "%")

def Documentos_finalizar(): 
    global b, RAMstate, DISCscate, CPUstate
    while b == 0:
        bar1['value'] -= 20
        bar2['value'] -= 10
        bar3['value'] -= 10
        RAMstate -= 20
        DISCscate -= 10
        CPUstate -= 10  
        b = 1
        scroll.insert(INSERT, "El proceso 'Documentos' ha finalizado             ")
        BarPer1.configure(text = str(RAMstate) + "%")
        BarPer2.configure(text = str(DISCscate) + "%")
        BarPer3.configure(text = str(CPUstate) + "%")
              
def Videos_Iniciar(): 
    global c, RAMstate, DISCscate, CPUstate
    while c == 1:
        bar1['value'] += 25
        bar2['value'] += 10
        bar3['value'] += 15
        RAMstate += 25
        DISCscate += 10
        CPUstate += 15  

        if RAMstate >= 100:

            bar1['value'] -= 25
            bar2['value'] -= 10
            bar3['value'] -= 15
            RAMstate -= 25
            DISCscate -= 10
            CPUstate -= 15 

            scroll.insert(INSERT, "El proceso 'Videos' esta en espera             ")
            scroll.insert(INSERT, "Termine programas para liberar recursos        ")
            break

        else:

            c = 0
            scroll.insert(INSERT, "El proceso 'Videos' ha iniciado                ")
            BarPer1.configure(text = str(RAMstate) + "%")
            BarPer2.configure(text = str(DISCscate) + "%")
            BarPer3.configure(text = str(CPUstate) + "%")

def Videos_Finalizar():
    global c, RAMstate, DISCscate, CPUstate

    while c == 0: 
            bar1['value'] -= 25
            bar2['value'] -= 10
            bar3['value'] -= 15
            RAMstate -= 25
            DISCscate -= 10
            CPUstate -= 15 

            c = 1
            scroll.insert(INSERT, "El proceso 'Videos' ha finalizado                ")
            BarPer1.configure(text = str(RAMstate) + "%")
            BarPer2.configure(text = str(DISCscate) + "%")
            BarPer3.configure(text = str(CPUstate) + "%")

def Fotos_Iniciar():
    global d, RAMstate, DISCscate, CPUstate
    while d == 1:
         bar1['value'] += 15
         bar2['value'] += 5
         bar3['value'] += 10
         RAMstate += 15
         DISCscate += 5
         CPUstate += 10

         if RAMstate >= 100:
            bar1['value'] -= 15
            bar2['value'] -= 5
            bar3['value'] -= 10
            RAMstate = 15
            DISCscate -= 5
            CPUstate -= 10
            scroll.insert(INSERT, "El proceso 'Fotos' esta en espera             ")
            scroll.insert(INSERT, "Termine programas para liberar recursos        ")
            break
         
         else: 
            d= 0
            scroll.insert(INSERT, "El proceso 'Fotos' ha iniciado                ")
            BarPer1.configure(text = str(RAMstate) + "%")
            BarPer2.configure(text = str(DISCscate) + "%")
            BarPer3.configure(text = str(CPUstate) + "%")

def Fotos_Finalizar(): 
    global d, RAMstate, DISCscate, CPUstate
    while d == 0:
        bar1['value'] -= 15
        bar2['value'] -= 5
        bar3['value'] -= 10
        RAMstate = -15
        DISCscate -= 5
        CPUstate -= 10
        d = 1 
        scroll.insert(INSERT, "El proceso 'Fotos' ha Finalizado                ")
        BarPer1.configure(text = str(RAMstate) + "%")
        BarPer2.configure(text = str(DISCscate) + "%")
        BarPer3.configure(text = str(CPUstate) + "%")

def Juego_Iniciar():
    global e, RAMstate, DISCscate, CPUstate
    while e == 1:
         bar1['value'] += 40
         bar2['value'] += 15
         bar3['value'] += 25
         RAMstate += 40
         DISCscate += 15
         CPUstate += 25

         if RAMstate >= 100:
            bar1['value'] -= 40
            bar2['value'] -= 15
            bar3['value'] -= 25
            RAMstate -= 40
            DISCscate -= 15
            CPUstate -= 25
            scroll.insert(INSERT, "El proceso 'Juego' esta en espera             ")
            scroll.insert(INSERT, "Termine programas para liberar recursos        ")
            break
        
         else: 
             
          e = 0
          scroll.insert(INSERT, "El proceso 'Juego' ha iniciado                   ")
          BarPer1.configure(text = str(RAMstate) + "%")
          BarPer2.configure(text = str(DISCscate) + "%")
          BarPer3.configure(text = str(CPUstate) + "%")


def Juego_Finzalizar():
    global e, RAMstate, DISCscate, CPUstate
    while e == 0:
         bar1['value'] -= 40
         bar2['value'] -= 15
         bar3['value'] -= 25
         RAMstate -= 40
         DISCscate -= 15
         CPUstate -= 25
         e == 1
         scroll.insert(INSERT, "El proceso 'Juego' ha Finalizado                   ")
         BarPer1.configure(text = str(RAMstate) + "%")
         BarPer2.configure(text = str(DISCscate) + "%")
         BarPer3.configure(text = str(CPUstate) + "%")

def Anti_Iniciar():
    global f, RAMstate, DISCscate, CPUstate
    while f == 1:
         bar1['value'] += 20
         bar2['value'] += 10
         bar3['value']+= 20
         RAMstate += 20
         DISCscate += 10
         CPUstate += 20

         if RAMstate >= 100:
            bar1['value'] -= 20
            bar2['value'] -= 10
            bar3['value'] -= 20
            RAMstate -= 20
            DISCscate -= 10
            CPUstate -= 20
            scroll.insert(INSERT, "El proceso 'Antivirus' esta en espera             ")
            scroll.insert(INSERT, "Termine programas para liberar recursos        ")
            break
         else: 
          f = 0
         scroll.insert(INSERT, "El proceso 'Antvirus' ha Iniciado                   ")
         BarPer1.configure(text = str(RAMstate) + "%")
         BarPer2.configure(text = str(DISCscate) + "%")
         BarPer3.configure(text = str(CPUstate) + "%")

def Anti_Finalizar ():
    global f, RAMstate, DISCscate, CPUstate
    while f == 0:
        bar1['value'] -= 20
        bar2['value'] -= 10
        bar3['value'] -= 20
        RAMstate -= 20
        DISCscate -= 10
        CPUstate -= 20

        f = 1
        scroll.insert(INSERT, "El proceso 'Antvirus' ha Finalizado                   ")
        BarPer1.configure(text = str(RAMstate) + "%")
        BarPer2.configure(text = str(DISCscate) + "%")
        BarPer3.configure(text = str(CPUstate) + "%")


def VS_Iniciar():
    global g, RAMstate, DISCscate, CPUstate
    while g == 1:
         bar1['value'] += 15
         bar2['value'] += 5
         bar3['value']+= 15
         RAMstate += 15
         DISCscate += 5
         CPUstate += 15

         if RAMstate >= 100:
            bar1['value'] -= 15
            bar2['value'] -= 5
            bar3['value'] -= 15
            RAMstate -= 15
            DISCscate -= 5
            CPUstate -= 15
            scroll.insert(INSERT, "El proceso 'VS Code' esta en espera             ")
            scroll.insert(INSERT, "Termine programas para liberar recursos        ")
            break
         else: 
          g = 0
         scroll.insert(INSERT, "El proceso 'VS Code' ha iniciado                   ")
         BarPer1.configure(text = str(RAMstate) + "%")
         BarPer2.configure(text = str(DISCscate) + "%")
         BarPer3.configure(text = str(CPUstate) + "%")

def VS_Finalizar(): 
    global f, RAMstate, DISCscate, CPUstate
    while f == 0:
        bar1['value'] -= 15
        bar2['value'] -= 5
        bar3['value'] -= 15
        RAMstate -= 15
        DISCscate -= 5
        CPUstate -= 15

        g = 1
        SCROLL.insert(INSERT, "El proceso 'VS Code' ha Finalizado                   ")
        BarPer1.configure(text = str(RAMstate) + "%")
        BarPer2.configure(text = str(DISCscate) + "%")
        BarPer3.configure(text = str(CPUstate) + "%")

def Photo_Iniciar():
    global h, RAMstate, DISCscate, CPUstate
    while h == 1:
         bar1['value'] += 25
         bar2['value'] += 15
         bar3['value']+= 20
         RAMstate += 25
         DISCscate += 15
         CPUstate += 20

         if RAMstate >= 100:
            bar1['value'] -= 25
            bar2['value'] -= 15
            bar3['value'] -= 20
            RAMstate -= 25
            DISCscate -= 15
            CPUstate -= 20
            scroll.insert(INSERT, "El proceso 'Photoshop' esta en espera             ")
            scroll.insert(INSERT, "Termine programas para liberar recursos        ")
            break
         
         else: 
          h = 0
         scroll.insert(INSERT, "El proceso 'VS Code' ha iniciado                   ")
         BarPer1.configure(text = str(RAMstate) + "%")
         BarPer2.configure(text = str(DISCscate) + "%")
         BarPer3.configure(text = str(CPUstate) + "%")

def Photo_Finalizar(): 
    global h, RAMstate, DISCscate, CPUstate
    while h == 0:
        bar1['value'] -= 25
        bar2['value'] -= 15
        bar3['value'] -= 20
        RAMstate -= 25
        DISCscate -= 15
        CPUstate -= 20

        h = 1
        scroll.insert(INSERT, "El proceso 'Photoshop' ha Finalizado                   ")
        BarPer1.configure(text = str(RAMstate) + "%")
        BarPer2.configure(text = str(DISCscate) + "%")
        BarPer3.configure(text = str(CPUstate) + "%")

def clear(): 
    scroll.delete(1,0,END)
    scroll.insert(INSERT, "       Registro de procesos     ")







#Ventana
window = Tk()
window.geometry("660x600")
window.title("Valentina Sequera Sistema Operativo")

#frame 
frame = Frame(window)
frame.pack()

#canvas
canvas = Canvas(frame, width=700, height= 660)
canvas.pack()

#fondo
background = PhotoImage(file= "Fondo4.png")
canvas.create_image(320,320, image=background)

#Iconos 
InTicon = Image.open("internet.png")
resized = InTicon.resize((50,50), Image.LANCZOS)
InTicon = ImageTk.PhotoImage(resized)
canvas.create_image(136,50, image = InTicon)

DocIcon = Image.open( "documentos.png")
resized = DocIcon.resize ((50,50), Image.LANCZOS)
DocIcon = ImageTk.PhotoImage (resized)
canvas.create_image(270,50, image=DocIcon)

VidIcon = Image.open( "Video.png")
resized = VidIcon.resize ((50,50), Image.LANCZOS)
VidIcon = ImageTk.PhotoImage (resized)
canvas.create_image(400,50, image=VidIcon)

FotoIcon = Image.open( "fotos.png")
resized = FotoIcon.resize ((50,50), Image.LANCZOS)
FotoIcon = ImageTk.PhotoImage (resized)
canvas.create_image(530,55, image=FotoIcon)

JuegoIcon = Image.open( "Juego.png")
resized = JuegoIcon.resize ((50,50), Image.LANCZOS)
JuegoIcon = ImageTk.PhotoImage (resized)
canvas.create_image(140,185, image=JuegoIcon)

AntiICon = Image.open( "avast.png")
resized = AntiICon.resize ((50,50), Image.LANCZOS)
AntiICon = ImageTk.PhotoImage (resized)
canvas.create_image(270,175, image=AntiICon)

VSIcon = Image.open( "VS Code.png")
resized = VSIcon.resize ((50,50), Image.LANCZOS)
VSIcon = ImageTk.PhotoImage (resized)
canvas.create_image(400,175, image=VSIcon)

PhotoShopICon = Image.open( "PhotoShop.png")
resized = PhotoShopICon.resize ((50,50), Image.LANCZOS)
PhotoShopICon = ImageTk.PhotoImage (resized)
canvas.create_image(530,175, image=PhotoShopICon)



#Textos
canvas.create_text(140, 85, text= "Internet")
canvas.create_text(272, 85, text= "Documentos")
canvas.create_text(400, 85, text= "Videos")
canvas.create_text(530, 85, text= "Fotos")  

canvas.create_text(140, 212, text= "Juegos")
canvas.create_text(272, 212, text= "Antivirus")
canvas.create_text(405, 212, text= "Viual Studio Code")
canvas.create_text(530, 212, text= "PhotoShop")


BarName1 = Label (window, text= "RAM")
BarName2 = Label (window, text= "Disco")
BarName3 = Label (window, text= "CPU")

BarPer1 = Label (window, text= "0%")
BarPer2 = Label (window, text= "0%")
BarPer3 = Label (window, text= "0%")

#Posiciones de los textos
BarName1.place(relx = 0.6, rely = 0.7, anchor= 'center')
BarName2.place(relx = 0.6, rely = 0.8, anchor= 'center')
BarName3.place(relx = 0.6, rely = 0.9, anchor= 'center')
             
BarPer1.place(relx = 0.95, rely = 0.7, anchor= 'center')
BarPer2.place(relx = 0.95, rely = 0.8, anchor= 'center')
BarPer3.place(relx = 0.95, rely = 0.9, anchor= 'center')

#Barras de progreso
bar1 = Progressbar(window, length= 190)
bar2 = Progressbar(window, length= 190)
bar3 = Progressbar(window, length= 190)

#Posiciones de las barras
bar1.place(relx = 0.78, rely = 0.7, anchor= 'center')
bar2.place(relx = 0.78, rely = 0.8, anchor= 'center')
bar3.place(relx = 0.78, rely = 0.9, anchor= 'center')

#Scroltxt
scroll = scrolledtext.ScrolledText(window, width =43, height=12)
scroll.place(relx = 0.56, rely = 0.82, anchor= 'e')
scroll.insert(INSERT, '------------------- Registro de procesos  ---------------------')

#Botones
BotonInterA = Button(window, text= "Iniciar", command= lambda: [Internet_Iniciar()])
BotonInterB = Button(window, text= "Terminar", command= lambda: [Internet_Finalizar()])
BotonDocA = Button(window, text= "Iniciar", command= lambda: [Documentos_Iniciar()])
BotonDocB = Button(window, text= "Terminar", command= lambda: [Documentos_finalizar()])
BotonVideoA = Button(window, text= "Iniciar", command= lambda: [Videos_Iniciar()])
BotonVideoB = Button(window, text= "Terminar", command= lambda: [Videos_Finalizar()])
BotonFotosA = Button(window, text= "Iniciar", command= lambda: [Fotos_Iniciar()])
BotonFotosB = Button(window, text= "Terminar", command= lambda: [Fotos_Finalizar()])

BotonJuegoA = Button(window, text= "Iniciar", command= lambda: [Juego_Iniciar()])
BotonJuegoB = Button(window, text= "Terminar", command= lambda: [Juego_Finzalizar()])
BotonAntiA = Button(window, text= "Iniciar", command= lambda: [Anti_Iniciar()])
BotonAntiB = Button(window, text= "Terminar", command= lambda: [Anti_Finalizar()])
BotonVSA = Button(window, text= "Iniciar", command= lambda: [VS_Iniciar()])
BotonVSB = Button(window, text= "Terminar", command= lambda: [VS_Finalizar()])
BotonPhotoA = Button(window, text= "Iniciar", command= lambda: [Photo_Iniciar()])
BotonPhotoB = Button(window, text= "Terminar", command= lambda: [Photo_Finalizar()])

Clear = Button(window,text= "clear", command= clear)

#Posiciones de los botones
BotonInterA.place(relx = 0.17, rely= 0.19, anchor= 'center')
BotonDocA.place(relx = 0.37, rely= 0.19, anchor= 'center')
BotonVideoA.place(relx = 0.57, rely= 0.19, anchor= 'center')
BotonFotosA.place(relx = 0.77, rely= 0.19, anchor= 'center')
BotonJuegoA.place(relx = 0.17, rely= 0.40, anchor= 'center')
BotonAntiA.place(relx = 0.37, rely= 0.40, anchor= 'center')
BotonVSA.place(relx = 0.57, rely= 0.40, anchor= 'center')
BotonPhotoA.place(relx = 0.77, rely= 0.40, anchor= 'center')

BotonInterB.place(relx = 0.25, rely= 0.19, anchor= 'center')
BotonDocB.place(relx = 0.45, rely= 0.19, anchor= 'center')
BotonVideoB.place(relx = 0.65, rely= 0.19, anchor= 'center')
BotonFotosB.place(relx = 0.85, rely= 0.19, anchor= 'center')
BotonJuegoB.place(relx = 0.25, rely= 0.40, anchor= 'center')
BotonAntiB.place(relx = 0.45, rely= 0.40, anchor= 'center')
BotonVSB.place(relx = 0.65, rely= 0.40, anchor= 'center')
BotonPhotoB.place(relx = 0.85, rely= 0.40, anchor= 'center')

Clear.place(relx = 0.60, rely= 0.96, anchor = 'center')



window.mainloop()
