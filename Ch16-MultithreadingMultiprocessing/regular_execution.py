

from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(n):
    time.sleep(1)
    return f"Number: {n}"
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

t = time.time()
print("Starting thread pool executor")

results = map(print_numbers, numbers)

for result in results:
    print(result)

print(f"Time taken: {time.time() - t:.2f} seconds")