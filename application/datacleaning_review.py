# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 15:31:15 2016

@author: Elayne Ruane
"""

import zipfile
import os
import csv

def create_path(path):
    ''' function that creates a path if it does not already exist
    
    parameters
    ----------
    path: a string that represents the path to be created
    '''
    path = path
    if not os.path.exists(path):
        os.makedirs(path)

def extract_zip(zipa, path):
    '''function that extracts files from a zip file
    
    parameters
    ----------
    zipa: a string that represents the path to a zip file
    path: a string that represents the directory to extract the files to
    '''
    zipa = zipfile.ZipFile(zipa)
    zipa.extractall(path)

