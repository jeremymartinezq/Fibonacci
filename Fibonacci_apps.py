def fibonacci_cycle_length(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq


# Example length of cycles to predict
num_cycles = 5

cycles = fibonacci_cycle_length(num_cycles)
print(f"Fibonacci Cycle Lengths: {cycles}")



