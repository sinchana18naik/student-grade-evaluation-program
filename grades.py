marks=float(input("enter the marks:"))
if marks>=90:
    grade="A"
elif marks>=75:
    grade="B"
elif marks>=55:
    grade="c"
elif marks>=35:
    grade="D"
else:
    grade="fail"

print("result is :",grade)
