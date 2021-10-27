import turtle as trtl
import random

tracy = trtl.Turtle()
wn = trtl.Screen()

tracy.speed(2)
tracy.pensize(5)

tracy.rt(-90)
  
angle = 30
tracy.penup()
tracy.goto(0,-150)
tracy.pendown()


def color():
  list = ["red", "green", "blue", "orange", "brown"]
  index = random.randint(0,4)
  color = list[index]
  tracy.pencolor(color)
  

def branch(size, level):   
    if level > 0:    
        color()      
        tracy.forward(size)
        tracy.right(angle)

        branch(size*0.75, level-1)
        tracy.left(2*angle)

        branch(size*0.75, level-1)
        tracy.right(angle)
        tracy.forward(-size)
          
branch(100, 10)

wn.mainloop()