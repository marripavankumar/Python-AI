marks = input("enter your marks: ")
marks = int(marks)  

if marks >= 90:
    print("You got A grade")
elif marks >= 80 and marks < 90:
    print("You got B grade")
elif marks >= 70 and marks < 80:
    print("You got C grade")
elif marks >= 60 and marks < 70:
    print("You got D grade")
else :
    print("You got F grade")
       