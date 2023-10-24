
#? Module
    # collection of python declarations intended to be used as a tol
    # also referred to as libraries or packages
    #syntax: from 'module_name' import 'object_name'

from datetime import datetime
import random

current_time = datetime.now()
print(current_time)

random_list = []

for i in range(101):
    random_list.append(random.randint(1,100))
print(random_list)

#? using an alias to import a module 
# from matplotlib import pyplot as plt

#? importing from another file 
    # syntax: from 'file name' import 'function name'
    
#? DateTimes (video)
    # 