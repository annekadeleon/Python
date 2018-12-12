# begin compatibility level with 100%
comp = 100
# get player's name
xname = input("Enter your name: ")
# get their partner's name
yname = input("Enter your partner's name: ")
# combine names together
name = (xname) + (yname)
# weighted % of each character
weight = 100 / len(name)
# go through each character
# see if it has 'l','o','v','e', or 's'
# if it does, take weighted amount from percentage
for char in name:
  if char.lower() in ['l','o','v','e','s']:
    comp -= weight
# congratulate them if compatibility is high
if comp >= 65:
  print("Congratulations, " + (xname) + "! Your compatibility level is: " str(int(comp)) + "%")
# or just give them their compatibility level
else:
  print("Your compatibility level is: " + str(int(comp)) + "%")
