def is_prime(x):
    import math

    if x< 1:
        print("Provide a positive number")
    if x % 2 == 0:
        return print("%i is not a prime number"%x)
    p = 3
    while p <= math.sqrt(x):
        if x % p == 0:
            return print("%i is not a prime number"%x)
        p +=2
    return print("%i is a prime number"%x)

is_prime(9)

