from datetime import datetime
import time 
print(datetime.now())
sec = datetime.now().second
min = datetime.now().minute
hour = datetime.now().hour
day =  datetime.now().day


print("day = ",day,",sec = ", sec, ",hour = ",hour)
print(sec + 20) #can print values over 60 so use %60
print((sec + 20) %60)

wait_until = ((datetime.now().second +1) % 60)
while(datetime.now().second != wait_until):
    print(datetime.now())
    # will print current date-time inclufin microsec till one sec passes

print(f"current time in sec = {time.time()}")
time.sleep(0.5) # pauses execution for x second

# using next step we can see howmuch time a func took
start = time.time()
print(start - time.time())