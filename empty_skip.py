def fahrenheit(celsius):
    return (9/5)*celsius + 32
    
temps = [0, 22.5, 40, 100]


#map(function,iteral)
F_temps=map(fahrenheit,temps)

#show
print(list(F_temps))

##### LAMBdA
print(list(map(lambda x: (9/5)*x +32, temps)))

a=[1,2,3,4]
b=[2,4,5,7,8]
c=[100,200,300]
print(list(map(lambda x,y: x+y,a,b)))

### reduce(hàm, trình tự) liên tục áp dụng hàm cho trình tự, trả về 1 giá trị duy nhất
#vd: function(function(1,2),3).....

#function ex
from functools import reduce
lst =[47,55,67,88]
print(reduce(lambda x,y: x+y,lst))

#tìm min
min=lambda x,y: y if(x>y) else x
print(reduce(min,lst))