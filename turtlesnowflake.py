import turtle


def snowflake(length, threshold):
    if length < threshold:
        turtle.forward(length)
    else:
        length = length / 3
        # segment 1
        snowflake(length, threshold)
        turtle.left(60)
        # segment 2
        snowflake(length, threshold)
        turtle.right(120)
        # segment 3
        snowflake(length, threshold)
        turtle.left(60)
        # segment 4
        snowflake(length, threshold)


turtle.speed(0)
turtle.delay(0)

for i in range(3):
    snowflake(300, 10)
    turtle.right(120)

turtle.exitonclick()
