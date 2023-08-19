print('Welcome to my Quiz Game')
playing= input("Do You want to play?  ")
if playing.lower() !='yes':
    quit()
print('Okay! Lets play :)')
score=0
answer=input('Who is the president of India?   ')

if answer.lower()=="droupadi murmu":
    print('Correct Answer!')
    score+=1
else:
    print("Wrong Answer!!   Try Again..")
answer=input('Which country has the highest mountain in the world?')

if answer.lower()=="nepal":
    print('Correct Answer!')
    score+=1
else:
    print("Wrong Answer!!   Try Again..")
answer=input('Which is the highest mountaion in the world?')

if answer.lower()=="mount everest":
    print('Correct Answer!')
    score+=1
else:
    print("Wrong Answer!!   Try Again..")
answer=input('who is the prime minister of India?')

if answer.lower()=="narendra modi":
    print('Correct Answer!')
    score+=1
else:
    print("Wrong Answer!!   Try Again..")
answer=input('who is the prime minister of India?')

if answer.lower()=="Narendra Modi":
    print('Correct Answer!')
    score+=1
else:
    print("Wrong Answer!!   Try Again..")
answer=input('who is the prime minister of India?')

if answer.lower()=="Narendra Modi":
    print('Correct Answer!')
    score+=1
else:
    print("Wrong Answer!!   Try Again..")
    
    print("You got "+ str(score)+ "marks")
