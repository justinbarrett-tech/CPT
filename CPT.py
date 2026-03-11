# All the account stuff

accounts = ["ApplePie23","StrayMango38","GrayOwl57","Dxnte_707","sizzle","JB"]
scores = [5, 9, 6, 5, 11, 11]
user_acnt = input("What is your username? If you do not have one, what would you like it to be? \n")

def check_acnt(account):
 if account in accounts:
  print("We found your account!")
 else:
  print("We are adding your account now!")
  accounts.append(account)
  scores.append(0)

check_acnt(user_acnt)

user_color = input("What color would you like the moving turtle to be? \n")

# All the game stuff
import turtle as t
import random as r
import time as tm

nth = 0


j = t.Turtle()
j.hideturtle()
j.penup()
j.shape("turtle")
j.left(90)
j.shapesize(4)
j.speed(1)

st = t.Turtle()
st.hideturtle()
st.shape("square")
st.shapesize(5)
st.color("green")
st.showturtle()

w = t.Turtle()
w.hideturtle()
w.penup()
w.goto(-30,50)
w.write("START", font="Arial")

w2 = t.Turtle()
w2.hideturtle()
w2.penup()
w2.goto(-155,300)

count = 0

def add(x,y):
 global count
 count = count + 1

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
 else:
  print("You did not reach a new highscore. Your highscore is", scores[ind])

j.onclick(add)
st.onclick(lambda x,y: run_game(user_color,nth))
wn = t.Screen()
wn.mainloop()