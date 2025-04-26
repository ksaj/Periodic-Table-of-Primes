def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def periodic_table_of_primes(limit, columns=6):
    primes = [n for n in range(2, limit) if is_prime(n)]
    
    # Initialize the table
    table = [["." for _ in range(columns)] for _ in range((limit // columns) + 1)]
    
    for prime in primes:
        row = prime // columns
        col = prime % columns
        table[row][col] = str(prime).rjust(3)

    # Display table
    print(f"Periodic Table of Primes (mod {columns}):\n")
    header = " ".join([f"mod{i}".rjust(4) for i in range(columns)])
    print(header)
    print("-" * len(header))

    for idx, row in enumerate(table):
        line = " ".join(row)
        print(f"{str(idx*columns).rjust(3)} | {line}")

# Example: Primes up to 100
periodic_table_of_primes(100)

