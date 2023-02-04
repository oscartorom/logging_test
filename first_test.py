# Just testing the logging library to implement it later

import logging

# Report an normal event during operations
def log_test():
    logging.warning('Will print')
    logging.info("Won't print")

log_test()
# Logging functions are named after the severity
# DEBUG -> Detailed information, when diagnosing problems
# INFO -> Confirms things are working as expected
# WARNING -> Indication something unexpected happened, or of some problem in the future
# ERROR -> Serious problem, sofware could not run some function
# CRITICAL -> Serious error, program won't function


