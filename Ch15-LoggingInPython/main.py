''' 
Assignment 8: Logging in a Multi-Module Application
1. Write a Python script that sets up logging for a multi-module application. Each module should have its own logger.
2. Modify the script to propagate log messages from each module's logger to a root logger that handles logging to a file.
'''

import logging
from module_a import module_a_function
from module_b import module_b_function
import logging.config

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

def setup_logging():
    log_config = {
        'version': 1,
        'formatters': {
            'default': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s:%(lineno)d'
            }
        },
        'handlers': {
            'file_handler': {
                'class': 'logging.FileHandler',
                'filename': 'main_app.log',
                'formatter': 'default',
                'level': 'DEBUG'
            },
            'console_handler': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': 'DEBUG'
            }
        },
        'root': {
            'handlers': ['file_handler', 'console_handler'],
            'level': 'DEBUG',
        }
    }

    logging.config.dictConfig(log_config)

#main function
if __name__ == '__main__':
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Main application started')
    module_a_function()
    module_b_function()
    logger.info('Main application finished')