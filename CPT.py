# All the account stuff
# Import random
import random as r
# Lists for accounts and scores tied
# to those accounts by index
accounts = ["ApplePie23","StrayMango38","GrayOwl57","Dxnte_707","sizzle","JB"]
scores = [5, 9, 6, 5, 11, 8]

# Gets user_account
user_acnt = input("What is your username? If you do not have one, what would you like it to be? \n")

# Checks if user_acnt in list of 
# accounts and adds it if not
if user_acnt in accounts:
 print("We found your account!")
else:
 print("We are adding your account now!")
 accounts.append(user_acnt)
 scores.append(0)

# Asks the user what color it wants j
# to be to be used later on
user_color = input("What color would you like the moving turtle to be? \n")
# Got color_list from another student
color_list = ["snow", "ghost white", "white smoke", "gainsboro", "floral white", "old lace", "linen",
    "antique white", "papaya whip", "blanched almond", "bisque", "peach puff", "navajo white",
    "moccasin", "cornsilk", "ivory", "lemon chiffon", "seashell", "honeydew", "mint cream",
    "azure", "alice blue", "lavender", "lavender blush", "misty rose", "white", "dark slate gray", "dim gray", "slate gray", "light slate gray", "gray",
    "light grey", "midnight blue", "navy", "cornflower blue", "dark slate blue", "slate blue",
    "medium slate blue", "light slate blue", "medium blue", "royal blue", "blue", "dodger blue",
    "deep sky blue", "sky blue", "light sky blue", "steel blue", "light steel blue",
    "light blue", "powder blue", "pale turquoise", "dark turquoise", "medium turquoise",
    "turquoise", "cyan", "light cyan", "cadet blue", "medium aquamarine", "aquamarine",
    "dark green", "dark olive green", "dark sea green", "sea green", "medium sea green",
    "light sea green", "pale green", "spring green", "lawn green", "medium spring green",
    "green yellow", "lime green", "yellow green", "forest green", "olive drab", "dark khaki",
    "khaki", "pale goldenrod", "light goldenrod yellow", "light yellow", "yellow", "gold",
    "light goldenrod", "goldenrod", "dark goldenrod", "rosy brown", "indian red",
    "saddle brown", "sienna", "peru", "burlywood", "beige", "wheat", "sandy brown",
    "tan", "chocolate", "firebrick", "brown", "dark salmon", "salmon", "light salmon",
    "orange", "dark orange", "coral", "light coral", "tomato", "orange red", "red", "hot pink",
    "deep pink", "pink", "light pink", "pale violet red", "maroon", "medium violet red",
    "violet red", "magenta", "violet", "plum", "orchid", "medium orchid", "dark orchid",
    "dark violet", "blue violet", "purple", "medium purple", "thistle"]
# Checks if user_color in colorlist 
# and fixes it if not 
if user_color not in color_list:
  user_color = r.choice(color_list)
  print("Your color is not valid so we chose", user_color, "for you!")

# All the game stuff
# Importing turtles
import turtle as t

# Turtle for screen
wn = t.Screen()
wn.bgcolor("black")

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

# Turtle for writing start and point header
w = t.Turtle()
w.pencolor("white")
w.hideturtle()
w.penup()
w.goto(-30,50)
w.write("START", font="Arial")

# Turtle for writing current score
w2 = t.Turtle()
w2.pencolor("white")
w2.hideturtle()
w2.penup()
w2.goto(265,295)

# Turtle for writing the top words
w3 = t.Turtle()
w3.pencolor("white")
w3.hideturtle()
w3.penup()
w3.goto(-155,300)

# Gets a point counter set up
count = 0

# Add function to keep track of 
# points and point counter
def add(x,y):
 global count
 count += 1
 w2.clear()
 w2.write(count, font=("Arial", 15))

# Function for running the game so that 
# after the button is pressed the game runs
def run_game(color,nth):
 j.color(color)
 w.clear()
 w.penup()
 w.goto(200,295)
 st.penup()
 st.hideturtle()
 st.goto(400,400)
 j.showturtle()
 w3.write("Click The Moving Turtle!", font=("Arial", 20))
 w.write("Score:", font =("Arial", 15))
 for i in range(1,5):
  x = r.choice(range(-300,290))
  y = r.choice(range(-300,290))
  j.goto(x,y)
 j.hideturtle()
 w3.clear()
 w3.goto(-150,-20)
 w3.write("GOOD JOB!", font=("DM Sans", 40))
 w.clear()
 w2.clear()
 wn.bgcolor("light slate blue")
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

# Starts game only after start
# button is pressed
st.onclick(lambda x,y: run_game(user_color,nth))

wn.mainloop()