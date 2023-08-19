#print Hello World!
print("Hello World!")
#write whether people are eligible or not
n= int(input("Enter your age"))
if n > 18:
    print("you can vote")
else:
    print("you cannot vote")
    #loop
names="suvam"
for character in names:
    print(character)
#create an empty set
s=set()
#add number to set 
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)
print(f"The set has {len(s)} numbers")
#series
for i in range(7):
        print(i)
    #dictionaries
Address={"suvam":"Bharatpur7","supriya":"dipjyotitol"}
print(Address["suvam"])
#input and print square of a number
def square(x):
    return x*x
for i in range(10):
    print(f"the square of {i} is {square(i)}")
    