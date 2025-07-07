
def python_control_flow():
    """
    Demonstrates the use of control flow statements in Python.
    """
    # Conditional statements
    x = int(input("Enter a number: "))
    if x > 0:
        print("x is positive")
    elif x < 0:
        print("x is negative")
    else:
        print("x is zero")
        
    # Looping statements
    arr = [1, 2, 3, 4, 5]
    for i in arr:
        if i%2 == 0:
            print(f"{i} is even")
        else:
            pass
            print(f"{i} is odd")

    # While loop
    count = 0
    while x %2 == 0:
        count += 1  
        break 
    print(count)
    
    
python_control_flow()