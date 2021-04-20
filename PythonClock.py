import sys
import time
import os
import math
clear = "\n" * 100
Seconds = 0
Minutes = 0
Hours = 0
secsTimer = 0
print ("Start Time :")
print ("-------------")
startHour=input("What hour is it? ")
startMin=input("What minute is it? ")
startSec=input("What second is it? ")
print ("")
print ("End Time")
print ("--------")
endHour=input("What hour do you want go to? ")
endMin=input("What minute do you want go to? ")
endSec=input("What sec do you want go to? ")
midhour = (int(startHour) * 3600)
midhour2 = (int(endHour) * 3600)
midmin = (int(startMin) * 60)
midmin2 = (int(endMin) * 60)
secsStart = (int(midhour) + int(midmin) + int(startSec))
secsEnd = (int(midhour2) + int(midmin2) + int(endSec))
secsLeft = (int(secsEnd) - int(secsStart))
while True:
  print (clear)
  Seconds = Seconds + 1

  
  print ("Start Time :")
  print ("-------------")
  print ("Start Hour  : " + str(startHour))
  print ("Start Minute: " + str(startMin))
  print ("Start Second: " + str(startSec))
  print ("")
  print ("End Time")
  print ("--------")
  print ("End Hour  : " + str(endHour))
  print ("End Minute: " + str(endMin))
  print ("End Second: " + str(endSec))
  print ("")
  secsLeft = secsLeft - 1
  if Seconds == 60:
    Minutes = Minutes + 1
    Seconds = 0
  if Minutes == 60:
    Hours = Hours + 1
    Seconds = 0
    Minutes = 0
  if secsLeft < 0:
   sys.exit()
  print("Time until Finished:" + str(secsLeft) + " Seconds")
  print ("Time elapsed: " + str(Hours) + " Hours " + str
  (Minutes) + " Minutes " + str(Seconds) + " Seconds")
  time.sleep(1)
