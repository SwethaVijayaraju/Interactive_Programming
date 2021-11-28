# Move a ball

###################################################
# Student should add code where relevant to the following.


import simplegui 

# Define globals - Constants are capitalized in Python
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20

# Draw handler
def draw(canvas):
    if ball_radius > (HEIGHT / 2) or ball_radius <=0 :
        canvas.draw_text('Radius out of range', [100,200], 30, 'White')
    else:
        canvas.draw_circle((200, 200), ball_radius, 2, 'White', 'White')

# Event handlers for buttons
def increase_radius():
    global ball_radius
    if (ball_radius + RADIUS_INCREMENT) > (HEIGHT / 2):
        print 'radius out of range'
    else:
        ball_radius += RADIUS_INCREMENT
def decrease_radius():
    global ball_radius
    if ball_radius <= RADIUS_INCREMENT:
        print 'radius out of range'
    else:
        ball_radius -= RADIUS_INCREMENT

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("Increase radius", increase_radius, 100)
frame.add_button("Decrease radius", decrease_radius, 100)


# Start the frame animation
frame.start()

