import random 

options = [ "rock","paper","scissors"]

user_wins = 0
comp_wins = 0
Tie =0

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to Quit: " ).lower()
    if user_input == 'q':
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # 0 = rock, 1 = paper , 2= scissors
    comp_picks = options[random_number]
    print("Computer Picked" , comp_picks + '.')

    if comp_picks == user_input:
        print("It's a tie")
        Tie +=1
    elif comp_picks == 'rock' and user_input == 'scissors':
        print("You lost!")
        comp_wins +=1
    elif comp_picks == 'paper' and user_input == 'scissors':
        print("You lost!")
        comp_wins +=1
    else:
        print('You Won!')
        user_wins +=1   
    

print("User Wins:" , user_wins , "times.")
print("Computer Wins:" , comp_wins, "times.")
print("Tie:", Tie, "times.")
print("Goodbye!")




