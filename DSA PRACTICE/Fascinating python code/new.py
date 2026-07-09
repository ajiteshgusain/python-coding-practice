def is_prime(n: int) -> bool:
    """Returns True if n is prime, False otherwise."""
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

# Test it out
numbers = [2, 4, 17, 20, 23]
prime_status = {num: is_prime(num) for num in numbers}
print(prime_status)
# Output: {2: True, 4: False, 17: True, 20: False, 23: True}
