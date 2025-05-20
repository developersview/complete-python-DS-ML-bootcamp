''' 
Processes that run in parallel.
There are two reasons to use multiprocessing:
1. CPU-Bound Tasks-Tasks that are heavy on CPU usage (e.g., mathematical computations, data processing).
2. PArallel execution- Multiple cores of the CPU
'''
import multiprocessing
import time

def sqaure_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square of {i} is: {i * i}")

def cube_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Cube of {i} is: {i * i * i}")


if __name__ == '__main__':
    # Create 2 processes
    p1 = multiprocessing.Process(target=sqaure_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)


    t = time.time()

    #start the processes
    p1.start()
    p2.start()

    # Wait for the processes to finish
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(f"Finished in {finished_time} seconds")
