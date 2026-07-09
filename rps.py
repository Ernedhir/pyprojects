import time, random

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

while True:
    init()
    selME = input("Please select a move between 'Rock, Paper, Scissor' \n")
    if selME == 'q': break

    if selME not in moves:
        print("Please select the correct move. Those are: (Rock, Paper, Scissor.)")
    else: 
        if selME == selAI: 
            print ("Draw!")
        elif selME == 'Rock':
            if selAI == 'Paper':     n()
            elif selAI == 'Scissor': y()
        elif selME == 'Paper':
            if selAI == 'Scissor':   n()
            elif selAI == 'Rock':    y()
        elif selME == 'Scissor':
            if selAI == 'Rock':      n()
            elif selAI == 'Paper':   y()
