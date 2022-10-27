from turtle import Turtle

class paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.setpos(position)
        self.penup()
        self.shape("square")
        self.color("White")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        
    def f(self):
        self.forward(15)
        
    def b(self):
        self.backward(15)
   
        


