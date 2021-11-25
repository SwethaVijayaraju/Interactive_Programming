# Example of a simple event-driven program

# CodeSkulptor GUI module
import simplegui

# Event handler
def tick():
    print "tick!"

# Register handler
timer = simplegui.create_timer(1000, tick)

# simplegui.create_timer(1000, tick).start()

# Start timer
timer.start()
