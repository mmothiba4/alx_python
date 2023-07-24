#!/usr/bin/env python3
def fibonacci_sequence(n):
    if n in {0, 1}:
        return n
    else:
        return(fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2))
