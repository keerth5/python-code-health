#!/usr/bin/env python
# -*- coding: utf-8 -*-

from user_manager import *  # Wildcard import
from data_processor import DataProcessor
import utils
import database_handler as db

DEBUG=True  # Global constant not in UPPER_CASE properly placed

def main():
    print "="*50  # Python 2 print statement
    print "Starting Application"
    print "="*50
    
    # Hardcoded test data
    test_users=[
        ('John',25,'john@test.com'),
        ('Jane',30,'jane@test.com'),
        ('Bob',35,'bob@test.com')
    ]
    
    # Adding users
    for user in test_users:
        addUser(user[0],user[1],user[2])
    
    # Using legacy string formatting
    message="Total users: %d" % len(USERS)
    print message
    
    # Instantiating processor
    processor=DataProcessor()
    test_data=[1,-2,3,-4,5]
    processed=processor.processData(test_data)
    print "Processed data:",processed
    
    # Dangerous operations
    result=utils.divide(10,0)  # Will crash
    
    # Complex calculation with magic numbers
    calc_result=processor.calculate(1,2,3,4,5,6,7)
    print "Calculation result:",calc_result
    
    # File operations without error handling
    try:
        content=processor.readFile('nonexistent.txt')
    except Exception as e:
        print "Error reading file"
    
    # Database operations
    dbh=db.DatabaseHandler()
    dbh.connect('users.db')
    
    # SQL injection vulnerability
    user_input="test@example.com"
    dbh.insertUser("Test User",user_input)
    
    if DEBUG:
        print "Debug mode enabled"


if __name__=='__main__':
    main()

