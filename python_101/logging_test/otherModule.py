import logging

module_logger = logging.getLogger("sample.otherModule")

def add(x, y):
    logger = logging.getLogger("sample.otherModule.add")
    logger.info("added %s and %s to get %s" %(x, y, x+y))
    return x + y
