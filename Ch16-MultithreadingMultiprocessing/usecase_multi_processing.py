'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, 
involve significant computational work. Multiprocessing 
can be used to distribute the workload across multiple 
CPU cores, improving performance.

'''
import multiprocessing
import time
import math
import sys

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

## function to compute factorials of a given number 
def computer_factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    return result

if __name__ == "__main__":
    numbers = [1000, 5000, 10000, 15000]

    start_time = time.time()

    #create a pool of processes
    with multiprocessing.Pool(processes=8) as pool:
        results = pool.map(computer_factorial, numbers)

    end_time = time.time()

    print("Factorials computed:")
    print(f"Results: {results}")

    print(f"Time taken: {end_time - start_time:.2f} seconds")