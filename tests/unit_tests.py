import logging
import os
import shutil
import sys
import tempfile

import pytest

current_dir = os.path.dirname(os.path.abspath(__file__))
folder_sync_path = os.path.join(current_dir, '..', 'folder_sync.py')
sys.path.append(folder_sync_path)

from folder_sync import sync_folders
from logging_config import setup_logging


@pytest.fixture(autouse=True)
def setup_logging_for_tests():
    setup_logging("test_log.log")
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
    source, replica = setup_test_environment
    file_path = os.path.join(source, "test_file.txt")
    
    with open(file_path, "w") as f:
        f.write("Hello, World!")

    sync_folders(source, replica, "test_log.log")
    
    log_and_assert(os.path.exists(os.path.join(replica, "test_file.txt")), "File creation test passed.")

def test_modify_file(setup_test_environment):
    source, replica = setup_test_environment
    file_path_source = os.path.join(source, "test_file.txt")
    file_path_replica = os.path.join(replica, "test_file.txt")
    
    with open(file_path_source, "w") as f:
        f.write("Hello, World!")

    sync_folders(source, replica, "test_log.log")
    
    with open(file_path_source, "w") as f:
        f.write("Hello, Universe!")

    sync_folders(source, replica, "test_log.log")
    
    with open(file_path_replica, "r") as f:
        content = f.read()
    
    log_and_assert(content == "Hello, Universe!", "File modification test passed.")

def test_remove_file(setup_test_environment):
    source, replica = setup_test_environment
    file_path_source = os.path.join(source, "test_file.txt")
    file_path_replica = os.path.join(replica, "test_file.txt")
    
    with open(file_path_source, "w") as f:
        f.write("Hello, World!")

    sync_folders(source, replica, "test_log.log")
    os.remove(file_path_source)

    sync_folders(source, replica, "test_log.log")
    
    log_and_assert(not os.path.exists(file_path_replica), "File removal test passed.")

def test_create_directory(setup_test_environment):
    source, replica = setup_test_environment
    dir_path = os.path.join(source, "test_dir")
    
    os.makedirs(dir_path)

    sync_folders(source, replica, "test_log.log")
    
    log_and_assert(os.path.exists(os.path.join(replica, "test_dir")), "Directory creation test passed.")

def test_remove_directory(setup_test_environment):
    source, replica = setup_test_environment
    dir_path_source = os.path.join(source, "test_dir")
    dir_path_replica = os.path.join(replica, "test_dir")
    
    os.makedirs(dir_path_source)

    sync_folders(source, replica, "test_log.log")
    shutil.rmtree(dir_path_source)

    sync_folders(source, replica, "test_log.log")
    
    log_and_assert(not os.path.exists(dir_path_replica), "Directory removal test passed.")
