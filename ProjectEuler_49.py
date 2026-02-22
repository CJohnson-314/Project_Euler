# Project Euler 49
# Prime Permutations
# https://projecteuler.net/problem=49
# There are two 3-term arithmetic sequences of 4-digit numbers with the following properties:
    # All 3 terms are prime
    # Each of the terms are permutations of one another
# One of the sequences is 1487, 4817, 8147
# Find the other one

from itertools import permutations
from ProjectEuler_3_factors_function import factors

def find_arithmetic_triplet(nums):
    nums = sorted(nums)
    s = set(nums)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            a = nums[i]
            b = nums[j]
            d = b - a
            c = b + d   # third term of the progression
            if c in s:
                return (a, b, c)
    return None

n = 1000
solution = []
while len(solution) == 0:
    perms = set() # Set means we don't have to worry about dupes
    for perm in permutations(str(n), 4):
        int_perm = int(''.join(perm))
        # We just need to look at the permutations that are prime and 4 digits
        if len(factors(int_perm)[1]) == 1 and int_perm >= 1000:
            perms.add(int_perm)
    if n in [1487, 4817, 8147]:
        n += 1
        continue
    if find_arithmetic_triplet(perms) is not None:
        solution.append(find_arithmetic_triplet(perms))
    n += 1
    if n % 10 == 0:
        print(n)

print(solution)



