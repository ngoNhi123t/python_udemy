def func():
    return 1
s = 'Global Variable'

def check_for_locals():
    print(locals())
print(globals())
print(globals().keys())
globals()['s']
check_for_locals()

def hello(name='Jose'):
    print('The hello() function has been executed')
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"
    
    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function")
hello()

####
def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")
func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()