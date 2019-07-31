from tkinter import *



def matriz(x1,y1,x2,y2):
    
    if x1 == 0:
        return 0
    else:
        print("ENTRO")
        
        matriz(x1-1,y1-1,x2-1,y2-1,w)
    #w.create_oval(10,30,15,15,width=1, fill="red")
    #w.create_oval(20,70,20,150, fill="blue")
    #w.create_oval(250, 50,50,250, fill="black")
    #w.create_oval(15,5,15,15, fill="pink")
        
master = Tk()
w = Canvas(master, width=700, height=500, background="white")
w.pack()
w.create_line(x1,y1,x2,y2,fill="red",width=20)
mainloop()
