from replit import clear

import art

names_bids = {}

def add_to_bids(bidder, price):
  names_bids[bidder] = price
  


print(art.logo)


offline = False
while not offline:
  name = input("What is your name?\n")
  bid = input("How much do you want to bid?\n$")
  add_to_bids(name, bid)  
  more_bids = input("Are there anymore bidders?Type 'yes' or 'no'")
  

  if more_bids == "no":
    offline = True
    highest = 0
    for bidder in names_bids:
      store = ""
      store = names_bids[bidder] 
      price_hold = int(store)
      if price_hold > highest:
        highest = price_hold
    
    highest_value = str(highest)
    for bidder in names_bids:
      if highest_value in names_bids[bidder]:
        print(f"the winnder is {bidder} with a bid of {names_bids[bidder]}")

  else:
    clear()




