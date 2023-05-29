import sys
import os
import re
if (sys.argv[1] == '-ping'):
    result=os.popen("ping -c 1 " + sys.argv[2]).read() 
    result=re.findall(r"time=(.*) ms", result) 
    print(result[0]) 
elif (sys.argv[1] == '-simple_print'): 
    print(sys.argv[2]) 
elif (sys.argv[1] == '1'): 
    print("Gorbunov Vladimir") 
elif (sys.argv[1] == '2'): 
    result=os.popen("date -I").read()
    print(result)
else: 
    print(f"unknown input: {sys.argv[1]}") 