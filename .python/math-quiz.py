import math
import random

nestSpaces = random.randint(0,30)

print("Hello Niles!")
print("Help me get to the nest.")

print(f"The nest is {nestSpaces} spaces away. How many up moves should I do?")
moves = int(input("Enter the number: "))
print(f"Ok, I've moved up {moves} spaces.")
nestSpaces = nestSpaces - moves

print("Alright, how many left spaces should I move?")
moves = int(input("Enter the number: "))
print(f"Ok, I've moved left {moves} spaces.")
nestSpaces = nestSpaces - moves

print("Alright, how many right spaces should I move?")
moves = int(input("Enter the number: "))
print(f"Ok, I've moved right {moves} spaces.")
nestSpaces = nestSpaces - moves

print("Alright, how many down spaces should I move?")
moves = int(input("Enter the number: "))
print(f"Ok, I've moved down {moves} spaces.")
nestSpaces = nestSpaces - moves

print(f"The nest is now {nestSpaces} away.")

if nestSpaces == 0:
    print("You made it to the nest!")
else:
    print("Uh oh, you missed the nest! :(")