from turtle import Turtle

class circle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.home()
        self.movex = 10
        self.movey = 10
       
        
    def move(self):
        newx = self.xcor() + self.movex
        newy = self.ycor() + self.movey
        self.goto(newx,newy) 
        
        
    def bouncex(self):
        self.movex *= -1
        
    def bouncey(self):
        self.movey *= -1
            
    def paddle_bouncex(self):
        self.movex *= -1
    def paddle_bouncey(self):
        self.movey *= -1
        
            
       
    
        
        
        
    
            
            
            
            