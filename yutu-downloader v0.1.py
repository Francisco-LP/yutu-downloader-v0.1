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

#frame
root = customtkinter.CTk()
root.geometry("600x400")
root.title("Yutu-Downloader  0.1")


#elementos 

urlTitulo = customtkinter.CTkLabel(root, text="URL")
urlTitulo.pack()

#link input
url = tkinter.StringVar()
link = customtkinter.CTkEntry(root,width=400,height=45)
link.pack()

download = customtkinter.CTkButton(root,text="Descargar", command=descargar)
download.pack(pady=10)

#barra de progreso
porcentaje = customtkinter.CTkLabel(root, text="0%")

barraDeProgreso = customtkinter.CTkProgressBar(root, width=400)
barraDeProgreso.set(0)


#mensaje
descargado = customtkinter.CTkLabel(root,text="")
descargado.pack(pady=10)

tituloVideo = customtkinter.CTkLabel(root,text="")
tituloVideo.pack(pady=10)



#mantener app abierta
root.mainloop()