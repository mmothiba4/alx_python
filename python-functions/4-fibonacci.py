#!/usr/bin/env python3
def fibonacci_sequence(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fibonacci_sequence = [0, 1]
    if n == 2:
        return [1]
    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
        return []
        




















































































































































































































































        return n
    else:
        return(fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2))
