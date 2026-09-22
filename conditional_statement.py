marks = int(input("Enter Total Marks :- "))


if marks >= 90 and marks <= 100:
    print("Gread A")
elif marks >= 80 and marks < 90:
    print("Gread B")
elif marks >= 60 and marks < 80:
    print("Gread C")
elif marks >= 40 and marks < 60:
    print("Gread D")
elif marks >= 33 and marks < 40:
    print("Gread E")
elif marks < 33:
    print("Fail")
else:
    print("Please Provide Valid Marks ")
