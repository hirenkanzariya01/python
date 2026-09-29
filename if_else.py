income = int(input("Enter Anual Income :- "))
age = int(input("Enter Age :- "))

if income <= 400000:
    print("Tax FREE")
elif income >= 400001 and income <= 800000:
    tax = income * 5 / 100
    print("5% TAX :- ", tax)

elif income >= 800001 and income <= 1200000:
    tax = income * 10 / 100
    print("10% TAX :- ", tax)

elif income >= 1200001 and income <= 1600000:
    tax = income * 15 / 100
    print("15% TAX :- ", tax)
elif income >= 1600001 and income <= 2000000:
    tax = income * 20 / 100
    print("20% TAX :- ", tax)
elif income >= 2000001:
    tax = income * 30 / 100
    print("30% TAX :- ", tax)

print("---->>", tax)

if age >= 60:
    print("Final TAX is :- ", tax - 50000)

if tax >= 100000:
    extra_tax = tax * 4 / 100
    print(tax + extra_tax)

if income <= 700000:
    print("tax free")
