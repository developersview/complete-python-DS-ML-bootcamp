'''
Multithreading
When to use Multi Threading
1. I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
2. Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.
'''
import threading
import time

def print_numbers():
    for i in range(10):
        time.sleep(2)
        print(f"Number: {i}")

def print_letters():
    for letter in 'abcedefghijklmnopqrstuvwxyz':
        time.sleep(2)
        print(f"Letter: {letter}")
        

# Create 2 threads
t = time.time()

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

#Start the threads
t1.start()
t2.start()

# Wait for the threads to finish
t1.join()
t2.join()

finished_time = time.time() - t
print(f"Finished in {finished_time} seconds")