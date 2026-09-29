# first_name = "rahul"
# middle_name = " k"
# last_name = " patel \n "
# fullname = first_name + middle_name + last_name
# # print(type(fullname))
# print(first_name[0:3])


# data = "\n is use for break a line "
# print("0" not in data)
# print(data)

# val1 = 'py'
# val2 = 'javascript'

# print('py ' ,  val2)


my_string = "This Is An Apple"

# ? len()
# my_str_len = len(my_string)

# ? lower() & upper()
# lower_str = my_string.upper()
# print(lower_str)

# ? replace()
# new_str = my_string.replace("Apple", "banana")
# print(new_str)

# ? join()
# str1 = 'apple'
# str2 = 'banana'
# print(str1.join(str2))

# ? split()
# my_string = "This Is An Apple banana mango"
# print(len(my_string.split(' ')))

# ? find()
# print(my_string.find('Apple'))
# print(my_string)
# print(my_string.replace(' ', ''))


# ? isalnum()
# password = "abcd123"
# print(password.isalnum())


# ? isdigits
# number = '789456123'
# print(number.isdigit())

# ? isnumaric
# number = "\u2163"
# print(number)

# ? islower()
# print(s.islower())


# ? Reverce a string
# s = "this is string"
# for i in range(13, -1, -1):
#     print(s[i])


# ? cheack strcontain only digits ?
# s = "56789"
# if s.isdigit():
#     print("String contain only digits")
# else:
#     print("No String not contain digits ")


# ? cheack str is palindrome or not
# s = input("Enter String to cheack palindrome or not :-")
# rev = ""

# for i in range(len(s) - 1, -1, -1):
#     rev = rev + s[i]

# if s == rev:
#     print(s, "==", rev)
#     print("String is palindrome")
# else:
#     print(s, "!=", rev)
#     print("string is not palindrome ")


# ? count vovels and consonants
# str = "this is a vovels counter "
# str = str.replace(" ", "")
# vovels = "AEIOUaeiou"
# vovels_count = 0
# consonants_count = 0

# for i in str:
#     if i in vovels:
#         vovels_count = vovels_count + 1
#     else:
#         consonants_count = consonants_count + 1

# print("Total Vovels:- ", vovels_count)
# print("Total Consonants :- ", consonants_count)


# ? string to list
# str = "this is a string"
# str = str.replace(" ", "")
# # print(str.split(" "))
# l = []
# for i in str:
#     l.append(i)
# print(l)


# ? replace space with specific charactor 
# str = "this is a string"
# print(str.replace(' ', ' # '))