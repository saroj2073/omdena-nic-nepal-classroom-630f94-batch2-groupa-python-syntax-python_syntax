import pytest
from assignment import *

def test_format_string():
    assert format_string("John", 25) == "My name is John and I am 25 years old"
    assert format_string("Alice", 30) == "My name is Alice and I am 30 years old"

def test_conditional_check():
    assert conditional_check(15) == "Greater"
    assert conditional_check(5) == "Lesser"
    assert conditional_check(10) == "Equal"

def test_loop_sum():
    assert loop_sum(5) == 15
    assert loop_sum(3) == 6
    assert loop_sum(1) == 1

def test_list_operations():
    assert list_operations([1, 2, 3, 4, 5]) == (15, 5, 1)
    assert list_operations([10, 20, 30]) == (60, 30, 10)

def test_dict_operations():
    students = {
        "John": 85,
        "Alice": 90,
        "Bob": 75,
        "Eve": 95
    }
    result = dict_operations(students)
    assert set(result) == {"John", "Alice", "Eve"}

def test_set_operations():
    assert set_operations([1, 2, 3], [2, 3, 4]) == {2, 3}
    assert set_operations([1, 2], [3, 4]) == set()

def test_arithmetic_ops():
    result = arithmetic_ops(10, 5)
    assert result["sum"] == 15
    assert result["difference"] == 5
    assert result["product"] == 50
    assert result["quotient"] == 2.0

def test_logical_ops():
    result = logical_ops(True, False)
    assert result["and"] == False
    assert result["or"] == True
    assert result["not_x"] == False

def test_bitwise_ops():
    result = bitwise_ops(12, 10)
    assert result["and"] == 8
    assert result["or"] == 14
    assert result["xor"] == 6

def format_string(name, age):
    return(f"My name is {name} and I am {age} years old")

def conditional_check(number):
    if(number<10):
        return("Lesser")
    elif(number>10):
        return("Greater")
    else:
        return("Equal")
    
def loop_sum(n):
    sum=0
    for x in range(1,n+1):
        sum=sum+x
    return(sum)

def list_operations(numbers):
    sum_no=0
    min_no=numbers[0]
    max_no=numbers[0]
    t=tuple()
    for item in numbers:
        sum_no=sum_no+item
        if(min_no>item):
            min_no=item
        if(max_no<item):
            max_no=item
    t=(sum_no,max_no,min_no)
    # t=(sum(numbers),max(numbers),min(numbers))
    return(t)

def dict_operations(students_dict):
    best_students=[]
    for key, value in students_dict.items():
        if(value>=80):
            best_students.append(key)
    return(best_students)

def set_operations(list1, list2):
    return set(list1).intersection(set(list2))

def airthmetic_ops(a,b):
    return {
            "sum": a + b,
            "difference": a - b,
            "product": a * b,
            "quotient": a / b if b != 0 else None
        }
def logical_ops(x, y):
    return{
        "and":x and y,
        "or":x or y,
        "not_x": not(x)
    }
def bitwise_ops(a, b):
    return{
        "and":a & b,
        "or":a | b,
        "xor": a^b
    }




print(format_string("Alice", 30))
print(conditional_check(15))
print(loop_sum(3))
print(list_operations([1, 2, 3, 4, 5]))
students = {
        "John": 85,
        "Alice": 90,
        "Bob": 75,
        "Eve": 95
    }
result = dict_operations(students)
print(result)
listA=[1, 2, 3]
listB=[2, 3, 4]
result=(airthmetic_ops(10,5))
print(result)
result=(logical_ops(True,False))
print(result)
result = bitwise_ops(12, 10)
print(result)




