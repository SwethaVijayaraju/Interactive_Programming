# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2]
paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT/2]
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0

def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == 'RIGHT':
        ball_vel = [random.randrange(120, 240)/60,  - random.randrange(60, 180)/60]   
    elif direction == 'LEFT':
        ball_vel = [-random.randrange(120, 240)/60,  -random.randrange(60, 180)/60] 

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2
    score1 = 0
    score2 = 0
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT/2]
    spawn_ball('RIGHT')

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if ball_pos[1] not in range((paddle1_pos[1] - HALF_PAD_HEIGHT), (paddle1_pos[1] + HALF_PAD_HEIGHT + 1)):
            score2 += 1
            spawn_ball('RIGHT')
        else:
            ball_vel[0] = - ball_vel[0]
    if ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        if ball_pos[1] not in range((paddle2_pos[1] - HALF_PAD_HEIGHT), (paddle2_pos[1] + HALF_PAD_HEIGHT + 1)):
            score1 += 1
            spawn_ball('LEFT')
        else:
            ball_vel[0] = - ball_vel[0]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, 'White', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos[1] - HALF_PAD_HEIGHT], [PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT], [PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT], [0, paddle1_pos[1] + HALF_PAD_HEIGHT]], 1, 'Yellow', 'Orange')
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT], [WIDTH - PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT]], 1, 'Yellow', 'Orange')    
    
    # determine whether paddle and ball collide 
    
    # draw scores
    canvas.draw_text(str(score1), [250, 50], 40, 'White')
    canvas.draw_text(str(score2), [340, 50], 40, 'White') 
    
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    if key == simplegui.KEY_MAP['W']:
        if paddle1_pos[1] > HALF_PAD_HEIGHT:
            paddle1_pos[1] -= 40
    elif key == simplegui.KEY_MAP['S']:
        if paddle1_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
            paddle1_pos[1] += 40
    elif key == simplegui.KEY_MAP['up']:
        if paddle2_pos[1] > HALF_PAD_HEIGHT:
            paddle2_pos[1] -= 40
    elif key == simplegui.KEY_MAP['down']:
        if paddle2_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
            paddle2_pos[1] += 40
        
def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', new_game, 100)
frame.set_keydown_handler(keydown)


# start frame
new_game()
frame.start()
