import turtle


def tree(len, n):
    if n <= 0:
        return
    else:
        turtle.forward(len)
        turtle.left(45)
        tree(len * 0.5, n - 1)
        turtle.right(90)
        tree(len * 0.5, n - 1)
        turtle.left(45)
        turtle.backward(len)


turtle.speed(0)
turtle.delay(0)

tree(200, 99)

turtle.exitonclick()
