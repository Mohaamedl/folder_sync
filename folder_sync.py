import argparse
import hashlib
import logging
import os
import shutil
import time


def calculate_md5(file_path):
    """Calculate MD5 checksum of a file"""
    hash_md5 = hashlib.md5()
    with open(file_path,"rb") as f:
        for chunk in iter(lambda : f.read(4096),b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
def sync_folders(source,replica, log_file):
    """Synchronize replica folder to match the source folder."""
    try:
        
        logging.basicConfig(filename =log_file,level=logging.INFO,
                            format="%(asctime)s - %(message)s",
                            datefmt="%d-%m-%Y %H:%M:%S")
        # Synchronize directories
        for src_dir,dirs,files in os.walk(source):
            relative_path = os.path.relpath(src_dir,source)
            replica_dir = os.path.join(replica,relative_path)
            if not os.path.exists(replica_dir):
                os.makedirs(replica_dir)
                logging.info(f"Directory created: {replica_dir}")
                print(f"Dicrectory created: {replica_dir}")
            for file in files:
                src_file = os.path.join(src_dir,file)
                replica_file = os.path.join(replica_dir,file)
                try:
                    if not os.path.exists(replica_file):
                        shutil.copy2(src_file,replica_file)
                        logging.info(f"File copied: {src_file} to {replica_file}")
                        print(f"File copied: {src_file} to {replica_file}")
                    elif calculate_md5(src_file) != calculate_md5(replica_file):
                        shutil.copy2(src_file,replica_file)
                        logging.info(f"Updated file content : {src_file} to {replica_file}")
                        print(f"Updated file content: {src_file} to {replica_file}")

                except Exception as e:
                    logging.error(f"Error copying file {src_file}: {e}")
                    print(f"Error copying file {src_file}: {e}")
        # Remove files and directories inreplica that are not in source
        for rep_dir,dirs,files in os.walk(replica,topdown=False):
            relative_path = os.path.relpath(rep_dir,replica)
            src_dir = os.path.join(source,relative_path)
            for file in files:
                rep_file = os.path.join(rep_dir,file)
                src_file = os.path.join(src_dir,file)
                try:
                    if not os.path.exists(src_file):
                        os.remove(rep_file)
                        logging.info(f"File removed: {rep_file}")
                        print(f"File removed: {rep_file}")
                except Exception as e:
                    logging.error(f"Error removing file {rep_file}: {e}")
                    print(f"Error removing file {rep_file}: {e}")
            for dir in dirs:
                rep_sub_dir = os.path.join(rep_dir,dir)
                src_sub_dir = os.path.join(src_dir,dir)
                try:
                    if not os.path.exists(src_sub_dir):
                        shutil.rmtree(rep_sub_dir)
                        logging.info(f"Directory removed: {rep_sub_dir}")
                        print(f"Directory removed: {rep_sub_dir}")
                except Exception as e:
                    logging.error(f"Error removing directory {rep_sub_dir}: {e}")
                    print(f"Error removing directory {rep_sub_dir}: {e}")


    except Exception as e:
        logging.error(f"Exception occured during synchronization: {e}")
        print(f"Exception occured during synchronization: {e}")
        exit


def main():
    parser = argparse.ArgumentParser(description="One-way Folder Synchronization")
    parser.add_argument("source",help="Source folder path")
    parser.add_argument("replica",help="Replica folder path")
    parser.add_argument("interval",help="Synchronization interval in seconds", type=int)
    parser.add_argument("log_file",help="Log file path")
    args = parser.parse_args()

    while True:
        sync_folders(args.source,args.replica,args.log_file)
        time.sleep(args.interval)
if __name__=="__main__":
    main()