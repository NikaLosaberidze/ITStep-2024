import functools

# N1

def func1(lst1,lst2):
    return list(zip(lst1,lst2))


# N2

def func2(lst):
    try:
        for i in lst:
            if type(i) is not int:
                raise TypeError
            
        return functools.reduce(lambda x,y:x*y,lst)
    
    except TypeError:
        print("Argument must be list of numbers!")


# N3

numbers = [1,2,3,4,5,6,7]
odds = list(filter(lambda x: x%2 == 1, numbers))

# print(odds)


# N4

def func4(lst,strr):
    try:
        return list(filter(lambda x:x.endswith(strr),[x for x in lst] ))
    except (AttributeError,TypeError):
        print("First Argument Must Be List Of Strings, Second Argument Must Be A String")


# print(func4(['hello', 'world', 'coding', 'nod','ing'],'ing'))
