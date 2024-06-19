# folder_sync
This script performs one-way synchronization between a source folder and a replica folder. It periodically updates the replica folder to match the source folder, logging file operations to a specified log file and the console.
## criate enviroment(optional)
python -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate


## Install Dependencies
```
pip install pytest`
```

## Usage

```bash
python folder_sync.py <source_folder> <replica_folder> <interval_in_seconds> <log_file>

Arguments
<source_folder>: Path to the source folder.
<replica_folder>: Path to the replica folder.
<interval_in_seconds>: Interval in seconds between synchronization checks.
<log_file>: Path to the log file.
```
# execute tests :
pytest


#### Example of use
python folder_sync.py /path/to/source /path/to/replica 60 /path/to/logfile.log

## Requirements
- Python 3.6 or higher
