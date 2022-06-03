
import random
print ('Hello, this is Rock, Paper, Scissor  Game for you!')
print('Instrucions')
print('Choose R for Rock')
print('Choose P for Paper')
print('Choose S for Scissor')

again_ = 1
while again_ == 1:

    inputerror = 0
    tie = 0
    possible_actions = ["R", "P", "S"] 
    CPU = random.choice(possible_actions)      
    player = input ('Please enter one of the following: "R","P","S":')
    print(f"\nPlayer :({player}), CPU:( {CPU}).\n")

    #check if player input is found in list array
    if player not in possible_actions:
        inputerror = 1
        while inputerror == 1:
            print ('Invalid choice!')
            player = input('Please enter one of the following: "R","P","S":')
            if player in possible_actions:
                playererror = 0
                break
            else:
                continue
         
    #Determine the winner:

        # The case of a tie

        if player == CPU:
            tie = 1
            while tie == 1:
                print ('Its a tie! You guys have both chosen:', player)
                player = input('Please enter one of the following: "R","P","S":')
            
                if player not in possible_actions:
                    inputerror = 1
                    while inputerror == 1:
                        print ('Invalid choice!')
                        player = input('Please enter one of the following: "R","P","S":')
                        if player  in possible_actions:
                            inputerror = 0
                            break
                        else:
                            continue
       
                 #Decide for tie           
                if player == CPU:
                    tie = 1
                    continue
                else:
                    tie = 0
                    break

        # The case of a winner
        
    if player == "R":
        if CPU == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player == "P":
        if CPU == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player == "S":
        if CPU == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
            
    again = input('Would you like to play once again?(yes/no)')
    if again == 'yes':
        again_ = 1
        
    else:
        print ('Thank you for playing :)')
        again_ = 0