import random 

computer = random.choice([1, 0, -1])
youstr = int(input("Enter 1 for rock, 0 for paper and -1 for scissors: "))
youDic = {1: "rock", 0: "paper", -1: "scissors"}
reverseDic = { 1: "rock",  0 :"paper",  -1 : "scissors"}
user = youDic[youstr]
print(f"Computer chose {youDic[computer]}")
if computer == user:
    print("It's a tie")
elif (computer == 1 and user == 0) or (computer == 0 and user == -1) or (computer == -1 and user == 1):
    print("You win")
else:
    print("You lose")

