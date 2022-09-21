from tkinter import *
root = Tk()
canv = Canvas(bg="white", width=1000,height=1000)  
canv.pack()
def click(event):	
  canv.create_oval((event.x, event.y, event.x+20, event.y+20),  width=0,  fill='black')
  xp = event.x
  yp = event.y
  xp = str(xp)+'\n'
  yp = str(yp)
  f = open('tt.txt','w')
  xp = f.write(xp)
  yp = f.write(yp)
  f.close
  canv.bind("<B1-Motion>", onmotion)
def onmotion(event):
  f = open(r'tt.txt')
  xp = f.readlines()	
  xp[0] = int(xp[0])+10
  xp[1] = int(xp[1])+10	
  f.close
  canv.create_oval((event.x, event.y, event.x+20, event.y+20),  width=0,  fill='black')
  canv.create_line(xp[0], xp[1], event.x+10, event.y+10,width=20, fill='black')
  xp = event.x
  yp = event.y
  xp = str(xp)+'\n'
  yp = str(yp)
  f = open('tt.txt','w')
  xp = f.write(xp)
  yp = f.write(yp)
  f.close	
canv.bind("<Button-1>", click)
root.mainloop()