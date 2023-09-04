import random

current_number = 0
total_number = 0
resets = 0
probability = 0
highest_number = 0

while current_number != 100:
  if current_number == 100:
    break
  current_number += 1
  total_number += 1
  probability = random.randint(0, 100)
  if probability <= current_number:
    if current_number > highest_number:
      highest_number = current_number
      print("Highest Number: ", highest_number)
      print("Total Number: ", total_number)
      print("Resets:", resets)
      print(" ")
    current_number = 0
    resets += 1
