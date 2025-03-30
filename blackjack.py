import time, random

deck = {"Clubs": ["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Joker", "Queen", "King"], 
        "Diamonds": ["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Joker", "Queen", "King"],
        "Hearts": ["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",  "Joker", "Queen", "King"],
        "Spades": ["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10" ,"Joker", "Queen", "King"]}

def select_random_card(who=None): # Selects a random card from given deck and assigns it accordingly.
    global Hand, AI, HandSum, AISum
    card_type = random.randint(0,3)
    sel_deck = list(deck.keys())[card_type]
    index = random.choice(range(len(deck[sel_deck])))
    sel_card = deck[sel_deck][index]
    if index == 0: index=11
    elif index>=11: index=10
    if who == "ME":
        Hand.append({sel_deck: sel_card})
        HandSum += index
    elif who == "AI":
        AI.append({sel_deck: sel_card})
        AISum += index
    return [sel_deck, sel_card, index]

def initilaziaton(): # Initializes the game. 
    global Hand, AI, HandSum, AISum
    AI=list()
    AISum=0
    Hand=list()
    HandSum=0
    for i in range(0, 4):
        i+=1
        if i % 2 != 0: select_random_card("ME")
        else: select_random_card("AI")
    print(HandSum, Hand)
    print(AISum, AI)
    print(f"Initilaziaton finished!\nDealer's Hand is: {str(list(AI[0]))[2:-2]} of {str(list(AI[0].values()))[1:-1]} and ?\nYour Hand is: {str(list(Hand[0]))[2:-2]} of {str(list(Hand[0].values()))[1:-1]} and {str(list(Hand[1]))[2:-2]} of {str(list(Hand[1].values()))[1:-1]} ({HandSum})")

def comp(arg1, arg2): # Compares two given integer. Not very needed but meh.
    if type(arg1) is not int or type(arg2) is not int: raise TypeError(f"bruh u gotta compare between to integers not {type(arg1)} or {type(arg2)}")
    if arg1>arg2: return True
    elif arg1<arg2: return False
    else: return "Equal"

while True:
    print("Welcome to Blackjack on Python!")
    initilaziaton()
    time.sleep(2)

    if HandSum == 21:
        print("Congratz, you won! You did not even need to hit or sum :O")
        time.sleep(3)
        initilaziaton()
    elif HandSum != 21 and AISum == 21:
        print("Case won :(")
        initilaziaton()
    elif AISum > 21:
        print("Case busted!")
        initilaziaton()
    else:
        while True:
            move = input("Wanna hit? (Avaliable options: [hit, stand, double]) ")
            if move == "double":
                print("not implemented")
                continue
            elif move == "hit":
                sel = select_random_card()
                Hand.append({sel[0]: sel[1]})
                HandSum+=sel[2]
                print(f"Your new card: {sel[0]} of {sel[1]} Total: {HandSum}")
                if HandSum == 21:
                    if AISum != 17:
                        while True:
                            if AISum <= HandSum:
                                sel = select_random_card()
                                AI.append({sel[0]: sel[1]})
                                AISum+=sel[2]
                                print(f"Dealer's turn: {sel[0]} of {sel[1]}")
                                time.sleep(1.2)
                            else:
                                break
                        if AISum == HandSum:
                            print("Push!")
                        else:
                            print("Dealer busted, you won! ({AISum})")
                        break
                    else:
                        print("You won with BJ in your hand! AI Had {AISum}")
                        break
                elif HandSum > 21:
                    print("You busted! "+ str(HandSum))
                    break
            elif move == "stand":
                if AISum == 17:
                    if AISum > HandSum:
                        print(f"You lost! {HandSum} and dealer had {AISum}")
                        break
                    elif AISum < HandSum:
                        print(f"You won! {HandSum} and dealer had {AISum}")
                        break
                    else:
                        print(f"Push! {HandSum} and {AISum}")
                        break
                elif AISum > HandSum:
                    print(f"Dealer won! {AISum} You had {HandSum}")
                    break
                elif AISum == HandSum and AISum > 10:
                    print(f"Push! Both of you had {AISum}")
                    break
                else:
                    while AISum <= 21:
                        sel = select_random_card()
                        AISum += sel[2]
                        AI.append({sel[0]: sel[1]})
                        print(f"Dealer picked: {sel[0]} of {sel[1]} ({AISum})")
                        time.sleep(1)
                        result = comp(HandSum, AISum)
                        if AISum == 17:
                            if result:
                                print(f"You won! ({HandSum}) AI had {AISum}")
                                break
                            elif result == "Equal":
                                print(f"Push! {HandSum} AI {AISum}")
                                break
                            else:
                                print(f"Dealer won! {AISum} You had {HandSum}")
                                break
                        elif not result and AISum <= 21:
                            print(f"Dealer won! {AISum} You had {HandSum}")
                            break
                        elif result == "Equal":
                            print(f"Push! {AISum}")
                            break
                    if AISum > 21:
                        print(f"Dealer busted! ({AISum}) You had {HandSum}")
                    break


    time.sleep(5)
