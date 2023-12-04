######### ALL CODE GOES HERE###########
import turtle as trtl
import random

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"

picked_letter_list = []
turtle_list = []
letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
tree_x1 = -200
tree_x2 = 200
tree_y1 = 0
tree_y2 = 125

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)

fruit1 = trtl.Turtle()
fruit1.penup()
turtle_list.append(fruit1)
fruit2 = trtl.Turtle()
fruit2.penup()
turtle_list.append(fruit2)
fruit3 = trtl.Turtle()
fruit3.penup()
turtle_list.append(fruit3)
fruit4 = trtl.Turtle()
fruit4.penup()
turtle_list.append(fruit4)
fruit5 = trtl.Turtle()
fruit5.penup()
turtle_list.append(fruit5)

drawer1 = trtl.Turtle()
drawer1.hideturtle()
drawer1.penup()
drawer2 = trtl.Turtle()
drawer2.hideturtle()
drawer2.penup()
drawer3 = trtl.Turtle()
drawer3.hideturtle()
drawer3.penup()
drawer4 = trtl.Turtle()
drawer4.hideturtle()
drawer4.penup()
drawer5 = trtl.Turtle()
drawer5.hideturtle()
drawer5.penup()

letter1 = ""
letter2 = ""
letter3 = ""
letter4 = ""
letter5 = ""

#coordinates of positions
# x_pos = apple.xcor()
# y_pos = apple.ycor()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def letter_pick():
  if len(letter_list) == 0:
    return 
  letter1 = random.choice(letter_list)
  print('q')
  letter_list.remove(letter1)
  if len(letter_list) == 0:
    return
  letter2 = random.choice(letter_list)
  print('q')
  letter_list.remove(letter2)
  if len(letter_list) == 0:
    return
  letter3 = random.choice(letter_list)
  print('q')
  letter_list.remove(letter3)
  if len(letter_list) == 0:
    return
  letter4 = random.choice(letter_list)
  print('q')
  letter_list.remove(letter4)
  if len(letter_list) == 0:
    return
  letter5 = random.choice(letter_list)
  print('q')
  letter_list.remove(letter5)
  if len(letter_list) == 0:
    return letter1

def draw_fruits():
  letter_pick()
  print(letter1)
  print(letter2)
  print(letter3)
  print(letter4)
  print(letter5)
  # letter1 = random.choice(letter_list)
  # letter_list.remove(letter1)
  # letter2 = random.choice(letter_list)
  # letter_list.remove(letter2)
  # letter3 = random.choice(letter_list)
  # letter_list.remove(letter3)
  # letter4 = random.choice(letter_list)
  # letter_list.remove(letter4)
  # letter5 = random.choice(letter_list)
  # letter_list.remove(letter5)
  
  for active_turtle in turtle_list:
    shape = random.randint(0, 1)
    if shape == 0:
      active_turtle.shape(apple_image)
    elif shape == 1:
      active_turtle.shape(pear_image)
    
  fruit1.goto(random.randint(-200, -120), random.randint(50, 80))
  fruit1pos = fruit1.pos()
  drawer1.goto(fruit1pos[0] - 10, fruit1pos[1]- 30)
  drawer1.write(letter1, font = ("Arial", 50, "bold"))
  
  fruit2.goto(random.randint(-120, -40), random.randint(tree_y1, tree_y2))
  fruit2pos = fruit2.pos()
  drawer2.goto(fruit2pos[0] - 10, fruit2pos[1]- 30)
  drawer2.write(letter2, font = ("Arial", 50, "bold"))
  
  fruit3.goto(random.randint(-40, 40), random.randint(tree_y1, tree_y2))
  fruit3pos = fruit3.pos()
  drawer3.goto(fruit3pos[0] - 10, fruit3pos[1]- 30)
  drawer3.write(letter3, font = ("Arial", 50, "bold"))
  
  fruit4.goto(random.randint(40, 120), random.randint(tree_y1, tree_y2))
  fruit4pos = fruit4.pos()
  drawer4.goto(fruit4pos[0] - 10, fruit4pos[1]- 30)
  drawer4.write(letter4, font = ("Arial", 50, "bold"))
  
  fruit5.goto(random.randint(120, 200), random.randint(50, 80))
  fruit5pos = fruit5.pos()
  drawer5.goto(fruit5pos[0] - 10, fruit5pos[1]- 30)
  drawer5.write(letter5, font = ("Arial", 50, "bold"))
  

# def drop_down():
#   if apple.ycor() > -150:
#     apple.penup()
#     apple.goto(0, -150)

    # drawer.clear() 
    # drawer.goto(-10,-150-32)
    # drawer.write("D", font = ("Arial", 30, "normal"))

# def draw_letter():
#   drawer.penup()
#   drawer.hideturtle()
#   drawer.goto(-10, -30)
#   drawer.write("D", font = ("Arial", 30, "normal"))

#-----function calls-----
# draw_fruit(apple)
# draw_letter()
draw_fruits()
draw_fruits()
draw_fruits()
draw_fruits()
draw_fruits()
draw_fruits()
# wn.onkeypress(drop_down, "d")
wn.listen()

wn.update()
wn.mainloop()

