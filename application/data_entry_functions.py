# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 23:54:44 2016

@author: Elayne Ruane
"""

import csv
import time as tm
import datetime
from dateutil.parser import parse
#import models
#import linear_model

def epochtime(x):
    ''' function that reads in a date and converts it to epoch time format
    
    parameters
    ----------
    x: a string that represents a date and time
    
    output
    ------
    an integer that represents the epoch time of the input
    '''
    # slice string to extract 'GMT' and replace with 'UTC', this is os agnostic
    x = x[:20] + "UTC" + x[23:]
    # convert string to datetime
    string = parse(x)
    # convert to epoch time
    epoch = int(tm.mktime(string.timetuple()))
    return epoch

def parseName(x):
    ''' function that reads in a string and returns the building name and room number
    
    parameters
    ----------
    x: a string in the format 'Campus > Building Name > Room-000'
    
    output
    ------
    building: a string, the name of the building in lowercase
    room: the int value that represents the room
    '''
    # variable that contains index of '>' character and adds 2     
    inst1 = x.find(">")+2 # finds beginning of building name
    #  variable that contains index of second '>' character
    inst2 = x.find(">", inst1) # begins searching at index inst1
    
    building = x[inst1:inst2-1].lower()
    room = x[inst2+6:]
    
    return (building,room)

def fileToList(file):
    ''' function that reads in a csv file and returns a list of each row of the file
    
    parameters
    ----------
    file: the name of a csv file or variable assigned the name of a csv file
    '''
    
    #open file as read only
    with open(file, 'r') as f:
        # reader object iterates over lines in the file, each element returned as a string
        mycsv = csv.reader(f)
        # create a list of lists
        mylist = list(mycsv)
    return mylist

def insertModCode(db_models, mod_table, field1, field2, user_table, username, modcode):
    ''' function that reads in database parameters 
    
    called by checkModCode function
    
    parameters
    ----------
    db_models: a file containing database models
    mod_table: the name of the class which represents the table that stores module codes
    field1: the name of the data field in 'mod_table' that stores the module code
    field2: the name of the data field in 'mod_table' that stores the module instructor
    user_table: the name of the class which represents the table that stores user data
    username: the name of the datafield in 'user_table' that stores the username
    modcode: a variable that contains a module code
    '''
    #insert data into db
    db_models.mod_table.create(field1 = modcode,
                               field2 = user_table.username
                               )
    

def checkModCode(file, db_models, mod_table, field1, field2, user_table, username):
    ''' function that reads in a file, checks for any unique module codes, and inserts them into a DB
    
    calls fileToList function and insertModCode function
    
    parameters
    ----------
    file: the name of a csv file or variable assigned the name of a csv file
    db_models: a file containing database models
    mod_table: the name of the class which represents the table that stores module codes
    field1: the name of the data field in 'mod_table' that stores the module code
    field2: the name of the data field in 'mod_table' that stores the module instructor
    user_table: the name of the class which represents the table that stores user data
    username: the name of the datafield in 'user_table' that stores the username
    
    '''
    # create an empty list
    modlist = []
    # create mylist variable containing data by calling fileToList function
    mylist = fileToList(file)
    # iterate trhough mylist, start from 1 to skip data field names
    for i in range (1, len(mylist)):
        # if module code exists
        if len(mylist[i][3])>1:
            # add to list
            modulecode = mylist[i][3]
            
            if modulecode in modlist:
                continue
            else:
                # call function to insert modcode into db
                insertModCode(db_models, mod_table, field1, field2, user_table, username)
                # add modulecode to list 
                modlist.append(modulecode) 