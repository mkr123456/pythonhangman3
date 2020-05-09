#importing the time module
import time

#welcoming the user
name = input ("What is your name? ")

print (" Hello, " + name, "Time to play hangman!") 

print ("  ")

#wait for 1 second
time.sleep(1)

print ("Start guessing...")
time.sleep(0.5)

#here we set the hangman word - I'm choosing purple but we can choose 
# any word - for this project im using 6 characters
word = "purple"

#creates a variable with an empty value
guesses = ''

#determines the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for char in word:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # if letter is a correct guess - then print character
            print (char, )
        else:
    
        # if not found, print a dash
            print ("_", )    
       
        # and increase the failed counter with one
            failed += 1    

    # print You Won
    if failed == 0:        
        print ( " You won" ) 

    # exit the script
        break              

    print

    # ask the user to guess a character
    guess = input("guess a character:") 

    # set the players guess to guesses, for correct grammar
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 with each guess
        turns -= 1        
 
    # print wrong if letter is not in puzzle
        print (" Wrong")
 
    # how many turns are left
        print ("You have", + turns, 'more guesses' )
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Lose"
            print ("You Lose")