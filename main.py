'''
import turtle as t
import random as r
import time as tm

j = t.Turtle()
j.hideturtle()
j.penup()
j.shape("turtle")
j.color("blue")
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

count = 0

def add(x,y):
 global count
 count = count + 1

def run_game(x,y):
 w.clear()
 w.penup()
 w.goto(400,400)
 st.penup()
 st.hideturtle()
 st.goto(400,400)
 j.showturtle()
 for i in range(1,5):
  x = r.choice(range(-300,300))
  y = r.choice(range(-300,300))
  j.goto(x,y)
 print("You clicked the turtle",  count,  "times!")

j.onclick(add)
st.onclick(run_game)
wn = t.Screen()
wn.mainloop()
'''

user_acnt = input("What is your username? If you do not have one, what would you like it to be?")
accounts = ["ApplePie23","StrayMango38","SSGLowtaper"]

def check_acnt(account):
 