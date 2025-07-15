import time, random

print("Initization finished!")
moves = ["Rock", "Paper", "Scissor"]

def init():
    global selAI
    selAI = random.choice(moves)
    time.sleep(1)

def y():
    print("You won!")
def n():
    print("AI won! :(")

print("Welcome to the Rock Paper Scissors in Python!")
time.sleep(2)

while True:
    init()
    selME = input("Please select a move between 'Rock, Paper, Scissor' \n")
    if selME not in moves:
        print("Please select the correct keyword. Those are: (Rock, Paper, Scissor.)")
    else: 
        if selME == selAI: 
            print ("Draw!")
        elif selME == "Rock" and selAI == "Paper":
            n()
        elif selME == "Rock" and selAI == "Scissor":
            y()
        elif selME == "Paper" and selAI == "Rock":
            y()
        elif selME == "Paper" and selAI == "Scissor":
            n()
        elif selME == "Scissor" and selAI == "Paper":
            y()
        elif selME == "Scissor" and selAI == "Rock":
            n()
