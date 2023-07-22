#!/usr/bin/env python3
def is_prime(number):
    for i in range(2,number):
        if (number%i) == 0:
            return True
        return False
    