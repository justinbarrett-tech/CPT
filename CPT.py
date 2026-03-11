# All the account stuff
# Lists for accounts and scores tied to those accounts by index
accounts = ["ApplePie23","StrayMango38","GrayOwl57","Dxnte_707","sizzle","JB"]
scores = [5, 9, 6, 5, 11, 5]

# Gets user_account
user_acnt = input("What is your username? If you do not have one, what would you like it to be? \n")

# Checks if user_acnt in list of accounts and adds it if not
if user_acnt in accounts:
 print("We found your account!")
else:
 print("We are adding your account now!")
 accounts.append(user_acnt)
 scores.append(0)

# Asks the user what color it wants j to be
# to be used later on
user_color = input("What color would you like the moving turtle to be? \n")

# All the game stuff
# Importing things
import turtle as t
import random as r

# Define turtles and add characteristics
# Moving/Clicking turtle
j = t.Turtle()
j.hideturtle()
j.penup()
j.shape("turtle")
j.left(90)
j.shapesize(4)
j.speed(1)

# Start button turtle
st = t.Turtle()
st.hideturtle()
st.shape("square")
st.shapesize(5)
st.color("green")
st.showturtle()

# Turtle for writing start
w = t.Turtle()
w.hideturtle()
w.penup()
w.goto(-30,50)
w.write("START", font="Arial")

# Turtle for writing the top words
w2 = t.Turtle()
w2.hideturtle()
w2.penup()
w2.goto(-155,300)

# Gets a point counter set up
count = 0

# Add function to keep track of points
def add(x,y):
 global count
 count = count + 1

# Function for running the game so that 
# after the button is pressed the game runs
def run_game(color,nth):
 j.color(color)
 w.clear()
 w.penup()
 w.goto(400,400)
 st.penup()
 st.hideturtle()
 st.goto(400,400)
 j.showturtle()
 w2.write("Click The Moving Turtle!", font=("Arial", 20))
 for i in range(1,5):
  x = r.choice(range(-300,290))
  y = r.choice(range(-300,290))
  j.goto(x,y)
 print("You clicked the turtle",  count,  "times!")
 ind = accounts.index(user_acnt)
 if count > scores[ind]:
  var = scores[ind]
  scores.remove(var)
  scores.insert(ind,count)
  print("You reached a new highscore!")
 elif count == scores[ind]:
  print("You matched your highscore!")
 else:
  print("You did not reach a new highscore. Your highscore is", scores[ind])

# Helps give another arguement to ensure 
# the code runs when clicked
nth = 0

# Where it calls all the functions
# Adds to points for each click
j.onclick(add)
# Starts game only after st is pressed
st.onclick(lambda x,y: run_game(user_color,nth))
wn = t.Screen()
wn.mainloop()