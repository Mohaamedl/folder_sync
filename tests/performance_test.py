import logging
import os
import shutil
import tempfile
import time

import psutil
import pytest

from folder_sync import sync_folders
from logging_config import setup_logging


@pytest.fixture(autouse=True)
def setup_logging_for_tests():
    setup_logging("tests/performance_test_log.log")
    yield
    logging.shutdown()  # Ensure all logging is flushed at the end of tests

@pytest.fixture
def setup_test_environment():
    source = tempfile.mkdtemp()
    replica = tempfile.mkdtemp()
    yield source, replica
    shutil.rmtree(source)
    shutil.rmtree(replica)

def log_and_assert(condition, message):
    logging.info(message)
    for handler in logging.getLogger().handlers:
        handler.flush()  # Ensure the log is written immediately
    assert condition, message

def measure_resource_usage():
    # CPU usage
    cpu_percent = psutil.cpu_percent(interval=1)

    # Memory usage
    memory_info = psutil.Process(os.getpid()).memory_info()
    memory_mb = memory_info.rss / 1024 / 1024  # Convert to MB

    return cpu_percent, memory_mb

def test_performance_sync(setup_test_environment):
    """Performance testing and evaluation of script functionality."""
    logging.info("Starting test_performance_sync")
    source, replica = setup_test_environment
    
    num_files = 1000
    file_size = 1024  # 1 KB per file

    # Create test files
    start_time = time.time()
    total_size_created = 0
    for i in range(num_files):
        file_path = os.path.join(source, f"test_file_{i}.txt")
        with open(file_path, "wb") as f:
            content = os.urandom(file_size)
            f.write(content)
            total_size_created += len(content)
    creation_duration = time.time() - start_time

    logging.info(f"Created {num_files} files ({total_size_created / 1024 / 1024:.2f} MB) in {creation_duration:.2f} seconds")

    # Synchronize folders
    start_time = time.time()
    sync_folders(source, replica, "tests/performance_test_log.log")
    sync_duration = time.time() - start_time

    # Verify all files were copied
    all_files_copied = all(os.path.exists(os.path.join(replica, f"test_file_{i}.txt")) for i in range(num_files))
    log_and_assert(all_files_copied, "Performance test: all files copied successfully.")

    logging.info(f"Synchronized {num_files} files in {sync_duration:.2f} seconds")

    # Measure resource usage
    cpu_usage, memory_usage = measure_resource_usage()
    logging.info(f"CPU Usage: {cpu_usage:.2f}%")
    logging.info(f"Memory Usage: {memory_usage:.2f} MB")

    # Ensure all logs are written to file
    for handler in logging.getLogger().handlers:
        handler.flush()
