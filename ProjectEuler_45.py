# Project Euler 45
# Triangular, Pentagonal, and Hexagonal
# https://projecteuler.net/problem=45
# The 285th triangular number (40755) is equal to the 165th pentagonal number, and the 143rd hexagonal number
# Find the next triangular number that is also pentagonal and hexagonal

# Not sure on the best approach as a starting point
# Seems fairly reasonable to just generate a load of triangular numbers and then test to see if they're also pent/hex?
# On second thoughts maybe start with hexagonal as they're rarer

hexagonal_numbers = []
def generate_hexagonals(n: int) -> int:
    return n*((2*n)-1)
n = 1
while n <= 50000:
    hexagonal_numbers.append(generate_hexagonals(n))
    n += 1

def test_pent(x: int) -> bin:
    if x <= 0:
        raise ValueError('Input cannot be 0 or negative')
    condition = (((24*x + 1)**0.5) + 1) / 6
    if condition % 1 == 0:
        return True
    else:
        return False

def test_tri(x: int) -> bin:
    if x <= 0:
        raise ValueError('Input cannot be 0 or negative')
    condition = ((8*x) + 1)**0.5
    if condition % 1 == 0:
        return True
    else: 
        return False

all_three = []
for hex in hexagonal_numbers:
    if test_pent(hex) == True and test_tri(hex) == True:
        all_three.append(hex)

print(all_three)
