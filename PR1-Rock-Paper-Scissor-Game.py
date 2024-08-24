
import random
print("rock paper scissor best of 5")
listx=["rock","paper","scissor"]

user_score = 0
comp_score = 0

print(listx)
for i in range(5):
    user = input("enter your choice from the followin options:")

    computer = random.choice(listx)
    print(computer)
    if (user == "rock" and computer == "scissor"):
        print("you win")
        user_score += 1
        print("Score:","User:",user_score,"Computer:",comp_score)
        
    elif (user == "scissor" and computer == "paper"):
        print("you win")
        user_score += 1
        print("Score:","User:",user_score,"Computer:",comp_score)
        
    elif (user == computer):
        print("tie")
        print("Score:","User:",user_score,"Computer:",comp_score)
        
    elif (user == "paper" and computer == "rock"):
        print("you win")
        user_score += 1
        print("Score:","User:",user_score,"Computer:",comp_score)
        
    else:
        print("computer wins")
        comp_score += 1
        print("Score:","User:",user_score,"Computer:",comp_score)
        
        
if user_score > comp_score:
    print("Congratulations!!, You win")
elif user_score < comp_score:
    print("Computer wins!!, Better luck next time")
else:
    print("Its is tie")

# scenarios
# # C - rock   U - scissor  : C
# # C - paper   U - rock     :C
# # C - scissors U - paper  : C


# # U - rock    C - scissor : U
# # U - paper   C - rock    : U
# # U - scissors  C - paper  : U


