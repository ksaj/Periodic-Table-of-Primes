# Periodic Table of Primes

This Python script demonstrates a simple visualization called the "Periodic Table of Primes," inspired by the periodic table of elements, but tailored specifically for prime numbers.

## What is Demonstrated?

The script visually arranges prime numbers based on their modulo value relative to a specified base (default is modulo 6). This highlights the common distribution patterns and regularities of prime numbers, showcasing that primes greater than 3 typically fit into a modulo 6 pattern:

- Prime numbers greater than 3 typically have a remainder of either 1 or 5 when divided by 6.
- The visual table emphasizes these repeating patterns, providing insight into prime number distributions.

## How the Code Works

- **Prime Detection**:
  - The script includes a simple prime-checking function (`is_prime(n)`) that tests divisibility up to the square root of the number.

- **Table Construction**:
  - Prime numbers within a specified range (`limit`) are generated and organized into rows and columns.
  - Each prime number is placed into the table based on its value modulo the specified number (`columns`, default is 6).

- **Output**:
  - The resulting table clearly shows prime distribution across different modulo positions.

## Usage

### Requirements

- Python 3.x
- No external libraries required.

### Running the Script

1. Save the provided Python script (`periodic_primes.py`) to your local directory.

2. Execute the script via the command line:
   ```bash
   python periodic_primes.py
   ```

3. By default, it prints primes up to 100. Adjust the limit by changing the parameter:

   ```python
   periodic_table_of_primes(200)
   ```

## Sample Output

```
Periodic Table of Primes (mod 6):

mod0 mod1 mod2 mod3 mod4 mod5
----------------------------
  0 |   .    .   2    3    .    5
  6 |   .    7   .    .    .   11
 12 |   .   13   .    .    .   17
 18 |   .   19   .    .    .   23
 24 |   .    .   .    .    .   29
 30 |   .   31   .    .    .    .
...
```

## Educational Purpose

This script is intended as an educational tool to visually explore the distribution of prime numbers, allowing learners to easily recognize patterns and properties of primes through modular arithmetic.

