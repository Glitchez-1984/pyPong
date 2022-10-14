from tkinter import *
from tkinter import colorchooser
def get_colors():
    root = Tk()
    root.title("Main Menu")
    root.geometry("400x300")
    root.configure(background='#292152')
    canvas = Canvas(root, width=105, height=55)
    canvas.configure(background='#292152', highlightthickness=0)
    canvas1 = Canvas(root, width=105, height=55)
    canvas1.configure(background='#292152', highlightthickness=0)

    def round_rectangle(x1, y1, x2, y2, r=25, **kwargs):
        points = (
            x1 + r, y1, x1 + r, y1, x2 - r, y1, x2 - r, y1, x2, y1, x2, y1 + r, x2, y1 + r, x2, y2 - r, x2, y2 - r, x2,
            y2,
            x2 - r, y2, x2 - r, y2, x1 + r, y2, x1 + r, y2, x1, y2, x1, y2 - r, x1, y2 - r, x1, y1 + r, x1, y1 + r, x1,
            y1)
        return canvas.create_polygon(points, **kwargs, smooth=True)

    def round_rectangle1(x1, y1, x2, y2, r=25, **kwargs):
        points = (
            x1 + r, y1, x1 + r, y1, x2 - r, y1, x2 - r, y1, x2, y1, x2, y1 + r, x2, y1 + r, x2, y2 - r, x2, y2 - r, x2,
            y2,
            x2 - r, y2, x2 - r, y2, x1 + r, y2, x1 + r, y2, x1, y2, x1, y2 - r, x1, y2 - r, x1, y1 + r, x1, y1 + r, x1,
            y1)
        return canvas1.create_polygon(points, **kwargs, smooth=True)

    def disable_button():
        root.destroy()

    def color_ask():
        global color
        color = colorchooser.askcolor()
        my_rectangle = round_rectangle(0, 0, 100, 50, fill=color[1], outline="white")
        canvas.place(x=40, y=100)

    def color_ask1():
        global color1
        color1 = colorchooser.askcolor()
        my_rectangle = round_rectangle1(0, 0, 100, 50, fill=color1[1], outline="white")
        canvas1.place(x=250, y=100)
    radio = IntVar()
    bg_button = Button(root, text="Foreground", command=color_ask, bg="#c9d9f2").place(x=65, y=50)
    fg_button = Button(root, text="Background", command=color_ask1, bg="#c9d9f2").place(x=265, y=50)
    P1 = Radiobutton(root, text="Singleplayer", value=0,variable=radio, fg = "red", background='#292152').place(x=150, y=100)
    P2 = Radiobutton(root, text="Multiplayer", value=1, variable=radio, fg = "red", background='#292152').place(x=150, y=50)
    #L1 = Radiobutton(root, text="Easy", value=1, variable=radio, fg="red", background='#292152').place(x=150,y=50)
    #L2 = Radiobutton(root, text="Medium", value=1, variable=radio, fg="red", background='#292152').place(x=150,y=50)
    #L3 = Radiobutton(root, text="Hard", value=1, variable=radio, fg="red", background='#292152').place(x=150,y=50)
    done = Button(root, text="Finished", command=disable_button).place(x=160, y=180)
    root.mainloop()
    try:
        return color1[1], color[1], int(radio.get())
    except:
        return (0,0,0), (255,255,255), int(radio.get())
