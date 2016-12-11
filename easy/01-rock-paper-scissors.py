from random import randint
from sys import exit

choices = ('Rock', 'Paper', 'Scissors')
summary = []
print ("Choose (r)ock, (p)aper, (s)cissors or (q)uit game.")

def main():
    choice = 0
    while True:
        choice = ask_choice()
        if (choice == -1):
            game_summary()
            break
        else: check_game(choice)


#Asks for user's input
def ask_choice():
    while True:
        choice = raw_input("\nEnter your choice> ").lower()[0]

        if choice not in ('r', 'p', 's', 'q'):
            print('Please try again.')
            continue

        elif choice == 'q':
            return -1

        else:
            return {'r': 0, 'p': 1, 's': 2} [choice]


#Checks who wins the game and adds to the summary
def check_game(usr_choice):
    cmp_choice = randint(0,2)
    diff = (usr_choice - cmp_choice) % 3

    print("Your choice = " + choices[usr_choice] + ". Computer's choice = " + choices[cmp_choice])

    if diff == 1:
        print(choices[usr_choice] + " beats " + choices[cmp_choice].lower() + ". You win!")
        summary.append('w')

    elif diff == 2:
        print(choices[cmp_choice] + " beats " + choices[usr_choice].lower() + ". You lost!")
        summary.append('l')

    else:
        print("Both chose " + choices[usr_choice] + ". Draw!")
        summary.append('d')


#Displays the final result
def game_summary():
    g = len(summary)
    w = summary.count('w')
    d = summary.count('d')
    l = g - w - d

    #Checks whether total games is zero. If not, proceeds to display the summary.
    if(g != 0):
        print("\nTotal games: " + str(g))
        print("Wins: " + str(w) + " || Losses: " + str(l) + " || Draws: " + str(d))


        if w > l:
            print("\nThank you for playing. You won!")
        elif w < l:
            print("\nThank you for playing. You lost!")
        else:
            print("\nThank you for playing. You drew!")
    else:
        print("\nYou quit without playing a game. Try again (Y/N)?")
        main() if raw_input().lower() == 'y' else exit()


if __name__ == "__main__":main()
