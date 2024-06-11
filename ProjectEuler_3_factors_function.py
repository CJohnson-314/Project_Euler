import math
from itertools import chain, combinations

# for future use, save as a function
def factors(n):
    #throw some errors
    assert n % 1 == 0, f"{n} is not an integer"
    assert n >= 0, f"{n} is negative"
    assert n <= 10**12, f"{n} is too big, floats don't play nicely around this size"
    
    factors = [n] # start with the number itself as a factor
    prime_factors = []
    
    if n == 2:
        factors.append(1)
        prime_factors.append(2)
        return factors, prime_factors
    # if method can't find any factors, add to primes
    for factor in factors:
        # deal with even numbers
        if factor == 2:
            prime_factors.append(2)
        elif factor % 2 == 0:
            factors.append(2)
            factors.append(factor/2)
        # Fermat stuff
        else:
            start = math.ceil(factor**0.5)
            m = start**2 - factor
            while m**0.5 % 1 != 0:
                start += 1
                m = start**2 - factor
            small_factor = start - m**0.5
            big_factor = start + m**0.5
            if big_factor == factor: # for primes e.g. if factor = 7, big_factor = 7, append to primes
                prime_factors.append(big_factor)
            else:
                factors.append(small_factor)
                factors.append(big_factor) 

    prime_factors_subsets = list(chain(*[combinations(prime_factors,n) for n in range(len(prime_factors)+1)]))
    for subset in prime_factors_subsets:
        if math.prod(subset) not in factors:
            factors.append(math.prod(subset))

    return sorted(list(set(factors))), sorted(prime_factors)