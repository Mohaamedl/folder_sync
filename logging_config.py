import logging

def setup_logging(log_file):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Remove any existing handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s', datefmt="%d-%m-%Y %H:%M:%S"))

    # Stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s', datefmt="%d-%m-%Y %H:%M:%S"))

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
