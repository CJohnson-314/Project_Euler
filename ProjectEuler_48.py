# Project Euler 48
# Self Powers
# https://projecteuler.net/problem=48
# Find the last 10 digits of the sum of 1^1 + 2^2 + ... + 1000^1000

def last_10_of_n_to_the_n(n:int) -> str:
    m = 1
    total = 0
    while m <= n:
        total += m**m
        m += 1
    return str(total)[-10:]

print(last_10_of_n_to_the_n(1000))

# Not a particularly elegent solution...
# Surely there must be a proper mathematical way to do it...
# But computer smashed it out in less than a tenth of a second...
