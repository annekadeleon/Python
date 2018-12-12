# pick a random number
import random
# player initially starts with score of 1
score = (1)
# ask if they want to double their score
print("Would you like to double your score? [y/n]")
# get answer
double = input()
# keep going as long as they say 'y'
while score != 0 and double.lower() == 'y':
  # get random number between 0 and 3 (75% chance of winning)
  fate = random.randint(0,3)
  # if random number is 0, half their current score
  if fate == (0) and score != (0):
    score = int(score/2)
    print("Your score is now " + str(score) + ".")
  # if the random score is 1 2 or 3, double their score
  else:
    score = int(score*2)
    print("Yay! Your score is now " + str(score) + ".")
  # tell them they lost
  if score == (0):
    print("Sorry, you lose.")
  # unless they didn't
  else:
    double = input("Do you want to double your current score?[y/n]: ")
  # tell them their final score
  print("Thank you for playing."
