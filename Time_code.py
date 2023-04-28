def func_one(n):
   return[str(num) for num in range(n)]
print(func_one(9))
 
def func_two(n):
   return list(map(str,range(n)))
print(func_two(9))

#Timing Start and Stop

import time
#STEP1: get start time
start_time = time.time()
#step2: run your code you want to time
result = func_one(1000000)
#step3: calculate total time elapsed
end_time=time.time() - start_time
print(end_time)

# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = func_two(1000000)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time
print(end_time)

#### TIMEIT MODULE

import timeit

setup='''def func_one(n):
   return[str(num) for num in range(n)]'''


#statement
stmt='func_one(100)'

print(timeit.timeit(stmt,setup,number=100000))

setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''
stmt2 = 'func_two(100)'
print(timeit.timeit(stmt2,setup2,number=100000))

#NOTE: This method is ONLY available in Jupyter and the magic command needs to be at the top of the cell with nothing above it (not even commented code)

#%%timeit
# func_one(100)
# %%timeit
# func_two(100)