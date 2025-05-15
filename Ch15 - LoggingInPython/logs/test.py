from logger import setup_logger

my_logger = setup_logger()
print(my_logger)

def add(a, b):
    my_logger.debug(f'Adding {a} and {b}')
    return a + b

my_logger.debug('The addition function was called')
sum = add(10, 25)
my_logger.info(f"Result of addition: {sum}")