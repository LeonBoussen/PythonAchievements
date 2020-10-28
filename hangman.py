import time
import os

os.system("cls")

print("Welcome player"'\n')
time.sleep(2)
print("Player 1 has to give a word and player 2 has to guess the word"'\n')
time.sleep(5)
os.system("cls")
name = input("What is your name player 1? "'\n'"Type your name here : ")
os.system("cls")
print("Hello",name,"nice to meet you")
time.sleep(5)
os.system("cls")
name2 = input("Hello player 2, and what is your name?"'\n'"Type Your name here : ")
os.system("cls")
print("Hello",name2,"good to meet you")
time.sleep(5)
os.system("cls")
print(name,"is going to choose a word for you",name2,"to solve")
time.sleep(7)

word = input(name +"type here the word : ")
os.system("cls")

print("this is the word you chose",word)
time.sleep(5)
os.system("cls")

print("Start guessing...")
time.sleep(0.5)

guesses = ''

turns = 12


while turns > 0:         

    failed = 0    
    os.system("cls")    

    for char in word:      

        if char in guesses:    
    
            print(char,)    

        else:
    
            print ("_",)     
       
            failed += 1    

    if failed == 0:        
        print('\n'"You won")
        time.sleep(5)
        exit()

        break              

    print("")
    
    print("You have",turns,"more turns")
    guess = input("guess a letter : ") 
    

    guesses += guess                    

    if guess not in word:  
 
        turns -= 1        
 
        print ("Wrong")    
        os.system("cls")
        
        
 

        if turns == 0:           
    
            print ('\n'"You Lose")  
            time.sleep(5)
            exit()