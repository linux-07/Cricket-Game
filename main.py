import random

overs = 0.0
innings = 1
computer_score = 0
computer_wickets = 0
user_score = 0
user_wickets = 0
user_decision = ''
computer_decision = ''

def toss():
    while True:
        user_input = input("Enter your choice (1 for Heads / 2 for Tails): ")
        if user_input == '1':
            user_choice = "heads"
            break
        elif user_input == '2':
            user_choice = "tails"
            break
        else:
            print("Invalid input! Please enter '1' for Heads or '2' for Tails.")

    toss_result = random.choice(['heads', 'tails'])
    
    toss = 'user' if toss_result == user_choice else 'computer'

    if toss == 'user':
        global user_decision, computer_decision
        print("You won the toss!")
        while True:
            user_decision = int(input("Choose to bat (1) or bowl (2): "))
            if user_decision == 1:
                user_decision = 'bat'
                print(f"You chosed to {user_decision} first")
                break
            elif user_decision == 2:
                user_decision = 'bowl'
                print(f"You chosed to {user_decision} first")
                break
            else:
                print("Invalid input! Please choose '1' to bat or '2' to bowl.")
    else:
        print("Computer won the toss!")
        computer_decision = random.choice(['1', '2'])
        computer_decision = 'bat' if computer_decision == '1' else 'bowl'
        print(f"Computer chose to {computer_decision} first.")

def display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings):
    print(f"\nScoreboard: (Inning: {innings})")
    print(f"Your score: {user_score}/{user_wickets}")
    print(f"Computer's score: {computer_score}/{computer_wickets}")
    print(f"Overs bowled: {overs}")

# Condition 1 - user won the toss and choose to bat first
def condition1():
    print("\nBatting time:")
    print("You get 2 overs(12 balls) you need to set a target for the computer.")
    print("If the computer chases the target, the computer wins. If not, you win.")
    print("If both your and computer's score is the same, it's a tie.\n")
    for i in range(2):  # 2 overs
        for j in range(6):  # 6 balls in an over
            if user_wickets == 2:
                break
            overs += 0.1  # Increment the overs by 0.1 at the start of each ball
            print(f"Here comes {int(overs)}.{int((overs - int(overs)) * 10)}")  # Display overs in the desired format
            user_inp = int(input("Enter a number between 1-6 to score: "))
            comp_inp = random.randint(1, 6)
            if user_inp > 6 or user_inp < 0:
                print("Invalid Option selected")
                continue
            else:
                if user_inp == comp_inp:
                    print(f"You are out, {'One more chance' if user_wickets == 1 else 'No more wickets left.'}")
                    user_wickets += 1
                    display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings)                        
                else:
                    user_score += user_inp  # Increment user's score
                    display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings)
    
    print(f"Your batting over, your final score is\n{display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings)}")
    print(f"Computer has a target of {user_score+1} runs!")
    
    print("\nBowling time:")
    for i in range(2):  # 2 overs
        for j in range(6):  # 6 balls in an over
            if computer_score>user_score:
                print("Computer won the match!")
                break
            if computer_wickets == 2:
                break
            overs += 0.1  # Increment the overs by 0.1 at the start of each ball
            print(f"Here comes {int(overs)}.{int((overs - int(overs)) * 10)}")  # Display overs in the desired format
            comp_inp = random.randint(1, 6)
            user_inp = int(input("Enter a number between 1-6 to take wicket: "))
            if user_inp > 6 or user_inp < 0:
                print("Invalid Option selected")
                continue
            else:
                if comp_inp == user_inp:
                    print(f"Computer is out, {'One more chance' if user_wickets == 1 else 'No more wickets left.'}")
                    computer_wickets += 1
                    display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings)                        
                else:
                    computer_score += comp_inp  # Increment computer's score
                    display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings)

    if user_score == computer_score:
        print("The match is a tie!")
    elif computer_score > user_score:
        print("Computer won the match!")
    else:
        print("Congrats, You won the match!!")

# Condition 2 - user won the toss and choose to bowl first
def condition2():
    pass

# Condition 3 - computer won the toss and choose to bat first
def condition2():
    pass

# Condition 4 - computer won the toss and choose to bowl first
def condition2():
    pass


def main():
    print("Welcome to CRICKET GAME!\n")
    print("Toss time!!\n")
    toss()

    # Condition 1 - user won the toss and choose to bat first
    if toss_result == 'user' and user_decision == 'bat':
        condition1()

    # Condition 2 - user won the toss and choose to bowl first
    if toss_result == 'user' and user_decision == 'bowl':
        condition2()

    # Condition 3 - computer won the toss and choose to bat first
    if toss_result == 'user' and user_decision == 'bowl':
        condition3()

    # Condition 2 - computer won the toss and choose to bowl first
    if toss_result == 'user' and user_decision == 'bowl':
        condition4()

if __name__ == '__main__':
    main()
