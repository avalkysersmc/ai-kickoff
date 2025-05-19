import logging
import time

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.debug('Hello, World!')

    while True:
        logger.debug("This prints once every 5 seconds.")
        time.sleep(5)

if __name__ == '__main__':
    main()
