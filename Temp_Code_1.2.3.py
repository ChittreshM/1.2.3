# a123_apple_1.py
import turtle as trtl
import random as rand

# -----setup-----
apple_image = "apple.gif"  # Store the file name of your shape
pear_image = "pear.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)  # Make the screen aware of the new file
wn.addshape(pear_image)
wn.bgpic("background.gif")

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', "L", 'M', 'N', 'O']
appleList = []
appleLetters = []

# Create turtles for apples and assign random letters to them
for i in range(5):
    tempApple = trtl.Turtle()
    appleList.append(tempApple)
    appleLetters.append(rand.choice(letters))

# -----functions-----
# Given a turtle, set that turtle to be shaped by the image file
def draw_apple(index):
    global appleLetter
    appleList[index].penup()
    # Use pear image if index is greater than 2, otherwise use apple image
    if index > 2:
        appleList[index].shape(pear_image)
    else:
        appleList[index].shape(apple_image)
    wn.tracer(False)
    # Set the position of the apple randomly
    appleList[index].setx(rand.randint(-140, 140))
    appleList[index].sety(rand.randint(-25, 90))

    appleList[index].sety(appleList[index].ycor() - 30)
    appleList[index].color("white")
    # Write the corresponding letter on the apple
    appleList[index].write(appleLetters[index], align="center", font=("Arial", 40, "bold"))
    appleList[index].sety(appleList[index].ycor() + 30)
    appleList[index].showturtle()
    wn.tracer(True)
    wn.update()

# Function to drop the apple (move it to the bottom and change the letter)
def drop_apple(index):
    appleList[index].penup()
    appleList[index].clear()
    appleList[index].goto(appleList[index].xcor(), -150)
    appleList[index].hideturtle()
    appleLetters[index] = rand.choice(letters)
    draw_apple(index)

# Functions for each letter to check and drop corresponding apples
def typedA():
  for i in range(5):
    if appleLetters[i] == 'A':
      drop_apple(i)

def typedB():
  for i in range(5):
      if appleLetters[i] == 'B':
        drop_apple(i)

def typedC():
  for i in range(5):
    if appleLetters[i] == 'C':
      drop_apple(i)

def typedD():
  for i in range(5):
    if appleLetters[i] == 'D':
      drop_apple(i)

def typedE():
  for i in range(5):
    if appleLetters[i] == 'E':
      drop_apple(i)

def typedF():
  for i in range(5):
    if appleLetters[i] == 'F':
      drop_apple(i)

def typedG():
  for i in range(5):
    if appleLetters[i] == 'G':
      drop_apple(i)

def typedH():
  for i in range(5):
    if appleLetters[i] == 'H':
      drop_apple(i)

def typedI():
  for i in range(5):
    if appleLetters[i] == 'I':
      drop_apple(i)

def typedJ():
  for i in range(5):
    if appleLetters[i] == 'J':
      drop_apple(i)
    
def typedK():
  for i in range(5):
    if appleLetters[i] == 'K':
      drop_apple(i)

def typedL():
  for i in range(5):
    if appleLetters[i] == 'L':
      drop_apple(i)

def typedM():
  for i in range(5):
    if appleLetters[i] == 'M':
      drop_apple(i)

def typedN():
  for i in range(5):
    if appleLetters[i] == 'N':
      drop_apple(i)

def typedO():
  for i in range(5):
    if appleLetters[i] == 'O':
      drop_apple(i)

# (similar functions for other letters)

# -----function calls-----

# Draw initial set of apples
for i in range(5):
    draw_apple(i)

# Set up keypress listeners for each letter
wn.onkeypress(typedA, 'A')
wn.onkeypress(typedB, 'B')
wn.onkeypress(typedC, 'C')
wn.onkeypress(typedD, 'D')
wn.onkeypress(typedE, 'E')
wn.onkeypress(typedF, 'F')
wn.onkeypress(typedG, 'G')
wn.onkeypress(typedH, 'H')
wn.onkeypress(typedI, 'I')
wn.onkeypress(typedJ, 'J')
wn.onkeypress(typedK, 'K')
wn.onkeypress(typedL, 'L')
wn.onkeypress(typedM, 'M')
wn.onkeypress(typedN, 'N')
wn.onkeypress(typedO, 'O')

wn.listen()

wn.mainloop()


