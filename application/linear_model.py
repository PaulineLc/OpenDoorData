# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 11:36:54 2016

@author: Elayne Ruane

This script contains a linear regression model that predicts the number of
people in a room based on the number of devices connected to wifi access points
in that room.

The accuracy of the model can be tested by occupancy data collected via survey.

Wifi logs contain readings at five minute intervatls. We use the median number
of devices connected per hour.

The model was originally prepared in iPython notebooks.

"""

# ---------- IMPORT NECESSARY LIBRARIES

import os
# import csv package for reading from and writing to csv files
import csv
# import pandas package to read and merge csv files
import pandas as pd


# ---------- READ DATA FROM CSV FILES INTO DATAFRAME

### OS AGNOSTIC VERSION
# a = '..' # removed slash
# b = 'cleaned_data' # removed slash
# c = 'full.csv'
# d = 'survey_data.csv'

# pathw = os.path.join(a, b, c)
# paths = os.path.join(a, b, d)

# print('Reading files from ', pathw)
# print('Reading files from ', paths)

# wifi_df = pd.read_csv(pathw, names=['room', 'event_time', 'ass', 'auth'])
# occupancy_df = pd.read_csv(paths)

wifi_df = pd.read_csv("D:\\Users\\Elayne Ruane\\Documents\\CSI MA\\research_practicum\\cleaned_data\\full.csv", names=['room', 'event_time', 'ass', 'auth'])
occupancy_df = pd.read_csv("D:\\Users\\Elayne Ruane\\Documents\\CSI MA\\research_practicum\\cleaned_data\\survey_data.csv")

## TEST IF FILES READ IN CORRECTLY

from model_functions import isempty_df

print('wifi log data successfully loaded into dataframe: ',isempty_df(wifi_df))
print('occupancy data successfully loaded into dataframe: ',isempty_df(occupancy_df))


# ---------- CLEAN DATA FOR MODEL

del occupancy_df['Unnamed: 0'] # delete unwanted column


from model_functions import convert_to_epoch
# convert 'event_time' values from timestamp to epoch so can convert to DATETIME
convert_to_epoch(wifi_df, 'event_time')

from model_functions import room_number
room_number(wifi_df, 'room')

# convert 'event_time' values from EPOCH to DATETIME in both dataframes
wifi_df['event_time'] = pd.to_datetime(wifi_df.event_time, unit='s')
occupancy_df['event_time'] = pd.to_datetime(occupancy_df.event_time, unit='s')

# use 'event_time' as dataframe index in both dataframes
wifi_df.set_index('event_time', inplace=True)
occupancy_df.set_index('event_time', inplace=True)

# create two new columns, event_hour and event_day for use in calculation of the median hourly value
wifi_df['event_hour'] = wifi_df.index.hour
wifi_df['event_day'] = wifi_df.index.day

occupancy_df['event_hour'] = occupancy_df.index.hour
occupancy_df['event_day'] = occupancy_df.index.day



# get median hourly values for each day for each room and put in 'median_df' dataframe
median_df = wifi_df.groupby(['room', 'event_day', 'event_hour'], as_index=False).median()

# merge median data and occupancy data into single dataframe, 'df'
median_df['room'] = median_df['room'].astype(int)
df = pd.merge(median_df, occupancy_df, on=['room', 'event_day', 'event_hour'], how='inner')



# ---------- DATA ANALYSIS

from model_functions import estimate_occ
# estimate the number of occupancts from the survey data to assess model accuracy
estimate_occ(df, 'room', 'occupancy')

# create a test data set and a train data set from 'df'
df_train = df[:int(0.7 * df.shape[0])]
df_test = df[int(0.7 * df.shape[0]):]



# ---------- CREATE AND TRAIN THE MODEL

import statsmodels.formula.api as sm
# can also use associated but higher correlation with authenticated 
lm = sm.ols(formula='est_occupants ~ auth', data=df_train).fit()

intercept = lm.params.Intercept
coef = lm.params.auth

# ---------- PUT MODEL COEFFICIENTS IN DATABASE

import models

# insert model parameters into database
models.regressionModel.create(offset = intercept,
                              weight = coef
                              )
    
    