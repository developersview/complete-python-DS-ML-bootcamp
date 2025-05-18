import logging

def setup_logger(name):
    # # Remove all handlers associated with the root logger
    # for handler in logging.root.handlers[:]:
    #     logging.root.removeHandler(handler)
    # Create a custom logger

    logging.basicConfig(
        filename='test.log',
        filemode='a',
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s- %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    return logging.getLogger(name)