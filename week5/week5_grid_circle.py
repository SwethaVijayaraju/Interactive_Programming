# Ball grid slution

###################################################
# Student should enter code below

import simplegui

BALL_RADIUS = 20
GRID_SIZE = 10
WIDTH = 2 * GRID_SIZE * BALL_RADIUS
HEIGHT = 2 * GRID_SIZE * BALL_RADIUS


# define draw
def draw(canvas): 
    BALL_RAD = 20
    for i in range(GRID_SIZE):
        j = 0
        for k in range(GRID_SIZE):
            ball_pos = [j+BALL_RADIUS, BALL_RAD]
            canvas.draw_circle(ball_pos, BALL_RADIUS, 2, 'White', 'White')
            j += 40
        BALL_RAD += 40
        
# create frame and register handlers
frame = simplegui.create_frame("Ball grid", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# start frame
frame.start()

