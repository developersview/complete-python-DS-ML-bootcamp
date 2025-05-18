import logging

def module_b_function():
    # Create a logger for this module
    logger = logging.getLogger(__name__)
    
    # Log some messages
    logger.info('Module B function started')
    logger.debug('This is a debug message from Module B')
    logger.info('Module B function finished')