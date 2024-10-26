from tkinter import *
import string as st
from random import randint, choice
import tksvg
# from PIL.ImageOps import expand
# from reportlab.lib.colors import yellow

# Créer la fonction de generation du mot de passe
def generate_password():
    password=''
    password_min = 6
    password_max = 12
    all_chars = st.ascii_letters + st.punctuation + st.digits
    for x in range(1,randint(password_min,password_max)):
        password = password + "".join(choice(all_chars))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# Créer une première fenêtre
window=Tk()
# Personnaliser la fenêtre
window.title("Password Generator")
window.geometry("800x800")
window.minsize(400,400)

icon = PhotoImage(file ="Logo_Raphael.png")
window.iconphoto(True, icon)
window.config(bg='lightblue')

# Créer la frame principale
frame_principale=Frame(window,bg='lightblue' )

left_frame=Frame(frame_principale, bg='lightblue')
# On place la left_frame à gauche de la frame principale
left_frame.grid(row=0,column=0, sticky=W)
# Création d'image
width=260
height=260
image = PhotoImage(file="Data/password.png").zoom(10).subsample(10)
canvas = Canvas(left_frame, width=width, height=height, bg='lightblue',bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.pack()#grid(row=0, column=0, sticky=W) #expand=YES)

right_frame=Frame(frame_principale, bg='lightblue')
# On place la right_frame à droite de la frame principale
right_frame.grid(row=0,column=1, sticky=E)
# Créer un titre
label_title=Label(right_frame, text="Entrez votre mot de passe", font=("Helvetica", 20), bg='lightblue')
label_title.grid(row=0, column=0, sticky=NSEW)#pack()
# Créer un champ/entrée/input
password_entry=Entry(right_frame, font=("Helvetica", 20), bg='lightblue')
password_entry.grid(row=1, column=0, sticky=NSEW)#pack()
# Ajout d'un bouton pour générer le mot de passe
generate_password_bouton=Button(right_frame, text="Générer", font=("Helvetica", 20), bg='lightblue', command=generate_password)
generate_password_bouton.grid(row=3, column=0, sticky=NSEW)#pack()

frame_principale_2=Frame(window,bg='lightblue', pady=20)
d = '''<svg width="10" height="10"><path d="M17.2 26.6l1.4 2.9 3.2.5-2.2 2.3.6 3.2-2.9-1.5-2.9 1.5.6-3.2-2.3-2.3 3.2-.5zM44.8 3.8l2 .3-1.4 1.4.3 2-1.8-.9-1.8.9.3-2L41 4.1l2-.3.9-1.8zM8.9 10l.9 1.8 2 .3-1.4 1.4.3 2-1.8-.9-1.8.9.3-2L6 12.1l2-.3zm37.6 17l.647 1.424 1.553.258-1.165 1.165.26 1.553-1.424-.776-1.295.647.26-1.553-1.165-1.165 1.553-.259zM29.191 1C24.481 2.216 21 6.512 21 11.626c0 6.058 4.887 10.97 10.915 10.97 3.79 0 7.128-1.941 9.085-4.888-.87.224-1.783.344-2.724.344-6.028 0-10.915-4.912-10.915-10.97 0-2.25.674-4.341 1.83-6.082z" fill="#7694b4" fill-rule="evenodd"></path></svg>'''

# if you have a SVG file on disk, use the file parameter:
svg_image = tksvg.SvgImage( file = 'Data/new.svg', scale = 0.125)
# if you have SVG code from somewhere - in my case I scraped it from a website - use the data parameter:
# svg_image = tksvg.SvgImage( data = d )

# You can also resize the image, but using only one of the three available parameters:
# svg_image = tksvg.SvgImage( data = d, scale = 0.5 )
# svg_image = tksvg.SvgImage( data = d, scaletowidth = 200 )
# svg_image = tksvg.SvgImage( data = d, scaletoheight = 200 )
label_image=Label( frame_principale_2,image = svg_image, bd=0 , justify="right")
label_image.pack()


frame_principale.pack(expand=YES)
frame_principale_2.pack(expand=YES)

# Création d'une barre de menu
menu_bar=Menu(window)
# créer un 1er menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Générer un mot de passe', command=generate_password)
file_menu.add_command(label='Quitter', command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)
# Configurer notre fenêtre pour ajouter le menu-bar
window.config(menu=menu_bar)

window.mainloop()