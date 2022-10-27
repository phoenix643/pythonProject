from turtle import Screen,Turtle
from paddles import paddle
from ball import circle
import time

screen = Screen()
paddle_comp = paddle((-350,0))
paddle_p = paddle((350,0))
ball = circle()


screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)
screen.listen()



screen.onkeypress(paddle_p.f,"Up")
screen.onkeypress(paddle_p.b,"Down")
screen.onkeypress(paddle_comp.f,"w")
screen.onkeypress(paddle_comp.b,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bouncey()
    elif ball.xcor() == 390 or ball.xcor() == -390:
        ball.bouncex()
        
screen.exitonclick()