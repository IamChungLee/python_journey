############### Blackjack Project #####################


from art import logo
import random

blackjack = True
while blackjack:
  play = input("Would you like to play blackjack? Type 'y' or 'n'")
  if play == "n":
    blackjack = False

  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  def random_card():
    return random.choice(cards)


  if play == "y":
    print(logo)
    # your hand and computer hand
    your_hand = [random_card(), random_card()]
    computer_hand = [random_card(), random_card()]
    computer_first = computer_hand[0]
    
  
    # condition to keep game running
    keep_playing = True
    while keep_playing: 
      
      # Your score and computer score

      # calculate_score function
      def calculate_score(hand):
        score = 0
        for card in hand:
          score += card
        return score


      # STARTING DISPLAY
      print(f"Your cards: {your_hand}, current score:{calculate_score(your_hand)}")
      print(f"Computers first score {computer_first}")
      hit_or_pass = input("Type 'y to get another card, type 'n' to pass: ")
      print(hit_or_pass)
      
      # ENDGAME DISPLAY
      def endgame():
        print(f"Your final hand: {your_hand}: {calculate_score(your_hand)}")
        print(f"Computers final hand: {computer_hand}: {calculate_score(computer_hand)}")

      # beginning draws
      if calculate_score(your_hand) == 21:
        endgame()
        print("you win")
        keep_playing = False
      elif calculate_score(computer_hand) == 21:
        endgame()
        print("you lose")
        keep_playing = False

      # when you hit or pass
      if hit_or_pass == "y":
        your_hand.append(random_card())
        if calculate_score(your_hand) > 21:
          endgame()
          print("You lose")
          keep_playing = False
        elif calculate_score(your_hand) == 21:
          endgame()
          print("You win")
          keep_playing = False
      elif hit_or_pass == "n":
        while calculate_score(computer_hand) < 17:
          computer_hand.append(random_card())
        if calculate_score(computer_hand) == calculate_score(your_hand):
          endgame()
          print("Draw")
          keep_playing = False
        elif calculate_score(computer_hand) > calculate_score(your_hand) and calculate_score(computer_hand) <= 21:
          endgame()
          print("you lose")
          keep_playing = False
        elif calculate_score(computer_hand) > 21:
          endgame()
          print("You win")
          keep_playing = False
        