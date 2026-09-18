print("...Snake-Water-Gun Game...")

import random

def game_win(user, computer):
    if user == computer:
        return None
    
    # Snake vs Water
    if user == "S" and computer == "W":
        return True
    if user == "W" and computer == "S":
        return False
    
    # Water vs Gun
    if user == "W" and computer == "G":
        return True
    if user == "G" and computer == "W":
        return False
    
    # Gun vs Snake
    if user == "G" and computer == "S":
        return True
    if user == "S" and computer == "G":
        return False

rand_no = random.randint(1,3)
print("Computer's turn: Snake (S), Water (W), Gun (G)")
if rand_no == 1:
    computer = "S"
elif rand_no == 2:
    computer = "W"
else:
    computer = "G"

user = input("Your turn: Snake (S), Water (W), Gun (G): ").upper()

result = game_win(user, computer)             # Return true if you win, None for draw  and false for draw
print(f"\n You Choose: {user}")
print(f"\n Computer Choose: {computer}")

if result is None:
    print("It's Draw!")

elif(result):
    print("You Win!")
else:
    print("You Loose!")
