name = input("Type your name: ")
print("Welcome", name, 'to this adventure!')

ans = input("You are on dirt road which is come to an end. Which way you want to go left or right? ").lower()
if ans == 'left':
    ans = input("You come to a river, you can walk around it or swim across. Type walk/swim ").lower()
    if ans == 'swim':
        print("You swim across and were eaten by aligator")
    elif ans == 'walk':
        print("You walk across several miles and ran out of water")
    else:
        print('Not a valid option. You lost!')
elif ans == 'right':
    ans = input("You come to a bridge, it looks woobly. Do you want to cross it or head back. Type Cross/Back ").lower()    
    if ans == 'back':
        print("Head back!")
    elif ans == 'cross':
        print( "You Won!")
    else:
        print('Not a valid option. You lost!')    
else:
    print('Not a valid option. You lost!')

print("Thanks for trying it,", name,"!")