import math
import turtle

def width_of_triangle(size):
    return 10 * (2**(size-1))

def draw_triangle(t, size, x, y):
    if size == 1:
        t.goto(x, y)
        t.seth(60)

        t.fill(True)
        for i in range(3):
            t.forward(10)
            t.right(120)
        t.fill(False)
    else:
        draw_triangle(t, size-1, x, y)
        draw_triangle(t, size-1, x + (width_of_triangle(size-1) / 2), y + (width_of_triangle(size-1) * math.sqrt(3) / 2))
        draw_triangle(t, size-1, x + width_of_triangle(size-1), y)
        t.goto(x, y)

if __name__ == "__main__":
    window = turtle.Screen()

    bob = turtle.Turtle()
    bob.pencolor("blue")
    bob.fillcolor("green")
    bob.speed(15)

    draw_triangle(bob, 6, 0, 0)

    window.exitonclick()
