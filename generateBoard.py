import random

def generate_random_list(n):
  lst = list(range(1, n+1))
  random.shuffle(lst)
  return lst

n = 1000

with open(f"boardSize{n}.txt", "w") as file:
  for item in generate_random_list(n):
    file.write(str(item) + "\n")