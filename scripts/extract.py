# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 09:30:00 2023

@author: Win 10
"""

import os
import kaggle
from zipfile import ZipFile

kaggle.api.authenticate()
from zipfile import ZipFile

def extract_kaggle_api():
    file_exist = os.path.exists('C:/Users/Win 10/Downloads/Projects/ETL_2/data/SampleSuperstore.csv')
    if not file_exist:

        print("collecting data from kaggle api")
        file_download = "bravehart101/sample-supermarket-dataset/SampleSuperstore.csv"
        kaggle.api.dataset_download_file(dataset=file_download,file_name='SampleSuperstore.csv',path='C:/Users/Win 10/Downloads/Projects/ETL_2/data/zip')
        print("successfully downloaded dataset")
        with ZipFile('../data/zip/SampleSuperstore.csv.zip','r') as file:
            file.extractall('C:/Users/Win 10/Downloads/Projects/ETL_2/data/')
        print("unzipped file")
        
def main():      
    extract_kaggle_api()


