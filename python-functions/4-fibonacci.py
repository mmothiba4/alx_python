#!/usr/bin/env python3
def fibonacci_sequence(n):
    fibo_list = []
    a,b = 0,1
    while b < n:
        a,b = b, a+b
        fibo_list.append(a)
    print(fibo_list)




















































































































































































































































        return n
    else:
        return(fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2))
