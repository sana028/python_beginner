
def list_datastructure():
    """
    This function list data structure(Array).
    """
    # Create a list
    data = list(map(int,input("Enter numbers seperated by space: ").split()))
    print("List:", data[0])
    for index, value in enumerate(data):
        print(f"Index {index}: {value}")
    return data

def tuple_datastructure():
    """
    This function list tuple data structure(fixed size and we can convert tuple to list).
    """
    # Create a tuple
    data = tuple(map(int,input("Enter numbers seperated by space: ").split()))
    print("List from tuple:", list(data))
    print("Tuple size:", len(data))
    print("Tuple:", data[0])
    return data

def set_datastructure():
    """
    This function list set data structure(unordered and unique items , convertable to list and tuple).
    """
    # Create a set
    data = set(map(int,input("Enter numbers seperated by space: ").split()))
    tuple_data = tuple(data)
    list_data = list(data)
    print("Tuple from set:", tuple_data)
    print("List from set:", list_data)
    print("Set:", data)
    return data

def dict_datastructure():
    """
    This function list dictionary data structure(if key are duplicated two times the last updated key and value will consider).
    """
    # Create a dictionary
    data = dict()
    n = int(input("Enter number of key-value pairs: "))
    for _ in range(n):
        key, value = input("Enter key and value separated by space: ").split()
        data[key] = int(value)
    
    print("Dictionary:", data)
    return data


list_datastructure()
tuple_datastructure()
set_datastructure()
dict_datastructure()
    