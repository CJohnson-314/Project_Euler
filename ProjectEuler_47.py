# Project Euler 47
# Distinct Prime Factors
# put url here...
# Find the first 4 consecutive integers to have 4 distinct prime factors each
# What is the smallest of these numbers?

from ProjectEuler_3_factors_function import factors

# Okay, so attempt 1 just involved brute forcing
# Answer not in first 100k, so maybe need to get a bit smarter
# We don't need to compute factors of n every single time
# We can dynamically skip ahead based on which didn't have 4
# Still not very efficient at all, runs in ~90 secs for me
# I'll take it

# Start at 210 as the first number with 4 distinct primes
# (2 * 3 * 5 * 7)
n = 210
solution = []

while len(solution) == 0:
    if len(set(factors(n)[1])) != 4:
        n += 1
    elif len(set(factors(n+1)[1])) != 4:
        n += 2
    elif len(set(factors(n+2)[1])) != 4:
        n += 3
    elif len(set(factors(n+3)[1])) != 4:
        n += 4
    else:
        solution.append(n)
    if n % 1000 == 0:
        print(n)

print(solution[0])
