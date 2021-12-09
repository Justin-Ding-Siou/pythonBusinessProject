import time
num_heads = 35
num_legs = 94

# first try
start_time = time.time()
for chickens in range(0, num_heads+1):
  rabbits = num_heads - chickens
  if 2 * chickens + 4 * rabbits == num_legs:
    print("Number of chickens:", chickens)
    print("Number of rabbits: ", rabbits)

print("--- %s seconds ---" % (time.time() - start_time))

# second try
start_time = time.time()
for rabbits in range(0, num_heads+1):
  chickens = num_heads - rabbits
  if 2 * chickens + 4 * rabbits == num_legs:
    print("Number of chickens:", chickens)
    print("Number of rabbits: ", rabbits)

print("--- %s seconds ---" % (time.time() - start_time))
