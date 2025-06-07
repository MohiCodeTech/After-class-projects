import turtle
pen = turtle.Turtle()
pen.speed(2)
pen.color("red")
pen.fillcolor("orange")

#equillateral triangle
number_of_sides = 4
horizontal_length = 40
vertical_length = 80

# for i in range(number_of_sides):
#     pen.forward(side_length)
#     pen.right(360 / number_of_sides)

# turtle.done()

#Hexagon
# for i in range(number_of_sides):
#     pen.forward(side_length)
#     pen.right(360 / number_of_sides)

# turtle.done()

#rectangle
pen.forward(vertical_length)
pen.right(360 / number_of_sides)
pen.forward(horizontal_length)
pen.right(360 / number_of_sides)
pen.forward(vertical_length)
pen.right(360 / number_of_sides)
pen.forward(horizontal_length)
pen.right(360 / number_of_sides)

turtle.done()