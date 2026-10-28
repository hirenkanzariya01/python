# ? print even number from 1 to 50
# for a in range(1, 51):
#     if a % 2 == 0:
#       print(a, end='  ')


# ? sum of numbers from 1 to N
# n = 20
# total = 0
# for i in range(1, n + 1):
#     total = total + i
# print(total)


# ? find the factorial of number using loop
# n = 5
# fact = 1
# for i in range(1, n + 1):
#     fact = fact * i

# print(fact)


# ? print a table of any number
# N = 6
# for i in range(1, 11):
#     print(N , "X" , i , "=" , i * N)


# ? loop with break
# for i in range(1, 101):
#     if i == 50:
#         break
#     print(i, end="  ")


# ? reverce a number using loop
# number = 123456
# str_number = str(number)
# rev_number = ''
# for i in str_number:
#   rev_number = i + rev_number

# print(rev_number)


# ? count a digit in a number using loop
# number = 25255125
# digits = 0
# for i in str(number):
#   digits += 1

# print(digits)

# ? count a vovels in a string
# vovels = "aeiouAEIOU"
# name = "hiren kanzariya ai"
# count = 0
# for i in name:
#     if i in vovels:
#         count += 1

# print(count)

# ? print positive number from list
# a = [10, 20, 5, -8, 0, 12, -6, -4, 4, -5]
# for i in a:
#     if i >= 0:
#         print(i)


# ? find the largrst value from list
# a = [10, 20, 50, 15, 35, 84, 12]
# large = 0

# for i in a:
#     if i >= large:
#         large = i

# print(large)


# ? print pattern tryangle

# for i in range(1, 7):
#     print("* " * i)

for i in range(1, 10):
    print(" " * (10 - i), "* " * i)
