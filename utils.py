import os
import sys
import re
import json
import random  # Unused import

def divide(a,b):
    # No error handling for division by zero
    return a/b

def parseJSON(json_string):
    # Poor error handling
    try:
        return json.loads(json_string)
    except:
        return {}

def is_valid_email(email):
    # Overly simplistic validation
    if '@' in email and '.' in email:
        return True
    return False

def sort_list(l):  # 'l' is a bad variable name (looks like 1)
    # Inefficient bubble sort implementation
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    return l

def readConfig(filename='config.txt'):
    # Multiple issues
    f=open(filename)
    config={}
    for line in f:
        parts=line.split('=')
        config[parts[0]]=parts[1]  # Will crash if no '='
    return config

class Singleton:  # Broken singleton implementation
    instance=None
    def __init__(self):
        if Singleton.instance!=None:
            raise Exception("Singleton already exists")
        else:
            Singleton.instance=self


def legacy_string_concat(items):
    result=""
    for item in items:
        result=result+str(item)+","  # Inefficient string concatenation
    return result[:-1]

def compare(a,b):
    # Using 'is' for value comparison
    if a is b:
        return True
    return False

# Code in module level that runs on import
print "Utils module loaded"
temp_file=open('temp.log','a')
temp_file.write('Module imported\n')
temp_file.close()

