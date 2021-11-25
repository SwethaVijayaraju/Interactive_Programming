# Example of a simple event-driven program

# CodeSkulptor GUI module
import simplegui

i = 0
# Event handler

def tick1():
    print "1"
    
def tick2():
    print "2"

def ontick():
    print "tick!"
    global i
    i += 1
    if i == 5:
        timer1.stop()
        
def nested_tick():
    print "tick"
    timer = simplegui.create_timer(1000, nested_tick)
    timer.start()


# Register handler
timer1 = simplegui.create_timer(100, tick1)
timer2 = simplegui.create_timer(100, tick2)
# Start timer
timer1.start()
timer2.start()
timer3 = simplegui.create_timer(1000, nested_tick)
timer3.start()
print('done')