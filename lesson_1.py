#встроенные функции
# abs()
# pow()
# # print()
# input()
#len()
#list()
# s = {"k": 2}
# p =list(s.items())
# print(p)
# tuple()
# int()
# str()
# type()
# dir()



#map(), filter() , reduce()
# def add(x):
#     return x + 7
# lists = [3, 5, 8, 12]
# add_to = list(map(add, lists))
# print(add_to)

# def add(a):
#     if a < 0:
#         a = abs(a)
#     x = 1
#     for i in range(1, a +1):
#         x *=i
#     return x
# lists = [3, -5, 8, -12]
# list_new = list(map(add, lists ))
# print(list_new)

#filter()
# def test (number):
#     if number <= 3:
#         return number
# numbers = [1, 19, 13, 3]
# result = filter(test, numbers)
# print(list(result))


# polindrom = ["anna", "Civic", "almaz", "uluk"]
# def is_polindrom (string):
#     new_str = string[::-1]
#     if string.lower() == new_str.lower():
#         return string
# new_polindrom = list(filter(is_polindrom, polindrom))
# print(new_polindrom)


# from functools import reduce
# def proz(a, b):
#     return a * b
# numbers = [4, 2, 2, 3]
# num = reduce(proz, numbers)
# # print(num)
#
#
# from functools import reduce
# def square (x):
#     return x**2
#
# def is_div(x):
#         if x % 3 == 0 and x % 5 == 0:
#             return x
#
# def summa (x, y):
#     return x+ y
#
#
# l = list(range(1, 101))
# p = list(map(square, l))
# filter_result = list(filter(is_div, p))
# print(filter_result)
# reduce_result = reduce(summa, filter_result)
# print(reduce_result)

def add6(x):
    return x+7
x = add6(4)
print(x)



