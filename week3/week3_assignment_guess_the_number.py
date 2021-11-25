import simplegui
import random

# helper function to start and restart the game
def new_game():
    global end_range, rem_guess, secret_number
    if end_range == 100:
        rem_guess = 7
    else:
        rem_guess = 10
    print "New game. Range is [0, " + str(end_range) + ")"
    print "Number of remaining guesses is " + str(rem_guess)
    secret_number = random.randrange(0, end_range) 
    
# define event handlers for control panel
def range100():
    print
    global end_range,rem_guess
    end_range = 100
    new_game() 

def range1000():
    print
    global end_range,rem_guess
    end_range = 1000
    new_game()
    
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
            print
            new_game()
        elif entered_number < secret_number:
            print 'Higher!'
        else:
            print 'Lower!' 
    if rem_guess == 0:
        entered_number = int(guess)
        if entered_number == secret_number:
            print 'Correct!'
            print
            new_game()
        else:
            print 'Oops! Game Over!'
            print
            new_game()

    
# create frame
frame = simplegui.create_frame('Guess', 200, 200, 300)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Your guess:", input_guess, 200)
frame.start()

# call new_game
end_range = 100
new_game()

