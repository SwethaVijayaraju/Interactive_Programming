import simplegui

number = 217
def collatz(n_number):
    global number
    if n_number%2 == 0:
        number = n_number/2
        print number
    else:
        number = (n_number*3) + 1
        print number      
def tick():
    if number == 1:
        timer.stop()
        return
    collatz(number)
# frame = simplegui.create_frame("Collatz", 300, 300)
timer = simplegui.create_timer(500, tick)
timer.start()

