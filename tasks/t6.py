'''
Print local time in corresponding format 
13-06-2020 16:13:58
'''
import time

named_tuple = time.localtime() 
time_string = time.strftime("%d-%m-%Y %H:%M:%S", named_tuple)

print(time_string)
