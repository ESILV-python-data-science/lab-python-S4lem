# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:27:34 2018

@author: Salem
"""
import logging
import argparse
from sklearn.model_selection import train_test_split

import pandas as pd


# Setup logging
logger = logging.getLogger('classify_images.py')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(ch)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract features, classify page types')
    parser.add_argument('--images-list',required=True)
    args = parser.parse_args()
    

    df = pd.read_csv(args.images_list, names= ["filename", "class", "book"], header= None)
    
    file_list = df["filename"]
    y = df["class"]
    logger.info('Loaded {} images in {}'.format(df.shape,args.images_list))
    
    
    X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.20)
    X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=0.25)
    
    logger.info("Train set size is {}".format(X_train.shape))
    logger.info("Test set size is {}".format(X_test.shape))
    logger.info("valid set size is {}".format(X_valid.shape))