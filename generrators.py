# def gencubes(n):
#     lt = []
#     for num in range(n):
#         lt.append(num**3)
#     return lt
# print(gencubes(10))

def gencubes(n):
    for num in range(n):
        yield num**3
print(list(gencubes(10)))
# for x in gencubes(10):
#     print(x)

def genfibon(n):
    # generate a fibonnaci sequence up to n
    a=1
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b
for num in genfibon(10):
    print(num)
######
def fibon(n):
    a = 1
    b = 1
    output = []
    
    for i in range(n):
        output.append(a)
        a,b = b,a+b
        
    return output
fibon(10)

############## NEXT(), ITER()
def simple_gen():
    for x in range(2):
        yield x
# g = simple_gen()
# print(next(g))
# print(next(g))
# print(next(g))

###
s ='hello'
for let in s:
    print(let)
    
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))

####HOME WORK 
#problem 1
def gensquare(N):
    for num in range(N):
        yield num**2
for x in gensquare(10):
    print(x)

#problem 2

import random
print(random.randint(1,10))
def rand_num(low,high,n):
    for num in range(n):
        yield random.randint(low,high)
for num in rand_num(1,10,12):
    print(num)

##problem 3
s= 'helo'
# for let in s:
#     print(let)
s_iter =iter(s)
print(next(s_iter))
#problem 4
#If the output has the potential of taking up a large amount of memory and you only intend to iterate through it, you would want to use a generator. (Multiple answers are acceptable here!)
#Câu lệnh năng suất tạm dừng việc thực thi của một hàm và gửi lại một giá trị cho người gọi, nhưng vẫn giữ đủ trạng thái để cho phép hàm tiếp tục ở nơi nó đã dừng lại. Khi chức năng tiếp tục, nó tiếp tục thực hiện ngay sau lần chạy năng suất cuối cùng. Điều này cho phép mã của nó tạo ra một loạt giá trị theo thời gian, thay vì tính toán chúng cùng một lúc và gửi lại chúng như một danh sách.

### EXTRA CREDIT
##Google generator comprehension
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item <3)

for item in gencomp:
    print(item)
