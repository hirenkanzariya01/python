# # ? if condition
# # username = "admin"

# # if username == "student":
# #     print("You Are student")


# age = int(input("Enter AGE :- "))
# if age >= 100:
#     print("Please Provide Valid AGE ")
# else:
#     if age >= 18 and age <= 40:
#         print("Your Are Young ")
#     elif age >= 41 and age <= 80:
#         print("You Are old")
#     elif age >= 81:
#         print("You Are Very old")
#     else:
#         print("You Are Child")


# for loop
# if condition
# for i in range(0, 5+1):
#     print("for loop", i)


# n = input("enter a number :- ")
# print("User Number:-", int(n))

# for i in range(2, 51, 2):
#     print(i)

# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)

# ? sum of number from 1 to N

# n = 50
# 1275
# 1+2+3+4+5.....+50  =====>>> 15
# total = 0
# for i in range(1, n+1):
#     total = total + i

# print(total)

# list = []
# for i in range(1, n+1):
#   list.append(i)
# print(sum(list))

# find a factorial of a number
# n = 50
# # 1*2*3*4*5 = 120
# factorial = 1
# for i in range(1, n + 1):
#     factorial = factorial * i
# print(factorial)


# ? print a table of any number
# n = 12
# for i in range(1, 11):
#     print(n, 'X', i, '=' ,i*n)

# for i in range(1, 100):
#     if i >= 20 and i <= 30:
#         break
#     print(i)

# ? reverce loop
# for i in range(5, 0, -2):
#     print(i)

number = 987456
# reverse_number = "" #
# for i in str(number):
#     print(i)
#     reverse_number = i + reverse_number
# print(reverse_number)

# str_number = str(number)
# print(len(str_number))
# print("My number ", str_number[5])

# for i in range(len(str_number) - 1, -1, -1):
#     print(str_number[i])

# l = []

# for i in str_number:
#     l.append(i)

# l.reverse()
# print(l)


# number = "123400056789"
# str_numbeer = str(number)
# # print(len(str_numbeer))
# count = 0

# for i in str_numbeer:
#     print(i)
#     count = count + 1

# print(count)

# ?
# my_string = "this is a python aaa code"
# vovels = "aeiouAEIOU"
# vovels_count = 0

# for i in my_string:
#     if i in vovels:
#         vovels_count = vovels_count + 1
# print(vovels_count)


# number = [10, 20, 30, -20, -5, -4, 58, 67, 42, -7,99, -10]
# positive_number = []
# negative_number = []
# for i in number:
#     if i >= 0:
#         positive_number.append(i)
#     else:
#         negative_number.append(i)

# print('Positive number :- ', positive_number)
# print('negative number :- ', negative_number)

# print(max(number))

# number = [10, 20, 30, -20, -5, -4, 58, 67, 42, -7, 99, -10]
# max_number = 0
# for i in number:
#     if i >= max_number:
#         max_number = i
# print(max_number)


# for i in range(9, 0, -1):
#     print((11-i)* ' ',f"{i} " * i)

# for i in range(1, 10):
#     for j in range(1, i):
#         print("x"*j)
#     print()
