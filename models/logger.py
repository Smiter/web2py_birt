
import logging
import logging.handlers
from gluon import *


def get_configured_logger(name):
    logger = logging.getLogger(name)
    if (len(logger.handlers) == 0):
        # This logger has no handlers, so we can assume it hasn't yet been configured
        # (Configure logger)

        # Create default handler
        if request.env.web2py_runtime_gae:
            # Create GAEHandler
            handler = GAEHandler()
        else:
            # Create RotatingFileHandler
            import os
            formatter = "%(funcName)s():%(lineno)d %(message)s \n"
            handler = logging.handlers.RotatingFileHandler(os.path.join(request.folder, 'private/app3.log'), maxBytes=10000000, backupCount=2)
            handler.setFormatter(logging.Formatter(formatter))

        handler.setLevel(logging.DEBUG)

        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)

    return logger

# Assign application logger to a global var
logger = get_configured_logger("mylogger443223334")
