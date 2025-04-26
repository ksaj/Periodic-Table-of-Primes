# Periodic Table of Primes

This project demonstrates the concept of a "Periodic Table of Primes" through implementations in multiple programming languages, including Python and Common Lisp.

## What is Demonstrated?

The scripts visually arrange prime numbers based on their modulo value relative to a specified base (default is modulo 6). This highlights the common distribution patterns and regularities of prime numbers, showcasing that primes greater than 3 typically fit into a modulo 6 pattern:

- Prime numbers greater than 3 typically have a remainder of either 1 or 5 when divided by 6.
- The visual tables emphasize these repeating patterns, providing insight into prime number distributions.

## How the Code Works

### Prime Detection
- Both implementations use simple functions (`is_prime` in Python, `prime-p` in Lisp) that test divisibility up to the square root of the number.

### Table Construction
- Prime numbers within a specified range (`limit`) are generated and organized into rows and columns.
- Each prime number is placed into the table based on its value modulo the specified number (`columns`, default is 6).

### Output
- The resulting tables clearly show prime distribution across different modulo positions.

## Available Implementations
- **Python** (`ptp.py`): Simple, pure Python script without external dependencies.
- **Common Lisp** (`ptp.lisp`): Efficient, idiomatic Lisp implementation without external libraries.

## Usage

### Requirements
- Python 3.x (no external libraries)
- Common Lisp environment (no external libraries)

### Running the Scripts

#### Python

Save the Python script (`ptp.py`) and execute:

```bash
python ptp.py
```

Adjust the limit in the script to explore larger prime sets:

```python
periodic_table_of_primes(200)
```

#### Common Lisp

Load the Lisp script (`ptp.lisp`) into a Lisp interpreter such as SBCL or CLISP and run the provided example:

```lisp
(load "ptp.lisp")
```

## Sample Output

```
Periodic Table of Primes (mod 6):

mod |    0     1     2     3     4     5
----------------------------------------
  0 |    .     .     2     3     .     5
  6 |    .     7     .     .     .    11
 12 |    .    13     .     .     .    17
 18 |    .    19     .     .     .    23
 24 |    .     .     .     .     .    29
 30 |    .    31     .     .     .     .
...
```

## Educational Purpose

These scripts are intended as educational tools to visually explore the distribution of prime numbers, allowing learners to easily recognize patterns and properties of primes through modular arithmetic.

