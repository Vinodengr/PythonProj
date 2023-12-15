#Quiz Game
print("Welcome to C Quiz Game")
x = input("Do you want to play the game? ")
if x.lower() != 'yes':
    quit()
c = 0
w = 0

print('Great,Lets Play!')
answer = input("What does CPU stands for? ")
if answer.lower()  == "central processing unit":
    print("Correct, You got it!")
    c +=1
else:
    print("Wrong!")
    w +=1

answer = input("What does GPU stands for? ")
if answer.lower()  == "graphics processing unit":
    print("Correct, You got it!")
    c +=1
else:
    print("Wrong!")
    w +=1


answer = input("What does RAM stands for? ")
if answer.lower()  == "random access memory":
    print("Correct, You got it!")
    c +=1
else:
    print("Wrong!")
    w +=1



answer = input("What does PSU stands for? ")
if answer.lower()  == "power supply":
    print("Correct, You got it!")
    c +=1
else:
    print("Wrong!")
    w +=1

print("You got " + str(c) + " questions correct!")
print("You got " + str(w) + " questions wrong")

print("You got " + str(c/4*100) + " %")