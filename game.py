#importing stuff
import turtle
import time
wn = turtle.Screen()
wn.title('Boring game')
wn.bgcolor('black')
wn.setup(width=600, height=600)
wn.tracer(0)
ball = turtle.Turtle()
start_game = turtle.Turtle()
start_game.speed(0)
start_game.color('white')
start_game.penup()
start_game.hideturtle()
start_game.goto(0,0)
start_game.write('Press s to start and q to quit', align='center', font=('Courier', '30', 'bold'))
x = 1
# starting the game
def game():
    start_game.clear()
    ball.speed(0)
    ball.shape('square')
    ball.color('white')
    ball.penup()
    ball.goto(0, 0)
# changing directions
def up():
    ball.setheading(90)
def down():
    ball.setheading(270)
def left():
    ball.setheading(180)
def right():
    ball.setheading(0)
def quit_game():
    wn.bye()
# keyboard presses
wn.listen()
wn.onkey(game, 's')
wn.onkey(up, 'Up')
wn.onkey(down, 'Down')
wn.onkey(left, 'Left')
wn.onkey(right, 'Right')
wn.onkey(quit_game, 'q')

while True:
    # kinda like wn.mainloop()
    wn.update()
    #setting the ball speed
    ball.forward(x)
    # checking collisions
    if ball.ycor() > 278:
        time.sleep(1)
        ball.goto(0, 0)
        x *= 2

    if ball.ycor() < -278:
        time.sleep(1)
        ball.goto(0, 0)
        x *= 2

    if ball.xcor() > 278:
        time.sleep(1)
        ball.goto(0, 0)
        x *= 2


    if ball.xcor() < -278:
        time.sleep(1)
        ball.goto(0, 0)
        x *= 2
