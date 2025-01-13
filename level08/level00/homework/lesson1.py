from turtle import *


#we want to paint a house
speed(7)
#step 1:  draw a square
width(7)
color("green")

forward(200)
left(90)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square 

#drawing a door 

forward(70)
color ("black")
begin_fill()
left(90)
forward(100)   #height of the door 
right(90)
forward(60)
right(90)
forward(100)
end_fill()
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#drawing a windows 

penup()
goto(180, 180)
pendown()
left(30)
color ("blue")
begin_fill()
forward(60)
right(90)
forward(40)
right(90)
forward(60)
right(90)
forward(40)
end_fill()
penup()
goto(20, 180)
pendown()
forward(40)
begin_fill()
right(90)
forward(60)
right(90)
forward(40)
right(90)
forward(60)
end_fill()

#end of house
exitonclick()