import logging


def setup_logging(log_file):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt="%d-%m-%Y %H:%M:%S",
                        handlers=[
                            logging.FileHandler(log_file),
                            logging.StreamHandler()
                        ])
