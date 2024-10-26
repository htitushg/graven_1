from tkinter import *

import tksvg


# Créer une première fenêtre
window=Tk()
# Personnaliser la fenêtre
window.title("Password Generator")
window.geometry("400x400")
window.minsize(200,200)

icon = PhotoImage(file ="Logo_Raphael.png")
window.iconphoto(True, icon)
window.config(bg='lightblue')

# Création d'image
width=300
height=300
image = PhotoImage(file="Data/password.png").zoom(10).subsample(10)
canvas = Canvas(window, width=width, height=height, bg='lightblue',bd=2)
canvas.create_image(width/2, height/2, image=image)
canvas.pack(expand=YES)

d = '''<svg width="10" height="10"><path d="M17.2 26.6l1.4 2.9 3.2.5-2.2 2.3.6 3.2-2.9-1.5-2.9 1.5.6-3.2-2.3-2.3 3.2-.5zM44.8 3.8l2 .3-1.4 1.4.3 2-1.8-.9-1.8.9.3-2L41 4.1l2-.3.9-1.8zM8.9 10l.9 1.8 2 .3-1.4 1.4.3 2-1.8-.9-1.8.9.3-2L6 12.1l2-.3zm37.6 17l.647 1.424 1.553.258-1.165 1.165.26 1.553-1.424-.776-1.295.647.26-1.553-1.165-1.165 1.553-.259zM29.191 1C24.481 2.216 21 6.512 21 11.626c0 6.058 4.887 10.97 10.915 10.97 3.79 0 7.128-1.941 9.085-4.888-.87.224-1.783.344-2.724.344-6.028 0-10.915-4.912-10.915-10.97 0-2.25.674-4.341 1.83-6.082z" fill="#7694b4" fill-rule="evenodd"></path></svg>'''

# if you have a SVG file on disk, use the file parameter:
#svg_image = tksvg.SvgImage( file = 'Data/twitch_icon_146123.svg').subsample(20,20)
svg_image = tksvg.SvgImage( file = 'Data/new.svg', scale = 0.125)
# if you have SVG code from somewhere - in my case I scraped it from a website - use the data parameter:
#svg_image = tksvg.SvgImage( data = d )

# You can also resize the image, but using only one of the three available parameters:
# svg_image = tksvg.SvgImage( data = d, scale = 0.5 )
# svg_image = tksvg.SvgImage( data = d, scaletowidth = 200 )
#svg_image = tksvg.SvgImage( data = d, scaletoheight = 200 )
label_image=Label( image = svg_image )
label_image.pack()





window.mainloop()