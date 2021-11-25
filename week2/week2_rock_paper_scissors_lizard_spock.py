# Rock-paper-scissors-lizard-Spock template

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random
def name_to_number(name):
    if name == 'rock':
        number = 0
    elif name == 'Spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else:
        return 'inf'
    return number      

def number_to_name(number):
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        name = None
    return name     

def rpsls(player_choice): 
    print('') #empty line
    player_number = name_to_number(player_choice)
    if player_number not in range(0,5):
        '''
        in case of spelling error in input.
        '''
        print 'Give a valid input!'
        return ''
    print'Player chooses', player_choice
    
# Computer's choice    
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    
    if comp_choice == None:
        '''
        in case of wrong random range
        '''
        print 'Check random number range in computer choice.'
        return ''
    print'Computer chooses', comp_choice
    
# After getting valind player number and computer number.
    num_difference = player_number - comp_number
    
# Making negative number fall in the range of 0 to 4.    
    if num_difference < 0:
        num_difference += 5
        
#  Game result:   
    if num_difference == 0:
        print ("Player and computer tie!")
    elif num_difference == 1 or num_difference == 2:
        print 'Player wins!'
    else:
        print 'Computer wins!'

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
# rpsls("scisors")

