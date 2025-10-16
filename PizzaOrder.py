print("Welcome to python Pizza Deliveries!")
size=input("What size pizza do you want? S,M or L")
pepperoni=input("Do you want pepperoni on your pizza? Y or n")
extra_cheese("Do you want extra cheese?y or n")

bill=0
if size=="S":
 bill+=15
elif size=="M":
 bill +=20
elif size=="L":
 bill +=25
else
 print("you types\d the wrong inputs")
if pepperoni=="Y":
 if size=="S":
  bill+=2
 else:
  bill+=3
if extra_cheese=="Y":
 bill+=1
print(f"your final bill is: ${bill}")
