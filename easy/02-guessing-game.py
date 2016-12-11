#!/usr/bin/env
#The user thinks of a number and the program will try to figure it out as quickly as possible.
print("Think of a number.")

def main():
    limit = [0, 101]
    guess_list = []
    choice = ""
    num = 50
    lim_ref = {'h': 0, 'l': 1}
    while(choice != "c"): #Loops until correct guess
        guess_list.append(num) #Adds 50 to guess list
        choice = get_input(num)
        if (choice == "h" or choice == "l"):
            #Sets lower & upper limit = num when choice is high or low respectively
            limit[lim_ref[choice]] = num
            num = sum(limit) / len(limit) #Average of upper & lower limit
        elif (choice =="c"): #Correct guess
            print("Thank you for playing.")
        else: #Invalid responses
            print("Please enter valid response (h/l/c).")
    print("The total number of guesses => " + str(len(guess_list)))
    print("Guessed numbers => " + str(guess_list)[1:-1])

def get_input(num):
    print("\n" + str(num) + " => Is this guess (h)igh, (l)ow, or (c)orrect?")
    return raw_input("> ").lower()[0]

if __name__ == "__main__":main()
