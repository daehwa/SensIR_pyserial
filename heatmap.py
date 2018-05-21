import matplotlib.pyplot as plt
import serial
import numpy as np
import time

port = '/dev/ttyACM1'
ard = serial.Serial(port,9600,timeout=None)
#time.sleep(2)
#msg = ard.read(ard.inWaiting())
#print(msg)

flag = False
a = np.array([])
while(1):
  data = ard.readline()
  data = (data.split("\n"))[0];
  #End
  if(int(data)==-2):
    break;
  if(flag):
    print(data)
    a = np.append(a,int(data))
  #Start
  if(int(data)==-1):
    flag = True

#a = np.random.random((11, 11))
print(a)
a = np.reshape(a,(11,11))
plt.imshow(a, cmap='hot', interpolation='nearest')
plt.show()
