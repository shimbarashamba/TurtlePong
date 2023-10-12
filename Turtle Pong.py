import turtle
import functools

def create_players():
    
    # Create player 1
    player1 = turtle.Turtle()
    player1.shape("square")
    player1.shapesize(stretch_wid=2, stretch_len=1, outline=1)
    player1.color("white")
    player1.up()
    player1.goto(300, 0)
    
    # Create player 2
    player2 = turtle.Turtle()
    player2.shape("square")
    player2.shapesize(stretch_wid=2, stretch_len=1, outline=1)
    player2.color("white")
    player2.up()
    player2.goto(-300, 0)
    # Return both players
    return player1, player2

def initiate_ball():
    
    # Create ball
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("white")
    ball.up()
    ball.speed(0)
    ball.degrees(fullcircle=8)
    
    # Return ball
    return ball

def create_walls():
    
    # upper wall
    wall_up = turtle.Turtle()
    wall_up.up()
    wall_up.shape("square")
    wall_up.shapesize(stretch_wid=1, stretch_len=35, outline=1)
    wall_up.color("white")
    wall_up.goto(0,200)
    
    # lower wall
    wall_down = turtle.Turtle()
    wall_down.up()
    wall_down.shape("square")
    wall_down.shapesize(stretch_wid=1, stretch_len=35, outline=1)
    wall_down.color("white")
    wall_down.goto(0,-200)
    
    return wall_up, wall_down


def create_goals():
    
    # left goal
    goal_left = turtle.Turtle()
    goal_left.up()
    goal_left.shape("square")
    goal_left.shapesize(stretch_wid=20, stretch_len=1, outline=1)
    goal_left.color("white")
    goal_left.goto(350,0)
    
    # right goal
    goal_right = turtle.Turtle()
    goal_right.up()
    goal_right.shape("square")
    goal_right.shapesize(stretch_wid=20, stretch_len=1, outline=1)
    goal_right.color("white")
    goal_right.goto(-350,0)
    
    return goal_left, goal_right
    pass

def move_ball(ball):
    # Move ball
    ball.forward(5)

def reset_ball(ball):
    ball.goto(0, 0)
    
def check_hit_player(ball, player):
    
    return ball.distance(player) < 10
    pass

def check_hit_wall_up(ball, wall):
    return ball.ycor() >= wall.ycor()-10

def check_hit_wall_down(ball, wall):
    return ball.ycor() <= wall.ycor()+10

    
def move_up(player):
    if player.pos()[1] < 150:
        player.sety( player.pos()[1] +40)


def move_down(player):
    if player.pos()[1] > -150:
        player.sety( player.pos()[1] -40)
    
    
def create_score(player1_score, player2_score):
    score1 = turtle.Turtle()
    score1.up()
    score1.color("red")
    score1.hideturtle()
    score1.goto(-200,  140)
    score1.write(f"{player1_score}", font=("Verdana",24, "bold"))
    score2 = turtle.Turtle()
    score2.up()
    score2.color("red")
    score2.hideturtle()
    score2.goto(180,  140)
    score2.write(f"{player2_score}", font=("Verdana",24, "bold"))
    
    return score1, score2

def update_score(score1, score2, player1_score, player2_score):
    score1.clear()
    score1.write(f"{player1_score}", font=("Verdana",24, "bold"))
    score2.clear()
    score2.write(f"{player2_score}", font=("Verdana",24, "bold"))

def check_goal_left(ball, goal):
    return ball.xcor() <= goal.xcor()-10

def check_goal_right(ball, goal):
    return ball.xcor() >= goal.xcor()+10

def player1_movement(up, down):
    wn.onkeypress(functools.partial(move_up, player1), up)
    wn.onkeypress(functools.partial(move_down, player1), down)

def player2_movement(up, down):
    wn.onkeypress(functools.partial(move_up, player2), up)
    wn.onkeypress(functools.partial(move_down, player2), down)
    
def change_direction(direction):
    return not direction

def replay():
    return turtle.textinput("Great job, pong champ! Play again?", "Yes or no?")

def start_game():
        return turtle.textinput("Want to play Turtle Pong?", "Yes or no?")

wn = turtle.Screen()
wn.setup(width=750, height=450, startx=0, starty=0)
wn.bgcolor("black")
wn.title("TURTLE PONG")

game_on = start_game()

# The full game loop
while game_on != None and game_on.lower().startswith("y"):
    
    # Clearing the screen before game starts
    turtle.clearscreen()
    
    # Initiating variables before the main game loop
    # Initiating the screen
    wn.setup(width=750, height=450, startx=0, starty=0)
    wn.bgcolor("black")
    wn.title("TURTLE PONG")
    
    # Player scores and max score
    player1_score = 0
    player2_score = 0

    player1_score_draw, player2_score_draw = create_score(player1_score, player2_score)

    max_score = 5


    # Initiating the balls direction
    direction_x = True
    direction_y = False

    # Initiating upper and lower walls
    wall_up, wall_down = create_walls()

    # Initiating left and right goals
    goal_left, goal_right = create_goals()

    # Initiating players
    player1, player2 = create_players()

    # Initiating ball
    ball = initiate_ball()

    # Creating the keybindings for player movement (can be made into a function)

    player1_movement("Up", "Down")
    player2_movement("w", "s")

    # Determines whether the ball can collide with a player or not (this is to prevent 'double-touches')
    player1_active = True
    player2_active = False

    # Listens for input
    wn.listen()


    # Loop for one game of pong
    while player1_score < max_score and player2_score < max_score:

        # Check if the ball touches player 2, which would change the balls direction
        if check_hit_player(ball, player2) and player2_active:
            player2_active = False
            if direction_y:
                ball.setheading(1)
            else:
                ball.setheading(7)
            direction_x = change_direction(direction_x)
            player1_active = True

        # Check if the ball touches player 1, which would change the balls direction
        if check_hit_player(ball, player1) and player1_active:
            player1_active = False
            if direction_y:
                ball.setheading(3)
            else:
                ball.setheading(5)
            direction_x = change_direction(direction_x)
            player2_active = True
        
        # Checks for an upper wall hit
        if check_hit_wall_up(ball, wall_up):
            if direction_x:
                ball.setheading(7)
            else:
                ball.setheading(5)
            direction_y = change_direction(direction_y)

        # Checks for a lower wall hit
        if check_hit_wall_down(ball, wall_down):
            if direction_x:
                ball.setheading(1)
            else:
                ball.setheading(3)
            direction_y = change_direction(direction_y)
        
        # Checks for a goal hit, incrementing the player score
        if ball.pos()[0] > 350:
            reset_ball(ball)
            player1_score += 1
            update_score(player1_score_draw, player2_score_draw, player1_score, player2_score)
        if ball.pos()[0] < -350:
            reset_ball(ball)
            player2_score += 1
            update_score(player1_score_draw, player2_score_draw, player1_score, player2_score)

        # Moves the ball forward in the direction it's facing
        move_ball(ball)
    
    # Ask the player if they want to replay
    game_on = replay()
    
    
wn.mainloop()



