import logging
import sys
import time

logger = logging.getLogger(__name__)


def setup_logging():
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
    )


def main():
    logger = logging.getLogger(__name__)
    logger.info("Program started")
    # Application logic here...
    #
    try:
        while True:
            print("Running...")
            time.sleep(2)
    except KeyboardInterrupt:
        print("Shutting down gracefully!")


if __name__ == "__main__":
    setup_logging()
    main()
