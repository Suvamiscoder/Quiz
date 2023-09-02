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
while True:
    user_guess=input("Guess a Number:  ")
    if user_guess.isdigit:
        user_guess= int(user_guess)
    else:
     print('Please type a number Next time..')    
     continue 

    if user_guess== random_number:
        print("Congrats! You got it!!")
        break
    else:
        print("TRY AGAIN!!  ")
               