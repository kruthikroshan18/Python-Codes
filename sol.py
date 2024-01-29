import random
print("\nHere comes the Toss")
toss = (input("Choose heads or tails: ")).lower()
random_toss = random.randint(0,6)            
random_opt = random.randint(0,6)             
u_opt = 0
c_opt = 0
if random_toss == 1 and toss == "heads":
    print("\nYou won the toss")
    u_opt = (input("Choose bat or ball: ")).lower()
 
elif random_toss == 2 and toss == "tails":
    print("\nYou won the toss")
    u_opt = (input("Choose bat or ball: ")).lower()
else:
    print("\nYou lost the toss")
 
    if random_opt == 1:
        c_opt = "bat"
        print("Computer choose to",c_opt)
 
    elif random_opt == 2:
        c_opt = "ball"
        print("Computer choose to",c_opt)
 
print("\n---------- First Innings Begins ----------")
 
runs_1 = 0
wickets_1 = 0
balls_1 = 0
 
while wickets_1 != 11 and balls_1 != 60:
 
    u_choice = int(input("\nChoose any number from 1 to 6: "))
    c_choice = random.randint(1,6)
 
    if u_choice < 1 or u_choice > 6:
        print("\nPlease choose a value from 1 to 6.")
 
    else:
        print("Your choice: ",u_choice,"\nComputer's choice: ",c_choice)
 
        if u_choice == c_choice:
            wickets_1 += 1
 
        else:
            if u_opt == "bat" or c_opt == "ball":
                Bat_first = "You"
                Ball_first = "Computer"
                runs_1 += u_choice
 
            elif u_opt == "ball" or c_opt == "bat":
                Bat_first = "Computer"
                Ball_first = "You"
                runs_1 += c_choice
 
        print("\nScore =",runs_1,"/",wickets_1)
 
        balls_1 += 1
 
        if balls_1 == 6:
            print("End of Over 1")
 
        elif balls_1 == 12:
            print("End of Over 2")
        
        elif balls_1 == 18:
            print("End of Over 3")
        
        elif balls_1 == 24:
            print("End of Over 4")
            
        elif balls_1 == 30:
            print("End of Over 5")
            
        elif balls_1 == 36:
            print("End of Over 6")
        
        elif balls_1 == 42:
            print("End of Over 7")
            
        elif balls_1 == 48:
            print("End of Over 8")
            
        elif balls_1 == 54:
            print("End of Over 9")
            
        elif balls_1 == 60:
            print("End of Over 10")
 
        print("Balls remaining: ",60 - balls_1)
 
print("\n---------- End of Innings ----------") 
 
print("\nFinal Score:")
print("Runs =",runs_1)
print("wickets =",wickets_1)
 
print("\n",Ball_first,"needs",runs_1 + 1,"runs to win.")
 
# Second Innings 
 
print("\n---------- Second Innings Begins ----------")
 
runs_2 = 0
wickets_2 = 0
balls_2 = 0
 
while wickets_2 != 11 and balls_2 != 60 and runs_2 <= runs_1:
 
    u_choice = int(input("\nChoose any number from 1 to 6: "))
    c_choice = random.randint(1,6)
 
    if u_choice < 1 or u_choice > 6:
        print("\nPlease choose a value from 1 to 6.")
 
    else:
        print("Your choice: ",u_choice,"\nComputer's choice: ",c_choice)
 
        if u_choice == c_choice:
            wickets_2 += 1
 
        else:
            if Bat_first == "Computer": 
                runs_2 += u_choice
                Bat_second = "You"
 
            elif Bat_first == "You":
                runs_2 += c_choice
                Bat_second = "Computer"
 
        print("\nScore =",runs_2,"/",wickets_2)
 
        balls_2 += 1
 
        if balls_2 == 6:
            print("End of Over 1")
 
        elif balls_2 == 12:
            print("End of Over 2")
            
        elif balls_1 == 18:
            print("End of Over 3")
        
        elif balls_1 == 24:
            print("End of Over 4")
            
        elif balls_1 == 30:
            print("End of Over 5")
            
        elif balls_1 == 36:
            print("End of Over 6")
        
        elif balls_1 == 42:
            print("End of Over 7")
            
        elif balls_1 == 48:
            print("End of Over 8")
            
        elif balls_1 == 54:
            print("End of Over 9")
            
        elif balls_1 == 60:
            print("End of Over 10")
 
        if runs_2 <= runs_1 and balls_2 <= 59 and wickets_2 != 11:
            print("To win:",runs_1 - runs_2 + 1,"runs needed from",60 - balls_2,"balls.")
 
print("\n---------- End of Innings ----------") 
 
print("\nFinal Score:")
print("Runs =",runs_2)
print("wickets =",wickets_2)
 
# Result of Match 
 
print("\n~~~~~~~~~~ Result ~~~~~~~~~~")
 
if runs_1 > runs_2:
 
    if Bat_first == "You": 
        print("\nCongratulations! You won the Match by",runs_1 - runs_2,"runs.")
 
    else:
        print("\nBetter luck next time! The Computer won the Match by",runs_1 - runs_2,"runs.") 
 
elif runs_2 > runs_1:
 
    if Bat_second == "You": 
        print("\nCongratulations! You won the Match by",11 - wickets_2,"wickets.")
 
    else:
        print("\nBetter luck next time! The Computer won the Match by",11 - wickets_2,"wickets.")
 
else:
    print("The Match is a Tie.","\nNo one Wins.")