def fibonacci_for_loop(n):
    """Generates the Fibonacci sequence up to n terms using a for loop."""
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Example usage:
fibonacci_for_loop(10)