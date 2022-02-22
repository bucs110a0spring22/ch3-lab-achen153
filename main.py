import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

mich = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
mich.color('orange')
leonardo.color('blue')
mich.shape('turtle')
leonardo.shape('turtle')

mich.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
mich.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
mich.speed(1)
leonardo.speed(1)
mich.down()
leonardo.down()
mich.forward(random.randrange(0,100))
leonardo.forward(random.randrange(0,100))
mich.goto(-100,20)
leonardo.goto(-100,-20)


for i in range(0,10):
  x = random.randrange(0,10)
  mich.forward(x)
  leonardo.forward(x)
  
# Part B - complete part B here
mich.clear()
leonardo.clear()
sides = [3,4,6,9,12]
mich.down()
length = 30
for i in sides:
  angle = 360/i
  for num in range(i):
    mich.right(angle)
    mich.forward(length)
  mich.clear()

window.exitonclick()
