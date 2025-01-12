#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])  
        return
    elif length == 1:
        print([0])  
        return

    fib = [0, 1]
    for _ in range(2, length):
        fib.append(fib[-1] + fib[-2])
    
    print(fib)  
print_fibonacci(0)  
print_fibonacci(1)  
print_fibonacci(2)  
print_fibonacci(10)
