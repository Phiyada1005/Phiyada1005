# This program simulates 10 tosses of a coin.
import random

# Constants
HEADS = 1
TAILS = 2
TOSSES = 10

def tosses_coin():
    for toss in range (TOSSES):
        # Simulate the cion toss.
        if random. randint(HEADS , TAILS) == HEADS:
            print('Heads')
        else:
            print('Tails')

# Call the main function.
tosses_coin()