# Compute a (simplified) Pig Latin version of a word.

###################################################
# Pig Latin formula
def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""
    
    first_letter = word[0]
    rest_of_word = word[1 : ]
    if first_letter == 'a' or first_letter == 'e' or first_letter == 'i' or first_letter == 'o' or first_letter == 'u':
        latin_word = word + 'way'
    else:
        latin_word = rest_of_word + first_letter + 'ay'
        
    return latin_word
    # Student should complete function on the next lines.



###################################################
# Tests
# Student should not change this code.

def test(word):
    """Tests the pig_latin function."""
    
    print pig_latin(word)
    
test("pig")
test("owl")
test("python")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#igpay
#owlway
#ythonpay
