'''A conditional statement evaluates a boolean condition and executes 
   a specific block of code only if that condition is satisfied; otherwise, 
   it executes an alternative block.'''

# Nested Decision Hell
a = int(input("Enter a value:"))
b = int(input("Enter b value:"))
c = int(input("Enter c value:"))
if a < b and b < c:
    print('Strictly Increasing')
elif a > b and b > c:
    print('Strictly Decreasing')
elif b > a and b > c:
    print("Peak")
elif b < a and b < c:
    print("Valley")
else:
    print("Mixed")
  
# Triangle Validity + Type
x = int(input("Enter x side value:"))
y = int(input("Enter y side value:"))
z = int(input("Enter z side value:"))
if x+y <= z or x+z <= y or z+y <= x:
    print("Not a Triangle")
elif x == y == z :
    print("Equilateral")
elif x == y or y == z or x == z :
    print("Isosceles")
else:
    print("Scalene")

# Time Classification
hour = int(input("Enter the hour:"))
if hour >= 0 and hour <= 3:
    print("Late Night") 
elif hour >= 4 and hour <= 7:
    print("Early Morning")
elif hour >= 8 and hour <= 11:
    print("Morning")
elif hour >= 12 and hour <= 15:
    print("Afternoon")
elif hour >= 16 and hour <= 19:
    print("Evening")
elif hour >= 20 and hour <= 23:
    print("Night")
else:
    print("Invalid")

# Admission Shortlisting Logic
marks = int(input("Enter the marks:"))
attendance = int(input("Enter the attendance:"))
sports = input("Enter yes or no:").lower()
if not(0 <= marks <= 100 and 0 <= attendance <= 100):
    print("Invalid input")
elif (marks >= 85 and attendance >= 75) or (marks >= 90 and sports == 'yes'):
    print("Selected")
elif marks >= 70 and attendance >= 60:
    print("Waitlisted")
else:
    print("Rejected")
