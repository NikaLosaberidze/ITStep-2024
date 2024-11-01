# N1

# n = int(input("Write an integer: "))


# def fib(n):
#     if n == 0:
#         return 
#     if n == 1:
#         return [0]
#     if n == 2:
#         return [0,1]
#     result = [0,1]
#     for _ in range(n-2):
#         result.append(result[-1] + result[-2])

#     return result


# print(fib(n))



# N2

# str1 = input("Write something: ")
# str2 = input("Write something: ")

# def anagrams(str1,str2):
#     while str1 != "":
#         if str1[0] not in str2:
#             return "These are not anagrams!"
#         str2 = str2.replace(str1[0],"")
#         str1 = str1.replace(str1[0],"")

#     if str1 != "" or str2 != "":
#         return "These are not anagrams!"
    
#     return "These Are Anagrams."

# print(anagrams(str1,str2))



# N3

# n = int(input("Write an integer: "))

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fact(n-1)

# print(fact(n))



# N4

# strr = input("Write something: ")
# charr = input("Write one letter or symbol: ")

# def counter(lst, x):
#     count = 0
#     while x in lst:
#         count += 1
#         lst.remove(x)

#     return count

# print(counter(list(strr),charr))