#TIME
import datetime
t= datetime.time(4,20,1,30)
print(t)
print(t.hour)
print(t.tzinfo)
#Note: A time instance only holds values of time, and not a date associated with the time.

#We can also check the min and max values a time of day can have in the module:
print('Earliest  :', datetime.time.min)
print('Latest    :', datetime.time.max)
print('Resolution:', datetime.time.resolution)
 


#DATE
d1 = datetime.date(2015,3,11)
print('d1',d1)

d2 = datetime.date(1998,4,5)

### Arithmatic date
print(d1-d2)

setday = datetime.datetime(3000, 4,23,5,45,8,3)
print(setday)