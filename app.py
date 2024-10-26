from tkinter import *
import webbrowser

def open_graven_channel():
    webbrowser.open_new("https://github.com/htitushg/graven_1")

# Créer une première fenêtre
window=Tk()
# Personnaliser la fenêtre
window.title("My application")
window.geometry("400x400")
window.minsize(200,200)

icon = PhotoImage(file ="Logo_Raphael.png")
window.iconphoto(True, icon)
window.config(bg='#41B77F')

# Créer une boite (frame)
frame_1=Frame(window, bg='#41B77F', bd=1, relief=SUNKEN)
frame_1.pack(expand=YES)

# Ajouter un texte
label_title= Label(frame_1, text="Bonjour", font=("Courrier", 40), bg='#41B77F', fg='white')
label_title.pack(expand=YES)
label_subtitle= Label(frame_1, text="Salut à tous", font=("Courrier", 25), bg='#41B77F', fg='white')
label_subtitle.pack(expand=YES)
# Ajouter un bouton
yt_bouton = Button(frame_1, text="Ouvrir Github HG", font=("Courrier", 25), bg='white', fg='#41B77F', command=open_graven_channel)
yt_bouton.pack(pady=25, fill=X)

window.mainloop()