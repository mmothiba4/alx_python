#!/usr/bin/env python3
def fibonacci_sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return(fibonacci_sequence(n - 2) + fibonacci_sequence(n - 1))
