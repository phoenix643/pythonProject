from turtle import Screen,Turtle
from paddles import paddle
from ball import circle
import time

screen = Screen()
paddle_comp = paddle((-350,0))
paddle_p = paddle((350,0))
ball = circle()
line = Turtle(shape = 'square')
line.pencolor('white')
line.color('white')


screen.setup(width = 800, height = 600)
screen.bgcolor('black')
screen.title("pong")
screen.tracer(0)
screen.listen()
line.sety(-320)
line.right(90)
line.forward(30)

while True:
    line.forward(10)
    line.penup()
    line.forward(10)
    line.pendown()
    if line.pos() == (0,320):
        break



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
        print(ball.pos())
    # elif ball.xcor() == 390 and ball.xcor() == -390 :
    #     ball.bouncex()

    
    if ball.xcor() == (paddle_comp.xcor() + 10) and ((ball.ycor() >= paddle_comp.ycor() - 50) and (ball.ycor() <= paddle_comp.ycor() + 50)):
        print(paddle_comp.ycor(), ball.ycor())
        ball.paddle_bouncex()
        
    if ball.xcor() == (paddle_p.xcor() - 10 ) and ((ball.ycor() >= paddle_p.ycor() - 50) and (ball.ycor() <= paddle_p.ycor() + 50)) :
        print(paddle_p.ycor(), ball.ycor())
        ball.paddle_bouncex()
  
    if ball.xcor() > 400 or ball.xcor() < -400:
        game_is_on = False
        print('Game OVer')

    
screen.exitonclick()