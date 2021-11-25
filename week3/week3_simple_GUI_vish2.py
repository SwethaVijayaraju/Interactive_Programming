# Example of a simple event-driven program

# CodeSkulptor GUI module
import simplegui

def tick():
    print "tik"
    timer2.start()
    timer1.stop()
    
    
def tok():
    print "tok"
    timer1.start()
    timer2.stop()

# Register handler
timer1 = simplegui.create_timer(1000, tick)
timer2 = simplegui.create_timer(1000, tok)

timer1.start()
