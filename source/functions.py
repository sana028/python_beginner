
'''
functions are used to reuse the piece of code and it made code more readable.
'''

# function syntax with params
def greet(name):
    print("Hello, " + name)
    
    
# funtion with default parameter
def default_param(len_of_books = 1):
    print("You have " + str(len_of_books) + " book(s) in your library.")
    
# function with return value
def divide_sub_string(s = '') -> str:
    length = len(s)
    if length == 0:
        return s
    else:
        return s[:length // 2]
    
# function with keyword arguments
'''
It makes clear that the function is called with specific parameters.
It is useful when a function has many parameters, and you want to specify only some of them
'''
def print_bill(amount, tax = 0, discount = 0):
    total = amount + tax - discount
    print(f"Total bill is: {total}")
    
    
# function with variable number of arguments
def variable_args(name,*args):
    print(type(args))
    for arg in args:
        print(arg)
        
# function with positional and keyword arguments
'''
Positional arguments are the arguments that are passed to a function in the order they are defined.
Keyword arguments are the arguments that are passed to a function by explicitly specifying the parameter name.
*args it is passed as positional arguments and it is a tuple.
**kwargs it is passed as keyword arguments and it is a dictionary.
'''
def demo(pos1, *args, key1="default", **kwargs):
    print("Positional:", pos1)
    print("Extra positional (*args):", args)
    print("Keyword with default:", key1)
    print("Extra keyword (**kwargs):", kwargs)

demo(10, 20, 30, key1="value", key2="another", key3=100)
    
    
#funciton with variable keyword arguments
def print_details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=25, country="India")
    
'''
lamda is used to create small anonymous functions.
It can take any number of arguments, but can only have one expression.
'''
nums = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even) 





# Example usage of the functions defined above
greet("Alice")
default_param(3)
default_param()  # using default parameter
result = divide_sub_string("Hello, World!")
print("Length of the string divided by 2 is:", result)
print_bill(100, tax=10, discount=5)  # using keyword arguments
print_bill(200)  # using when i user don't have tax on buyed item and no discount
variable_args("helli",("apple", "banana", "cherry"))  # variable number of arguments

