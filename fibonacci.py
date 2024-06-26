# -*- coding: utf-8 -*-
"""fibonacci.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uf7oxNIqhTZN3G8vUd5t2vUhQJHmPuIU
"""

# fibonacci.py

def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    fib_sequence = [0, 1]  # Initialize Fibonacci sequence
    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]  # Calculate next term
        fib_sequence.append(next_term)  # Add next term to sequence
    return fib_sequence

def main():
    try:
        n = int(input("Enter the number of Fibonacci terms to generate: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        fib_sequence = fibonacci(n)
        print("Fibonacci sequence:", fib_sequence)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()