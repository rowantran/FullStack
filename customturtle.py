import turtle

def draw_square():
    # Initialize screen
    window = turtle.Screen()
    window.bgcolor("red")

    # Initialize turtle
    bob = turtle.Turtle()
    bob.shape("turtle")
    bob.color("black")
    bob.speed(10)

    bob.forward(100)
    for i in range(3):
        bob.right(90)
        bob.forward(100)

    window.exitonclick()
    
if __name__ == "__main__":
    draw_square()
