import os

permission = "yes"
empty_dictionary={}

while permission=="yes":
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ")
    bids = int(input("What's your bid?: $"))
    empty_dictionary[name] = bids
    permission=input("Are there any other bidders? Type 'yes or 'no").lower()
    if permission=="yes":
     os.system('cls')

max_bid=0
winner = ""
for name, bid in empty_dictionary.items():
    if bid > max_bid:
        max_bid = bid
        winner = name
 
print(f"The winner is {winner} with a bid of ${max_bid}")