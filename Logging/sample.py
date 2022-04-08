from cmath import log
import logging

# DEBUG - Detailed information, typically of interest when diagnosing problems.
# INFO - Confirmation of things working as expected.
# WARNING - Indication of something unexpected or a problem in the near future e.g. 'disk space low'.
# ERROR - A more serious problem due to which the program was unable to perform a function.
# CRITICAL - A serious error, indicating that the program itself may not be able to continue executing.

# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

logging.basicConfig(level=logging.DEBUG)  
logging.debug('The dubug message is logged')  
