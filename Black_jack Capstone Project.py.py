# from Black_jack_art import logo
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)

# This is used to clear the page for the next game
def clear():
    print('\n'*50)

# This function is used to deal the cards and then return that value
def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# This calculates the total sum of the cards and then returns its respected value
def calculate_score(cards):
    # This checks if it is a blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # This is a rule of the game as in if the score is over 21, and you have a card
    # 11 in your hand, it will represent a 1.
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    # Comparing/ going over different conditions.
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer wins, it has a blackjack"
    elif user_score == 0:
        return "User wins, you have a blackjack"
    elif user_score > 21:
        return "Computer wins"
    elif computer_score > 21:
        return "User wins"
    elif computer_score > user_score:
            return "Computer wins"
    else:
        return "User wins"

def play_again():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play == 'y':
        clear()
        print(logo)


        # These are dummy variables
        user_cards = []
        computer_cards = []

        # We start off the game with the game not being over
        is_game_over = False

        # This will use the deal_cards functions and randomly generate two cards
        for _ in range(2):
            user_cards.append(deal_cards())
            computer_cards.append((deal_cards()))



        # This while loop is calculating the final values of the cards we draw
        while is_game_over == False:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print(f"    Your cards: {user_cards}, current score: {user_score}")
            print(f"    Computer's first card: {computer_cards[0]}")

            # if any of the below statements are true it will end the game
            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over = True

            # Asks the player if they want to draw another card
            else:
                draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if draw_card == 'y':
                    user_cards.append(deal_cards())
                else:
                    is_game_over = True
        # This is so the computer can keep pulling cards as long as its score is less than 17.
        while computer_score < 17 and computer_score != 0:
            computer_cards.append((deal_cards()))
            computer_score = calculate_score(computer_cards)

        print(f"    Your final cards: {user_cards}, final score: {user_score}")
        print(f"    Computer's final cards: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))
        play_again()
    else:
        pass
play_again()
