# data = {
#     "user_name": "abcd",
#     "password": "123456",
#     "email": "abcd@gmail.com",
#     "mobile_number": 1234567890,
#     "Products": ["Mobile", "Watch", "Leptop"],
# }

# # data["user_name"] = "hiren kanzariya"
# # data["Education"] = "MSC IT"

# data.pop('password')
# print(data)


data = [
    {"name": "raju", "id": "002", "std": 12, "marks": 75},
    {"name": "vivek", "id": "003", "std": 12, "marks": 78},
    {"name": "rahul", "id": "001", "std": 12, "marks": 85},
    {"name": "raj", "id": "004", "std": 12, "marks": 74},
    {"name": "raj", "id": "004", "std": 12, "marks": 89},
    {"name": "raj", "id": "004", "std": 12, "marks": 90},
]

for i in data[:]:
    if i["marks"] > 80:
        pass
    else:
        data.remove(i)
print(data)

