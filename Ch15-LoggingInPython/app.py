import logging

## basic config

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s- %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("CalculatorApp")

def add(a, b):
    logger.debug(f'Adding {a} and {b} = {a + b}')
    return a + b

def subtract(a, b):
    logger.debug(f'Subtracting {a} and {b} = {a - b}')
    return a - b

def multiply(a, b):
    logger.debug(f'Multiplying {a} and {b} = {a * b}')
    return a * b

def divide(a, b):
    try:
        result = a / b
        logger.debug(f'Dividing {a} and {b} = {result}')
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    

if __name__ == "__main__":
    logger.info("Starting Calculator App")

    a = 10
    b = 50

    add(a, b)
    subtract(a, b)
    multiply(a, b)
    divide(a, b)

    logger.info("Calculator App finished")
