import turtle


def play(len, n):
    if n <= 0:
        return
    else:
        turtle.forward(len)
        turtle.left(45)
        play(len * 0.5, n - 1)
        play(len * 0.5, n - 1)
        turtle.left(45)
        turtle.backward(len)


turtle.speed(0)
turtle.delay(0)

for i in range(4):
    play(60, 8)


turtle.exitonclick()
