import math

# for future use, save as a function
def factors(n):
    #throw some errors
    assert n % 1 == 0, f"{n} is not an integer"
    assert n >= 0, f"{n} is negative"
    assert n <= 10**16, f"{n} is too big, floats don't play nicely around this size"
    
    factors = [n] # start with the number itself as a factor
    prime_factors = []
    
    if n == 2:
        factors.append(1)
        prime_factors.append(2)
        return factors, prime_factors
    # if method can't find any factors, add to primes
    # loop until prime_factors multiplies to n
    #while math.prod(prime_factors) != factors[0]:
    for factor in factors:
        # deal with even numbers
        if factor == 2:
            prime_factors.append(2)
            continue
        elif factor % 2 == 0:
            factors.append(2)
            factors.append(factor/2)
            #prime_factors.append(2)
        # Fermat stuff
        else:
            start = math.ceil(math.sqrt(factor))
            m = start**2 - factor
            while math.sqrt(m) % 1 != 0:
                start += 1
                m = start**2 - factor
            small_factor = start - math.sqrt(m)
            big_factor = start + math.sqrt(m)
            if big_factor == factor: # for primes e.g. if factor = 7, big_factor = 7, append to primes
                prime_factors.append(big_factor)
            else:
                factors.append(small_factor)
                factors.append(big_factor)

    factors.append(1) # for completeness

    return factors, prime_factors