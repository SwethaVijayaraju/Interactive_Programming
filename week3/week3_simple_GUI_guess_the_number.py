import simplegui
import random

# helper function to start and restart the game
def new_game():
    print 
    print "New game. Range is [0,100)"
    global rem_guess 
    rem_guess = 7
    print "Number of remaining guesses is " + str(rem_guess)
    global secret_number
    secret_number = random.randrange(0,100)
    
# define event handlers for control panel
def range100():
    print
    print "New game. Range is [0,100)"
    global rem_guess 
    rem_guess = 7
    print "Number of remaining guesses is " + str(rem_guess)
    global secret_number
    secret_number = random.randrange(0,100)    

def range1000():
    print
    print "New game. Range is [0,1000)"
    global rem_guess 
    rem_guess = 10
    print "Number of remaining guesses is " + str(rem_guess)
    global secret_number
    secret_number = random.randrange(0,1000)    

    
def input_guess(guess):
    print 
    print "Guess was " + guess
    global rem_guess 
    rem_guess -= 1
    print "Number of remaining guesses is " + str(rem_guess)
    if rem_guess > 0:
        entered_number = int(guess)
        if entered_number == secret_number:
            print 'Correct!'
            new_game()
        elif entered_number < secret_number:
            print 'Higher!'
        else:
            print 'Lower!' 
    if rem_guess == 0:
        entered_number = int(guess)
        if entered_number == secret_number:
            print 'Correct!'
            new_game()
        else:
            print 'Oops! Game Over!'
            new_game()

    
# create frame
frame = simplegui.create_frame('Guess', 200, 200, 300)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Your guess:", input_guess, 200)
frame.start()

# call new_game 
new_game()

