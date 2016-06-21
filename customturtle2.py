import turtle

def draw_square():
    bob = turtle.Turtle()
    bob.color("yellow")
    
    for i in range(4):
        bob.right(90)
        bob.forward(100)

def draw_circle():
    bob = turtle.Turtle()
    bob.color("black")
    
    bob.circle(100)

def draw_triangle():
    bob = turtle.Turtle()
    bob.color("blue")

    # Make turtle face east
    bob.seth(0)
    for i in range(3):
        bob.forward(100)
        bob.left(120)

if __name__ == "__main__":
    window = turtle.Screen()
    window.bgcolor("red")

    draw_square()
    draw_circle()
    draw_triangle()

    window.exitonclick()
