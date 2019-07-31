#AUTOR Jose Pablo Barrientos Rojas
from tkinter import *
import sys
import time
import random


#la class "Ball" crea los objetos bolas, las cuales see utilizan para dibujar las curvas de bezier
class Ball:
    def __init__(self,canvas,x1,y1,color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 0, 0, outline = color, fill = color)#crea los circulos, le puede poner el tama;o que se requiera
        self.canvas.move(self.id, x1, y1)#en el espacio de la ventana, dice en que parte de la ventana se va a situar en este caso los circulos.
        
#la class "Pixels" crea los objetos pixeles dibuja o es el grafico de las curvas        
class Pixels:
    def __init__(self,canvas,t,p,color,tam):
        self.canvas = canvas
        self.id = canvas.create_oval(tam, tam, 1, 1,outline = color, fill=color)#crea los circulos, le puede poner el tama;o que se requiera
        self.canvas.move(self.id, t, p)
#"Hacer curva", aplica la formula matematica(curva de bezier), para que por medio de los ejes,
# x = x1,x2,x3,x4 y los y= y1,y2,y3,y4 y t = total de pixeles o el largo de un punto 'x' a un punto 'y'         
def hacer_curva(x1,x2,x3,x4,y1,y2,y3,y4,t,tiempo,tam,color):
    timer1 = time.time()#se crea la funcion tiempo para luego con " time.sleep()" poner dentro de los "()" los segundo que desea que se espere para crear los pixeles.
    if t > 1:
        return 0
    else:
        x = x1*(1-t)**3+x2*3*(1-t)**2*t+x3*3*(1-t)*t**2+x4*t**3#formulas de Bezier para el eje 'x'(dibujar por pixel)
        y = y1*(1-t)**3+y2*3*(1-t)**2*t+y3*3*(1-t)*t**2+y4*t**3#formulas de Bezier para el eje 'y'(dibujar por pixel)
        root.update_idletasks()#reinicia la ventana para que se vea el movimiento de los pixeles
        root.update()#reinicia la ventana para que se vea el movimiento de los pixeles
        time.sleep(tiempo)#llama a la funcion de tiempo, para que pase cuanto tiene q esperar
        Pixels(canvas,x , y, color,tam)
    hacer_curva(x1,x2,x3,x4,y1,y2,y3,y4,t+0.01,tiempo,tam,color)#llamada recursiva
    
#button da las acciones, de tamano de pixel, color o colores q desee, 
def button():
    tamano_text = text1.get()#guarda y utiliza el texto para realizar acciones, luego de dar aceptar al boton
    random_text = text2.get()#guarda y utiliza el texto para realizar acciones, luego de dar aceptar al boton
    tiempo_text = text3.get()#guarda y utiliza el texto para realizar acciones, luego de dar aceptar al boton
    mlabel2 = crear_curvas(tamano_text, random_text,float(tiempo_text))#cuando le da aceptar en el botton de la interfas grafica llama a crear curvas para validar las acciones de los textos
    
# "sor_color" hace el random para dibujar las curvas por partes
def sor_color(color):
    sorteo = ''
    if color == 'colores' or color =='green' or color =='blue' or color =='red' or color =='black' or color =='yellow' or color =='white' or color =='cyan' or color =='pink': #solo los valores que acepta 
        if color == 'colores':
            sorteo = random.sample(['green', 'blue', 'red', 'black', 'yellow','white','cyan','pink' ],  1)
        else:
            sorteo = color
    else: 	
        print("error")
        
    return sorteo

#crear_curvas crea las bolas que dibujan y jalas las curvas para poder hacer las figuras    
def crear_curvas(tam,color,tiempo):

    timer1 = time.time()
    #Hacer la 'J'
    time.sleep(0.40)
    ball_left = Ball(canvas,120,160,'red')
    ball_right = Ball(canvas, 35, 200,'blue')
    ball_left_down = Ball(canvas, 220, 260, 'black')
    ball_right_down = Ball(canvas, 220, 40,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(120,35,220,220,160,200,260,40,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    canvas.delete(Ball)
    time.sleep(0.40)
    ball_left = Ball(canvas,180,34,'red')
    ball_right = Ball(canvas, 230, 30,'blue')
    ball_left_down = Ball(canvas, 200, 30, 'black')
    ball_right_down = Ball(canvas, 250, 34,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(180,230,250,250,34,30,30,34,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #Termina la 'J'
    #Hacer la 'o'
    time.sleep(0.40)
    ball_left = Ball(canvas,230,140,'red')
    ball_right = Ball(canvas, 230, 180,'blue')
    ball_left_down = Ball(canvas, 290, 180, 'black')
    ball_right_down = Ball(canvas, 290, 140,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(230,230,290,290,140,180,180,140,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,230,140,'red')
    ball_right = Ball(canvas, 230, 100,'blue')
    ball_left_down = Ball(canvas, 290, 100, 'black')
    ball_right_down = Ball(canvas, 290, 140,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(230,230,290,290,140,100,100,140,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos 
    #Termina la 'o'
    #Dibujar la 's'
    time.sleep(0.40)
    ball_left = Ball(canvas,310,170,'red')
    ball_right = Ball(canvas, 385, 185,'blue')
    ball_left_down = Ball(canvas, 270, 120, 'black')
    ball_right_down = Ball(canvas, 340, 110,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(310,385,270,340,170,185,120,110,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #terminar la 's'
    #Dibujar la 'e'
    time.sleep(0.40)
    ball_left = Ball(canvas,400,110,'red')
    ball_right = Ball(canvas, 350, 110,'blue')
    ball_left_down = Ball(canvas, 350, 170, 'black')
    ball_right_down = Ball(canvas, 400, 170,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(400,350,350,400,110,110,170,170,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,400,110,'red')
    ball_right = Ball(canvas, 400, 120,'blue')
    ball_left_down = Ball(canvas, 380, 130, 'black')
    ball_right_down = Ball(canvas, 370, 120,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(400,400,380,370,110,120,130,120,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #terminar la 'e'
    #Dibujar la 'P'
    time.sleep(0.40)
    ball_left = Ball(canvas,475,34,'red')
    ball_right = Ball(canvas, 469, 90,'blue')
    ball_left_down = Ball(canvas, 475, 120, 'black')
    ball_right_down = Ball(canvas, 475, 190,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(475,469,475,475,34,90,120,190,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,440,30,'red')
    ball_right = Ball(canvas, 510, 10,'blue')
    ball_left_down = Ball(canvas, 540,70, 'black')
    ball_right_down = Ball(canvas, 485, 90,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(440,510,540,485,30,10,70,90,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #terminar la 'P'
    #Dibujar la 'a'
    time.sleep(0.40)
    ball_left = Ball(canvas,490,150,'red')
    ball_right = Ball(canvas, 490, 190,'blue')
    ball_left_down = Ball(canvas, 550, 190, 'black')
    ball_right_down = Ball(canvas, 550, 150,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(490,490,550,550,150,190,190,150,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,490,150,'red')
    ball_right = Ball(canvas, 490, 110,'blue')
    ball_left_down = Ball(canvas, 550, 110, 'black')
    ball_right_down = Ball(canvas, 550, 150,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(490,490,550,550,150,110,110,150,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,550,150,'red')
    ball_right = Ball(canvas, 550, 160,'blue')
    ball_left_down = Ball(canvas, 560, 180, 'black')
    ball_right_down = Ball(canvas, 570, 190,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(550,550,560,570,150,160,180,190,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #terminar la 'a'
    #Dibujar la 'b'
    time.sleep(0.40)
    ball_left = Ball(canvas,580,34,'red')
    ball_right = Ball(canvas, 580, 90,'blue')
    ball_left_down = Ball(canvas, 580, 120, 'black')
    ball_right_down = Ball(canvas, 580, 190,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(580,580,580,580,34,90,120,190,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,580,120,'red')
    ball_right = Ball(canvas, 620, 120,'blue')
    ball_left_down = Ball(canvas, 620,190, 'black')
    ball_right_down = Ball(canvas, 580, 190,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(580,620,620,580,120,120,190,190,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #terminar la 'b'
    #Dibujar la 'l'
    time.sleep(0.40)
    ball_left = Ball(canvas,635,34,'red')
    ball_right = Ball(canvas, 640, 80,'blue')
    ball_left_down = Ball(canvas, 630, 120, 'black')
    ball_right_down = Ball(canvas, 625, 190,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(635,640,630,625,34,80,120,190,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #terminar la 'l'
    #Dibujar la 'o'
    time.sleep(0.40)
    ball_left = Ball(canvas,650,150,'red')
    ball_right = Ball(canvas, 650, 190,'blue')
    ball_left_down = Ball(canvas, 710, 190, 'black')
    ball_right_down = Ball(canvas, 710, 150,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(650,650,710,710,150,190,190,150,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,650,150,'red')
    ball_right = Ball(canvas, 650, 110,'blue')
    ball_left_down = Ball(canvas, 710, 110, 'black')
    ball_right_down = Ball(canvas, 710, 150,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(650,650,710,710,150,110,110,150,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #terminar la 'o'
    #Dibujar la 'B'
    time.sleep(0.40)
    ball_left = Ball(canvas,780,34,'red')
    ball_right = Ball(canvas, 785, 80,'blue')
    ball_left_down = Ball(canvas, 770, 120, 'black')
    ball_right_down = Ball(canvas, 765, 190,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(780,785,770,765,34,80,120,190,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,780,34,'red')
    ball_right = Ball(canvas, 830, 30,'blue')
    ball_left_down = Ball(canvas, 830,110, 'black')
    ball_right_down = Ball(canvas, 775, 100,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(780,830,830,775,34,30,110,100,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,780,95,'red')
    ball_right = Ball(canvas, 830, 60,'blue')
    ball_left_down = Ball(canvas, 830,190, 'black')
    ball_right_down = Ball(canvas, 775, 180,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(780,830,830,775,95,60,190,180,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #terminar la 'B'
    #Dibujar la 'a'
    time.sleep(0.40)
    ball_left = Ball(canvas,830,150,'red')
    ball_right = Ball(canvas, 830, 190,'blue')
    ball_left_down = Ball(canvas, 890, 190, 'black')
    ball_right_down = Ball(canvas, 890, 150,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(830,830,890,890,150,190,190,150,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,830,150,'red')
    ball_right = Ball(canvas, 830, 110,'blue')
    ball_left_down = Ball(canvas, 890, 110, 'black')
    ball_right_down = Ball(canvas, 890, 150,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(830,830,890,890,150,110,110,150,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,890,150,'red')
    ball_right = Ball(canvas, 896, 160,'blue')
    ball_left_down = Ball(canvas, 910, 180, 'black')
    ball_right_down = Ball(canvas, 920, 190,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(890,896,910,920,150,160,180,190,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #terminar la 'a'
    #Dibujar la 'r'
    time.sleep(0.40)
    ball_left = Ball(canvas,935,130,'red')
    ball_right = Ball(canvas, 935, 140,'blue')
    ball_left_down = Ball(canvas, 935, 150, 'black')
    ball_right_down = Ball(canvas, 940, 190,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(935,935,935,940,130,140,150,190,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos 
    time.sleep(0.40)
    ball_left = Ball(canvas,935,155,'red')
    ball_right = Ball(canvas, 960, 115,'blue')
    ball_left_down = Ball(canvas, 980, 115, 'black')
    ball_right_down = Ball(canvas, 994, 132,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(935,960,980,994,155,115,115,132,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #terminar la 'r'
    #Dibujar la segunda 'r'
    time.sleep(0.40)
    ball_left = Ball(canvas,960,160,'red')
    ball_right = Ball(canvas, 960, 170,'blue')
    ball_left_down = Ball(canvas, 960, 180, 'black')
    ball_right_down = Ball(canvas, 960, 190,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(960,960,960,960,160,170,180,190,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,960,160,'red')
    ball_right = Ball(canvas, 979, 140,'blue')
    ball_left_down = Ball(canvas, 985, 130, 'black')
    ball_right_down = Ball(canvas, 994, 132,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(960,979,985,994,160,140,130,132,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #terminar la 'r'
    #Dibujar 'i'
    time.sleep(0.40)
    ball_left = Ball(canvas,1010,130,'red')
    ball_right = Ball(canvas, 1010, 140,'blue')
    ball_left_down = Ball(canvas, 1010, 150, 'black')
    ball_right_down = Ball(canvas, 1010, 190,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(1010,1010,1010,1010,130,140,150,190,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,1010,100,'red')
    ball_right = Ball(canvas, 1000, 100,'blue')
    ball_left_down = Ball(canvas, 1020, 100, 'black')
    ball_right_down = Ball(canvas, 1010, 100,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(1010,1010,1010,1010,100,100,100,100,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #Terminar 'i'
    #Dibujar la 'e'
    time.sleep(0.40)
    ball_left = Ball(canvas,1060,140,'red')
    ball_right = Ball(canvas, 1005, 140,'blue')
    ball_left_down = Ball(canvas, 1005, 190, 'black')
    ball_right_down = Ball(canvas, 1060, 195,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(1060,1005,1005,1060,140,140,190,195,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,1060,140,'red')
    ball_right = Ball(canvas, 1060, 160,'blue')
    ball_left_down = Ball(canvas, 1035, 155, 'black')
    ball_right_down = Ball(canvas, 1035, 155,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(1060,1060,1035,1035,140,160,155,155,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #terminar la 'e'
    #Dibujar la 'n'
    time.sleep(0.40)
    ball_left = Ball(canvas,1060,190,'red')
    ball_right = Ball(canvas, 1060, 130,'blue')
    ball_left_down = Ball(canvas, 1105, 125, 'black')
    ball_right_down = Ball(canvas, 1100, 190,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(1060,1060,1105,1100,190,130,125,190,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #terminar la 'n'
    #Dibujar la 't'
    time.sleep(0.40)
    ball_left = Ball(canvas,1110,40,'red')
    ball_right = Ball(canvas, 1110, 90,'blue')
    ball_left_down = Ball(canvas, 1118, 120, 'black')
    ball_right_down = Ball(canvas, 1100, 190,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(1110,1110,1118,1100,40,90,120,190,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,1075,55,'red')
    ball_right = Ball(canvas, 1095, 55,'blue')
    ball_left_down = Ball(canvas, 1110,55, 'black')
    ball_right_down = Ball(canvas, 1140, 55,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(1075,1095,1110,1140,55,55,55,55,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #terminar la 't'
    #Dibujar la 'o'
    time.sleep(0.40)
    ball_left = Ball(canvas,1115,160,'red')
    ball_right = Ball(canvas, 1115, 200,'blue')
    ball_left_down = Ball(canvas, 1175, 200, 'black')
    ball_right_down = Ball(canvas, 1175, 160,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(1115,1115,1175,1175,160,200,200,160,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,1115,160,'red')
    ball_right = Ball(canvas, 1115, 120,'blue')
    ball_left_down = Ball(canvas, 1175, 120, 'black')
    ball_right_down = Ball(canvas, 1175, 160,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(1115,1115,1175,1175,160,120,120,160,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #terminar la 'o'
    #Dibujar la 's'
    time.sleep(0.40)
    ball_left = Ball(canvas,1210,200,'red')
    ball_right = Ball(canvas, 1290, 185,'blue')
    ball_left_down = Ball(canvas, 1160, 140, 'black')
    ball_right_down = Ball(canvas, 1220, 130,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(1210,1290,1160,1220,200,185,140,130,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #terminar la 's'
    #Dibujar la 'R'
    time.sleep(0.40)
    ball_left = Ball(canvas,1275,34,'red')
    ball_right = Ball(canvas, 1275, 80,'blue')
    ball_left_down = Ball(canvas, 1275, 120, 'black')
    ball_right_down = Ball(canvas, 1275, 190,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(1275,1275,1275,1275,34,80,120,190,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,1275,34,'red')
    ball_right = Ball(canvas, 1335, 30,'blue')
    ball_left_down = Ball(canvas, 1335,110, 'black')
    ball_right_down = Ball(canvas, 1275, 100,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(1275,1335,1335,1275,34,30,110,100,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,1275,105,'red')
    ball_right = Ball(canvas, 1315, 70,'blue')
    ball_left_down = Ball(canvas, 1325,195, 'black')
    ball_right_down = Ball(canvas, 1340, 185,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(1275,1315,1325,1340,105,70,195,185,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #terminar la 'R'
    #Dibujar la 'o'
    time.sleep(0.40)
    ball_left = Ball(canvas,1335,160,'red')
    ball_right = Ball(canvas,1335, 200,'blue')
    ball_left_down = Ball(canvas, 1385, 200, 'black')
    ball_right_down = Ball(canvas, 1385, 160,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(1335,1335,1385,1385,160,200,200,160,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,1335,160,'red')
    ball_right = Ball(canvas, 1335, 120,'blue')
    ball_left_down = Ball(canvas, 1385, 120, 'black')
    ball_right_down = Ball(canvas, 1385, 160,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(1335,1335,1385,1385,160,120,120,160,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #terminar la 'o'
    #dibuja la 'j'
    time.sleep(0.40)
    ball_left = Ball(canvas,1410,160,'red')
    ball_right = Ball(canvas, 1430, 260,'blue')
    ball_left_down = Ball(canvas, 1400, 280, 'black')
    ball_right_down = Ball(canvas, 1360, 290,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(1410,1430,1400,1360,160,260,280,290,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,1410,140,'red')
    ball_right = Ball(canvas, 1400, 140,'blue')
    ball_left_down = Ball(canvas, 1420, 140, 'black')
    ball_right_down = Ball(canvas, 1410, 140,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(1410,1400,1420,1410,140,140,140,140,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #Termina la 'j'
    #Dibujar la 'a'
    time.sleep(0.40)
    ball_left = Ball(canvas,1430,150,'red')
    ball_right = Ball(canvas, 1430, 190,'blue')
    ball_left_down = Ball(canvas, 1480, 190, 'black')
    ball_right_down = Ball(canvas, 1480, 150,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(1430,1430,1480,1480,150,190,190,150,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,1430,150,'red')
    ball_right = Ball(canvas, 1430, 110,'blue')
    ball_left_down = Ball(canvas, 1480, 110, 'black')
    ball_right_down = Ball(canvas, 1480, 150,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(1430,1430,1480,1480,150,110,110,150,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    time.sleep(0.40)
    ball_left = Ball(canvas,1480,150,'red')
    ball_right = Ball(canvas, 1486, 160,'blue')
    ball_left_down = Ball(canvas, 1496, 180, 'black')
    ball_right_down = Ball(canvas, 1500, 190,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(1480,1486,1496,1500,150,160,180,190,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #terminar la 'a'
    #Dibujar la 's'
    time.sleep(0.40)
    ball_left = Ball(canvas,1510,185,'red')
    ball_right = Ball(canvas, 1550, 185,'blue')
    ball_left_down = Ball(canvas, 1460, 120, 'black')
    ball_right_down = Ball(canvas, 1510, 110,'yellow')
    sorteo = sor_color(color)
    mover = hacer_curva(1510,1550,1460,1510,185,185,120,110,0.01,tiempo,tam,sorteo)#llama a la funcion "hacer_curva", y con las cordenas realiza los movimientos
    #terminar la 's'
#Crear la ventana
root = Tk()
text1 =StringVar()
text2 = StringVar()
text3 = StringVar()
root.geometry("2500x500")#tama;o de la ventana
root.title("Bezier Curves")#nombre de la ventana
label = Label(root,text='Ingrese la medida del pixel que desea,(se recomienda del 1 al 10)').pack()#Mensaje en ventana
entry = Entry(root,textvariable=text1).pack()#espacio para escribir texto
label = Label(root,text='Digite "colores" para ver curva por curva de diferente color(random). Sino digite el color en ingles y en minuscula que desea para las curvas(Solo se pueden utilizar los siguientes: white, black, red, green, blue, cyan, yellow, pink)').pack()
entry = Entry(root,textvariable=text2).pack()#espacio para escribir texto
label = Label(root,text='Ingrese la duraccion de cada pixel(tiempo, 1 = un segundo por pixel, asi que se recomienda usar 0.10,0.15...)').pack()
entry = Entry(root,textvariable=text3).pack()#espacio para escribir texto
button = Button(root,text='Acept',command = button ,fg = 'white',bg='black').pack()
canvas = Canvas(root, width=2500, height=500, bd=0, highlightthickness=0)#canvas, para crear los margenes de la ventana
canvas.pack()
root.update()
mainloop()
#Termina la ventana
