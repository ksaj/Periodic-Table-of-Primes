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
    print("mod |", end="")
    for i in range(columns):
        print(f"{i:>5}", end="")
    print("\n" + "-" * (6 + columns * 5))
    
    for idx, row in enumerate(table):
        print(f"{idx * columns:3} |", end="")
        for cell in row:
            print(f"{cell:>5}", end="")
        print()

# Example: Primes up to 100
periodic_table_of_primes(100)

