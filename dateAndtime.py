from datetime import datetime

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

