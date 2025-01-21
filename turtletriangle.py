import turtle


def triangle(length, threshold):
    if length < threshold:
        return
    else:
        for i in range(3):
            turtle.forward(length)
            triangle(length / 2, threshold)
            turtle.backward(length)
            turtle.left(120)


turtle.speed(0)
turtle.delay(0)
triangle(100, 25)

turtle.exitonclick()
