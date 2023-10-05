import random


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

def main():
    print("Welcome to CRICKET GAME!\n")
    print("Toss time!!\n")
    toss()

if __name__ == '__main__':
    main()
