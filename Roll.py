import random 
def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val,max_val)
    return roll

while True:
    players = input("Enter Number of Players (1-4) ")
    if players.isdigit():
        players = int(players)
        if players >=1 and players <=4:            
            break
        else:
            print("Must be between 1 and 4")
    else:
        print("Invalid Input: try again ")

max_score = 50

player_scores =[0 for x in range(players)]


while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nplayer_number", player_idx+1 , "your turn has started\n")

        print("Your total score is ", player_scores[player_idx], "\n")
        current_score =0

        while True:
            should_roll = input("Would you like to roll (y) ").lower()
            if should_roll != 'y':
                break
            value = roll()
            if value == 1:
                print("You rolled a one! Your Turn done. ")
                current_score = 0
                break
            else:
                current_score += value
                print( 'You rolled a value: ', value)
            print("Your Score is: ", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is ", player_scores[player_idx])

max_scr = max(player_scores)
winning_idx  = player_scores.index(max_scr)
print("Player ", winning_idx+1, "is the winner with a score of: " ,max_scr)




