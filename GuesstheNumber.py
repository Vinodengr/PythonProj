import random


MaxNum = input("Enter the number:")

if MaxNum.isdigit():
    MaxNum = int(MaxNum)
    if MaxNum < 0:
        print("Enter the number greater than 0")
else:
    print('Input the valid number')

y = random.randint(0,MaxNum)
guesses = 0

while True:
    guesses +=1
    ui = input("Guess the number:")
    if y == int(ui):
        print('You Got it!')        
        break
    elif y < int(ui):
        print("you are the below number")
        continue
    else:
        print('you are the above number')

print("You got it in ", guesses, "guesses")
    