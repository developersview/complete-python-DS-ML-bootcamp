''' 
Multlthreading with process pool executor
'''
from concurrent.futures import ProcessPoolExecutor
import time

def square_number(n):
    time.sleep(1)
    return f"Square of {n}: {n * n}"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

if __name__ == "__main__":
    t = time.time()
    print("Starting process pool executor")

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)

    for result in results:
        print(result)

    print(f"Time taken: {time.time() - t:.2f} seconds")