import logging
import os
import shutil
import sys
import tempfile

import pytest

from folder_sync import sync_folders
from logging_config import setup_logging

log_file = "tests/unit_test_log.log"
@pytest.fixture(autouse=True)
def setup_logging_for_tests():
    setup_logging(log_file)
    print('deu')

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

def test_create_file(setup_test_environment):
    """Tests file creation on replica"""
    source, replica = setup_test_environment
    file_path = os.path.join(source, "test_file.txt")
    
    with open(file_path, "w") as f:
        f.write("Hello, World!")

    sync_folders(source, replica,log_file)
    
    log_and_assert(os.path.exists(os.path.join(replica, "test_file.txt")), "File creation test passed.")

def test_modify_file(setup_test_environment):
    """Tests file modification on replica"""
    source, replica = setup_test_environment
    file_path_source = os.path.join(source, "test_file.txt")
    file_path_replica = os.path.join(replica, "test_file.txt")
    
    with open(file_path_source, "w") as f:
        f.write("Hello, World!")

    sync_folders(source, replica, log_file)
    
    with open(file_path_source, "w") as f:
        f.write("Hello, Universe!")

    sync_folders(source, replica, log_file)
    
    with open(file_path_replica, "r") as f:
        content = f.read()
    
    log_and_assert(content == "Hello, Universe!", "File modification test passed.")

def test_remove_file(setup_test_environment):
    """Tests file removal on replica"""
    source, replica = setup_test_environment
    file_path_source = os.path.join(source, "test_file.txt")
    file_path_replica = os.path.join(replica, "test_file.txt")
    
    with open(file_path_source, "w") as f:
        f.write("Hello, World!")

    sync_folders(source, replica, log_file)
    os.remove(file_path_source)

    sync_folders(source, replica, log_file)
    
    log_and_assert(not os.path.exists(file_path_replica), "File removal test passed.")

def test_create_directory(setup_test_environment):
    """Tests directory creation on replica"""
    source, replica = setup_test_environment
    dir_path = os.path.join(source, "test_dir")
    
    os.makedirs(dir_path)

    sync_folders(source, replica, log_file)
    
    log_and_assert(os.path.exists(os.path.join(replica, "test_dir")), "Directory creation test passed.")

def test_remove_directory(setup_test_environment):
    """Tests directory removal on replica"""
    source, replica = setup_test_environment
    dir_path_source = os.path.join(source, "test_dir")
    dir_path_replica = os.path.join(replica, "test_dir")
    
    os.makedirs(dir_path_source)

    sync_folders(source, replica, log_file)
    shutil.rmtree(dir_path_source)

    sync_folders(source, replica, log_file)
    
    log_and_assert(not os.path.exists(dir_path_replica), "Directory removal test passed.")
