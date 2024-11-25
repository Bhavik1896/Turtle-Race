import random
from turtle import Turtle, Screen

screen = Screen()
is_race_on = False
screen.setup(width=800, height=700)
user_bet = screen.textinput(title="Make Your Bet", prompt="Enter the colour of the turtle which you wanna see winning"
                                                          " from green/pink/yellow/red/blue: ").lower()
print(user_bet)

all_turtles = []

if user_bet:
    is_race_on = True

color = ["red", "green", "blue", "orange", "violet", "black"]
y_position = [-90, -60, -30, 0, 30, 60]


for turtle_index in range(0, 6):
    timmy = Turtle(shape="turtle")
    timmy.color(color[turtle_index])
    timmy.penup()
    timmy.goto(x=-330, y=y_position[turtle_index])
    all_turtles.append(timmy)
    

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 310:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You Won by selecting {winning_color} colour")
            else:
                print(f"You have Lost, {winning_color} has won")
                turtle.goto(-250, 0)
                turtle.hideturtle()
                turtle.write(f"You Won by selecting {winning_color} colour", align="left", font=('Arial', 38, 'normal'))
        
        random_distance = random.randint(0, 40)
        turtle.forward(random_distance)


screen.exitonclick()


