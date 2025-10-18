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

sub1=float(input("enter marks of 1st subject:"))


sub2=float(input("enter marks of 2nd subject:"))


sub3=float(input("enter marks of 3st subject:"))


sub4=float(input("enter marks of 4st subject:"))


sub5=float(input("enter marks of 5st subject:"))
avg=(sub1+sub2+sub3+sub4+sub5)/5
print("average of marks is :",avg)

print("result is :",grade)
