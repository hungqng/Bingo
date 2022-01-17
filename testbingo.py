import random
import numpy as np

print("Here are your numbers:")
playerBoard = np.random.randint(1,99, size=(5,5))

print(playerBoard)
# print("Are you ready to play?")
# print("Type 1 to Play, Type 2 to Stop")
# userInput = input()
# while True:
#     if userInput == 1:
#         continue
#     elif userInput == 2:
#         break
#     else:
#         print("Please enter 1 to Play or 2 to Stop")
    
numlist = list(range(1,26))
    #numlist = random.shuffle(numlist)
random.shuffle(numlist)
    #newNumber = random.choice(range(1,25))

i = 0
while i < len(numlist):
    print(numlist[i])
    i += 1
