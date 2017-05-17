import logging


# in order to overwrite the log file, add filemode="w"

logging.basicConfig(filename="sample.log", level=logging.INFO)
logging.debug("Debug Message")
logging.info("Informational Message")
logging.error("An error has occured!")
log = logging.getLogger("ex")

try:
    raise RuntimeError
except RuntimeError:
    log.exception("Error!")
