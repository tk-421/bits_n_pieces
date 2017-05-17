import logging
import otherModule
import os

def main():
    # Main entry point for app

    # create logger
    log = logging.getLogger("sample")
    log.setLevel(logging.INFO)

    # create file handler for logger
    handler = logging.FileHandler("sample2.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # add handler to logger
    log.addHandler(handler)

    log.info("Program started")
    result = otherModule.add(7,8)
    log.info("Done!")

if __name__ == "__main__":
    main()
