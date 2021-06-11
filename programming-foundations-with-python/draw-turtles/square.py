import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor('red')

    t = turtle.Turtle()
    t.shape('turtle')
    t.color('yellow')
    t.speed(2)

    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)

    window.exitonclick()

if __name__ == "__main__":
    draw_square()
