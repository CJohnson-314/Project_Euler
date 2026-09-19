# Project Euler 55
# Lychrel Numbers
# How Many lychrel numbers are there below 10k?
# Where a lychrel number is a number that doesn't become a palindrome using reverse + add process
# For purpose of question, we only have to go up to 50 iterations for each number

def reverse_and_add(n: int) -> int:
    return n + int(str(n)[::-1])

def is_palindrome(n: int) -> bool:
    half_n = len(str(n)) // 2

    if str(n)[:half_n] == (str(n)[-half_n:])[::-1]:
        return True
    else:
        return False  

def is_lychrel(n: int,
               current_loop = 0) -> bool:
    iter_n = reverse_and_add(n)
    if is_palindrome(iter_n) == True:
        return False
    elif current_loop == 50:
        return True
    else:
        current_loop += 1
        return is_lychrel(iter_n, current_loop)

lychrel_numbers = []
n = 1
while n < 10000:
    if is_lychrel(n) == True:
        lychrel_numbers.append(n)
    n += 1

print(len(lychrel_numbers), lychrel_numbers)
