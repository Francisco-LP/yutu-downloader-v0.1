from tkinter import * 
from tkinter import ttk
import tkinter
import customtkinter
from pytube import YouTube

def descargar():
   
    try:
        urlYutu= link.get()
        porcentaje.pack()
        barraDeProgreso.pack(pady=10)
        yutuObject = YouTube(urlYutu, on_progress_callback=on_progress)
        
        video = yutuObject.streams.get_highest_resolution()
        video.download()
        tituloVideo.configure(text=yutuObject.title)
        descargado.configure(text="Descargado...")
    except:
        print("error ")
    print("Descarga exitosa")
    

def descargarAudio():
    try:
        urlYutu= link.get()
        porcentaje.pack()
        barraDeProgreso.pack(pady=10)
        yutuObject = YouTube(urlYutu, on_progress_callback=on_progress)
        
        audio = yutuObject.streams.filter(only_audio=True)
        audioFormato = audio.get_by_itag('140')
        audioFormato.download()
        tituloVideo.configure(text=yutuObject.title)
        descargado.configure(text="Descargado...")
    except:
        print("error ")
    print("Descarga exitosa")    
    


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    porcentaje.configure(text= per + "%")
    porcentaje.update()

    #actualizacion de la barra de Progreso
    barraDeProgreso.set(float(percentage_of_completion) / 100)
    



#Ajustes del sistema
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("600x400")
root.title("Yutu-Downloader  0.2")

# pestañas (Tabs)
notebook = ttk.Notebook(root)


tabVideo = customtkinter.CTkFrame(notebook)
tabAudio = customtkinter.CTkFrame(notebook)

notebook.add(tabVideo, text="Video")
notebook.add(tabAudio, text="Audio")
notebook.pack(expand=True, fill="both") #las pestañas quedan a la izquierd y se expandan 


# Elementos #

###################### Video ######################

# Titulo Video

urlTitulo = customtkinter.CTkLabel(tabVideo, text="URL del Video")
urlTitulo.pack()

#link input
url = tkinter.StringVar()
link = customtkinter.CTkEntry(tabVideo,width=400,height=45)
link.pack()

# boton
download = customtkinter.CTkButton(tabVideo,text="Descargar", command=descargar)
download.pack(pady=10)

#barra de progreso
porcentaje = customtkinter.CTkLabel(tabVideo, text="0%")

barraDeProgreso = customtkinter.CTkProgressBar(tabVideo, width=400)
barraDeProgreso.set(0)

#mensaje
descargado = customtkinter.CTkLabel(tabVideo,text="")
descargado.pack(pady=10)

tituloVideo = customtkinter.CTkLabel(tabVideo,text="")
tituloVideo.pack(pady=10)

###################### Audio ######################

# Titulo Audio

urlTitulo = customtkinter.CTkLabel(tabAudio, text="URL del Audio")
urlTitulo.pack()

#link input
url = tkinter.StringVar()
link = customtkinter.CTkEntry(tabAudio,width=400,height=45)
link.pack()

#boton
download = customtkinter.CTkButton(tabAudio,text="Descargar", command=descargarAudio)
download.pack(pady=10)

#barra de progreso
porcentaje = customtkinter.CTkLabel(tabAudio, text="0%")

barraDeProgreso = customtkinter.CTkProgressBar(tabAudio, width=400)
barraDeProgreso.set(0)

#mensaje
descargado = customtkinter.CTkLabel(tabAudio,text="")
descargado.pack(pady=10)

tituloVideo = customtkinter.CTkLabel(tabAudio,text="")
tituloVideo.pack(pady=10)

#mantener app abierta
root.mainloop()