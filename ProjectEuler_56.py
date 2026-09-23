# Project Euler 56
# https://projecteuler.net/problem=56
# Considering numbers of the form a^b, a,b<100, what is the maximum digit sum?

# There is probably some quite interesting and profound maths here
# Most (but not all of the time) raising a number to higher power results in a higher digit sum
# But we can brute force this
# Just look at 50 ^ 50 and up, cutting bottom 50% seems safe
# I'll eat my hat if it turns out to be 49 ^ 49
# This way we just end up with 50*50 numbers to compare

def sum_digits(n:int) -> int:
    digits = list(str(n))
    return sum(int(digit) for digit in digits)   

a = 50
sums = []

while a < 100:
    b = 50
    while b < 100:
        sums.append(sum_digits(a**b))
        b += 1
    a += 1

print(max(sums))
