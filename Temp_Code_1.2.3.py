######### ALL CODE GOES HERE###########
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)

apple = trtl.Turtle()
drawer = trtl.Turtle()
drawer.hideturtle()

#coordinates of positions
x_pos = apple.xcor()
y_pos = apple.ycor()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_fruit(active_fruit):
  active_fruit.shape(apple_image)
  wn.update()

def drop_down():
  if apple.ycor() > -150:
    apple.penup()
    apple.goto(0, -150)

    drawer.clear() 
    drawer.goto(-10,-150-32)
    drawer.write("D", font = ("Arial", 30, "normal"))

def draw_letter():
  drawer.penup()
  drawer.hideturtle()
  drawer.goto(-10, -30)
  drawer.write("D", font = ("Arial", 30, "normal"))

#-----function calls-----
draw_fruit(apple)
draw_letter()

wn.onkeypress(drop_down, "d")
wn.listen()

wn.mainloop()

