#!/usr/bin/env python3
def fibonacci_sequence(n):
    if n < 0:
        print("incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return(fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2))
