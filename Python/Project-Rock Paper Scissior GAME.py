import random
def play():
    print("Welcome to the game write your name and let fun!!")
    #name = input("Name: ")
    r="rock"
    s="scissior"
    p="paper"
    game = [r,s,p]
    w = 0
    l = 0
    t = 0
    R = 0
    while True:
        R += 1
        print("Round",R)
        print("Choose your hand rock, paper, scissior")
        user = input("Hand :").lower()
        com  = random.choices(game)
        com = com[0]
        if user == r and com == s:
            print("You win!!")
            w += 1
        elif user == s and com == p:
            print("You win!!")
            w += 1
        elif user == p and com == r:
            print("You win!!")
            w += 1
        elif user == com:
            print("Tie!! play again")
            t += 1
        elif user == "stop":
            print("Score")
            print(f"Win: {w}, Lose: {l}, Tie: {t}")
            break
        else:
            print("You lose!!")
            l += 1
        print("Result!")
        print(f"User hand: {user}")
        print(f"PC hand: {com}")
        print("\n")
