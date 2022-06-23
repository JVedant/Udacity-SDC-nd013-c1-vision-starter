import argparse
import glob
import os
import random
import shutil

import numpy as np

from utils import get_module_logger


def split(source, destination):
    """
    Create three splits from the processed records. The files should be moved to new folders in the
    same directory. This folder should be named train, val and test.

    args:
        - source [str]: source data directory, contains the processed tf records
        - destination [str]: destination data directory, contains 3 sub folders: train / val / test
    """
    # TODO: Implement function
    
    files = glob.glob(f"{source}/*.tfrecord")
    np.random.shuffle(files)
    total_files = len(files)
    
    # Split the data in 3 parts
    train_files, validation_files, test_files = files[0:int(total_files * 0.80)], files[int(total_files * 0.80): int(total_files * 0.90)], files[int(total_files * 0.90): total_files]
    
    # Get the destination directories
    train_destination, validation_destination, test_destination = os.path.join(destination, "train"), os.path.join(destination, "valid"), os.path.join(destination, "test")

    os.makedirs(train_destination, exist_ok=True)
    os.makedirs(validation_destination, exist_ok=True)
    os.makedirs(test_destination, exist_ok=True)
    
    for each in train_files:
        file_name = each.split("/")[-1]
        shutil.copy(each, os.path.join(train_destination, file_name))
        
    for each in test_files:
        file_name = each.split("/")[-1]
        shutil.copy(each, os.path.join(test_destination, file_name))
        
    for each in validation_files:
        file_name = each.split("/")[-1]
        shutil.copy(each, os.path.join(validation_destination, file_name))

        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--source', required=True,
                        help='source data directory')
    parser.add_argument('--destination', required=True,
                        help='destination data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.source, args.destination)