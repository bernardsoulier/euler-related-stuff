""" finds all primes up to a certain number and writes list to known_primes"""

import math

maxnumber = 100000000

prime_list = []

# load current primes

with open("known_primes", "r") as f:
    nextprime = 1
    while nextprime != "":
        nextprime = f.readline().strip()
        if nextprime != "":
            prime_list.append(int(nextprime))

lastprime = prime_list[-1]


with open("known_primes", "a") as f:
    for x in range(lastprime + 2, maxnumber, 2):
        prime = True
        for y in prime_list:
            if x % y == 0:
                prime = False
            if y > int(math.sqrt(x)):
                break
        if prime:
            prime_list.append(x)
            f.write(str(x) + "\n")
