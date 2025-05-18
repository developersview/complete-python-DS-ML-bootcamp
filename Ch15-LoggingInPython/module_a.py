import logging

def module_a_function():
    # Create a logger for this module
    logger = logging.getLogger(__name__)
    
    # Log some messages
    logger.info('Module A function started')
    logger.debug('This is a debug message from Module A')
    logger.info('Module A function finished')