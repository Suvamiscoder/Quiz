import random
top_of_range = input("type a Number: ")
if top_of_range.isdigit:
    top_of_range= int(top_of_range)
    if top_of_range<=0:
        print('Please type a number larger than 0 Next time..')
        quit()
else:
     print('Please type a number Next time..')    
     quit()   
                   

random_number= random.randint(0,top_of_range)
guesses=0
while True:
    guesses+=1
    user_guess=input("Guess a Number:  ")
    if user_guess.isdigit:
        user_guess= int(user_guess)
    else:
     print('Please type a number Next time..')    
     continue 

    if user_guess== random_number:
        print("Congrats! You got it!!")
        break
    elif user_guess> random_number:
        print("you were above the Number!")
    else:
        print("you were below the number!")
        print("you got it in" ,guesses,"guesses")            
               
