'''
Print local time every second in corresponding format 
13-06-2020 16:13:58

Remember to stop endless program using CONTROL-C
'''


import time
import threading

# def printit():
#     timer=threading.Timer(1.0,printit)
#     timer.start()
#     named_tuple = time.localtime() 
#     time_string = time.strftime("%d-%m-%Y %H:%M:%S", named_tuple)
#     print(time_string)
#     timer.cancel()
    
    

# printit()

# while True:
#   localtime = time.localtime()
#   result = time.strftime("%I:%M:%S %p", localtime)
#   print(result, end="", flush=True)
#   print("\r", end="", flush=True)
#   time.sleep(1)
    