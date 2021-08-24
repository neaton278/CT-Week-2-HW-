
# Exersice 1  Basic calculator
'''
num1 = (float(input("Please enter a larger number: ")))
num2 = (float (input("Please enter a smallest number: ")))
computation = input("What operation do you want to calculator perform?(+, -,/,*)")

if computation=="+":
    print(num1+num2)
if computation == "-":
    print(num1-num2)
if computation == "/":
    if num2 != 0:
        print(num1/num2)
    else:
        print("Division by zero is undefined")
if computation =="*":
    print(num2*num1)
'''
# Exersice 2 piramid of x's
rows = int(input("Enter the number of rows: "))
for row in range (0,rows):
    for _ in range(0,rows-row-1):
        print(end=' ')
    for _ in range(0,row+1):
        print('x',end=' ')
    print(' ')