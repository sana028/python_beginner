'''
Exception handle used to handle the run time erros
'''

# wrong input exception
def wrong_input_exception():
    '''
    Raise an exception when the input is not valid
    '''
    try:
     int_input = int(input("Please enter a valid input: "))
     print(f"You entered: {int_input}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        
        
def enter_two_values_to_division():
    '''
    raise an exception when divided with zero
    '''
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        # if b == 0:
        #     raise ZeroDivisionError("Division by zero is not allowed.")
        result = a / b
        print(f"The result of {a} divided by {b} is: {result}")
    except ZeroDivisionError as e:
        print(e)
    except ValueError:
        print("Invalid input! Please enter valid integers.")
    
    
# out of range exception with multiple exceptions
def out_of_range_exception():
    '''
    Raise an exception when the list iteration is out of range
    '''
    try:
        size = int(input("Enter the size of the list: "))
        exce_list = list(map(int, input("Enter numbers separated by space: ").split()))
        for i in range(size):
            print(exce_list[i]/exce_list[i+1])
    except IndexError:
        print("Index out of range! Please check the size of the list.")
    except ValueError:
        print("Invalid input! Please enter valid integers for the list size and elements.")
    except ZeroDivisionError:
        print("Division by zero is not allowed. Please ensure the list does not contain zero.")
        
        
# attribute exception handling
def import_exception_handling():
    '''
     raising exception when the using module is not found
    '''
    try:
        payload = {
            "name":"john",
            "age":25
        }
        res = payload.jsonify()
    except AttributeError as e:
        print(f"Attribute not found: {e}")
    
        
 #custom exception handling
class LoginFailureException(Exception):
    def __init__(self, message):
        super().__init__(message)
    


def validate_login(username, password):
        if username != "admin" or password != "password":
            raise LoginFailureException("Login failed! Invalid username or password.")
        else:
            print("Login successful!")

# super() referes to the parent class of current class, which is inherited from Exception class
def custom_exception_handling():
    '''
    validate the user login data and raise a custom exception if the login fails
    '''
    try:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        validate_login(username, password)
    except LoginFailureException as e:
        print(e)
    
#  super().__init__(f"{message} for user: {username}")

# - This calls the constructor of the **parent class** (`Exception`) using `super()`.
# - It passes a **formatted string** like:
# "Login failed for user: admin"

# - This becomes the **exception message** shown when the error is printed or logged.


  
wrong_input_exception()
enter_two_values_to_division()
out_of_range_exception()
import_exception_handling()
custom_exception_handling()