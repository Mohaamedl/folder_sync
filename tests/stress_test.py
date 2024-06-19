import logging
import os
import shutil
import tempfile
import time

import pytest

from folder_sync import sync_folders
from logging_config import setup_logging


@pytest.fixture(autouse=True)
def setup_logging_for_tests():
    setup_logging("test_log.log")

@pytest.fixture
def setup_test_environment():
    source = tempfile.mkdtemp()
    replica = tempfile.mkdtemp()
    yield source, replica
    shutil.rmtree(source)
    shutil.rmtree(replica)

def log_and_assert(condition, message):
    logging.info(message)
    logging.getLogger().handlers[0].flush()  # Ensure the log is written immediately
    assert condition, message

def test_stress_sync(setup_test_environment):
    source, replica = setup_test_environment
    
    num_files = 10000
    file_size = 1024  # 1 KB per file

    # Create a large number of files in the source directory
    start_time = time.time()
    for i in range(num_files):
        file_path = os.path.join(source, f"test_file_{i}.txt")
        with open(file_path, "wb") as f:
            f.write(os.urandom(file_size))
    creation_duration = time.time() - start_time
    logging.info(f"Created {num_files} files of {file_size} bytes each in {creation_duration:.2f} seconds")

    # Sync the source to the replica
    start_time = time.time()
    sync_folders(source, replica, "test_log.log")
    sync_duration = time.time() - start_time
    logging.info(f"Synchronized {num_files} files in {sync_duration:.2f} seconds")

    # Verify that all files were copied
    all_files_copied = all(os.path.exists(os.path.join(replica, f"test_file_{i}.txt")) for i in range(num_files))
    log_and_assert(all_files_copied, "Stress test: all files copied successfully.")
