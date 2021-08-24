

import random

#Players Cards
def initialize_cards():
    player_cards = []
    for i in range(1,53,1):
        if i%13 == 0:
            player_cards.append(13)
        else:
            player_cards.append(i%13)
    return player_cards

def random_cards(cards):
    index = random.randint(0,len(cards)-1)
    
    card_number = cards.pop(index)
   
    
   
    return card_number


def turn(playerDeck, dealerDeck, i):

    print("YOUR CARDS:")
    print(playerDeck)
    print("DEALER CARDS:")
    print(dealerDeck)
    valid = False
    while(not valid):

        if(i >=6):
            return False

        print("\n")
        user_input=input("Action Required: Type hit to recive card or stand to stay     ")
        print("\n")
        if(user_input == "hit"):
            return True
        if(user_input == "stand"):
            return False
        else:
            print("ERROR: type hit to recive card or stand to stay")


    

    
def main(bank):
    player_card_deck = []
    dealer_card_deck = []
    deck = initialize_cards()
    player_card_deck.append(random_cards(deck))
    player_card_deck.append(random_cards(deck))
    dealer_card_deck.append(random_cards(deck))

    if(sum(player_card_deck) == 21):
        print(sum(player_card_deck))
        print("PlayerBlackJack")
        bank = bank + 10
        return bank

    if(sum(player_card_deck) > 21 ):
            print("Cards over 21 - YOU LOSE")
            print(player_card_deck)
            bank = bank - 10
            return bank
    

    
    i = 0
    while (turn(player_card_deck,dealer_card_deck, i)):

        player_card_deck.append(random_cards(deck))
        i = i+1 #ask teacher

        if(sum(player_card_deck) == 21):
            print("YOUR CARDS:")
            print(player_card_deck)
            print("PlayerBlackJack - YOU WIN")
            bank = bank + 10
            print("Won " + str(10) + "$")
            return bank

        if(sum(player_card_deck) > 21 ):
            print("YOUR CARDS:")
            print(player_card_deck)
            print("Cards over 21 - YOU LOSE")
            bank = bank - 10
            print("Lost " + str(10) + "$")
            return bank
    

    
    while (sum(dealer_card_deck) < 17):
        dealer_card_deck.append(random_cards(deck))
        if(sum(dealer_card_deck) == 21):

            print("DeakerBlackJack - YOU LOSE")
            print(player_card_deck)
            print(dealer_card_deck)
            bank = bank - 10
            print("Lost " + str(10) + "$")
            return bank
        
        if(sum(dealer_card_deck) > 21 ):
            print("Dealer Cards over 21 - YOU WIN")
            print(player_card_deck)
            print(dealer_card_deck)
            bank = bank + 10
            print("Won " + str(10) + "$")
            return bank

    if(sum(player_card_deck) > sum(dealer_card_deck)):
        print(player_card_deck)
        print(dealer_card_deck)
        print("YOU WIN")
        bank = bank + 10
        print("Won " + str(10) + "$")
        return bank
    elif(sum(player_card_deck) == sum(dealer_card_deck)):
        print(player_card_deck)
        print(dealer_card_deck)
        print("DRAW")
        return 0

    else: 
        print(player_card_deck)
        print(dealer_card_deck)

        print("YOU LOSE")
        bank = bank - 10
        print("Lost " + str(10) + "$")
        return bank







    


def continue_game():
    valid = False
    while(not valid):
        user_input=input("Action Required: Type go to play next round or exit to quit   ")
        print("\n")
        if(user_input == "go"):
            return True
        if(user_input == "exit"):
            return False
        else:
            print("ERROR: Type go for new game or exit to quit")
        print("\n")



def gameStart():
    #instructions()
    cash = 0
    while(continue_game()):
        cash =  main(cash)
        print("Total: " + str(cash) + "$ ")

    print("Finished with: " + str(cash) + "$ ")




gameStart()

