# https://projecteuler.net/problem=53
# Combinatoric Selections
# How many values of n choose r are greater than 1 million,
# for 1 <= r <= n <= 100
# n choose r = n!/(r!(n-r)!)
# Nature of that formula means there is a symmetry around the halfway point
# e.g 5C1 = 5C4, 5C2 = 5C3
# So we only ever need to go up to halfway for each number
# Furthermore, up to the halfway point it's strictly increasing
# So, using the example from the question, 23C10 > 10^6
# Implies that 23C11, 23C12, 23C13 > 10^6
# Finally, we can use the fact that 100C3 < 10^6
# so never need to check 1/2

from math import comb
solutions = 0
n = 23
r = 3
while n <= 100:
    if comb(n, r) >= 1000000:
        for k in range(r, (n-r)+1):
            solutions += 1
        n += 1
        r = 3
        continue
    r += 1
print(solutions)
