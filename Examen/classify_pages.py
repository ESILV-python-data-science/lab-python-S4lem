# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:27:34 2018

@author: Salem
"""
import logging
import argparse
import time
import sys
import numpy as np

from PIL import Image, ImageFilter
from tqdm import tqdm
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

import pandas as pd

# default sub-resolution
IMG_FEATURE_SIZE = (12, 16)

def extract_features(img):
    # convert color images to grey level
    gray_img = img.convert('L')
    
    # reduce the image to a given size
    reduced_img = gray_img.resize(IMG_FEATURE_SIZE, Image.BOX).filter(ImageFilter.SHARPEN)
    return [255 - i for i in reduced_img.getdata()]



# Setup logging
logger = logging.getLogger('classify_images.py')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(ch)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract features, classify page types')
    parser.add_argument('--images-list',required=True)
    parser.add_argument('--limit-samples', type=int, help='limit the number of samples to consider for training')

    args = parser.parse_args()
    

    df = pd.read_csv(args.images_list, names= ["filename", "class", "book"], header= None)

    class_data = []
    data = []
    file_list = df["filename"]
    y = df["class"]
    for idx, i_path in df.iterrows():
        try:
            page_image = Image.open(i_path["filename"])
            data.append(extract_features(page_image))
            class_data.append(i_path["class"])
        except FileNotFoundError: 
            pass
        
    # convert to np.array
    X = np.array(data)

    # check that we have data
    if not data:
        logger.error("Could not extract any feature vector or class")
        sys.exit(1)
        
    df_features = pd.DataFrame(data = X)
    df_features["class"] = y
    
    if args.limit_samples:
        df_features = df_features.sample(n = args.limit_samples)
    
    logger.info('Loaded {} images in {}'.format(df.shape,args.images_list))
    
    
    X_train, X_test, y_train, y_test = train_test_split(X, class_data, test_size=0.20)
    X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=0.25)
    
    logger.info("Train set size is {}".format(X_train.shape))
    logger.info("Test set size is {}".format(X_test.shape))
    logger.info("valid set size is {}".format(X_valid.shape))
    
    clf = LogisticRegression()
    logger.info('Using logistic regression...')
    
    # Do Training@
    t0 = time.time()
    clf.fit(X_train, y_train) 
    logger.info("Training done in %0.3fs" % (time.time() - t0))
    
    # Do testing on validation set
    logger.info("Testing Classifier on validation set")
    t0 = time.time()
    predicted = clf.predict(X_valid)
    print(metrics.accuracy_score(y_valid, predicted))
    print(metrics.classification_report(y_valid, predicted))
    logger.info("Testing done in %0.3fs" % (time.time() - t0))