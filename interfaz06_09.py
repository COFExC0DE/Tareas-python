from tkinter import *


def primera_linea():
    tk = Tk()
    canvas = Canvas(tk, width=400, height=400)
    canvas.pack()
    canvas.create_arc(150, 150, 300, 100, extent=80, style=ARC)
    canvas.create_arc(50, 350, 300, 100, extent=80, style=ARC)
    canvas.create_arc(50, 350, 100, 150, extent=120, style=ARC)
    canvas.create_arc(400, 400, 40, 40, extent=80, style=ARC)
    canvas.create_line(0, 0, 400, 400)
    canvas.create_line(400, 400, 0, 0)
    return segunda_linea()

def segunda_linea():
    tk = Tk()
    canvas = Canvas(tk, width=400, height=400)
    canvas.pack()
    canvas.create_arc(350, 350, 300, 100, extent=80, style=ARC)


primera_linea()
