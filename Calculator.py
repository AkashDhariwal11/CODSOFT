def add(A,B):
    return A+B
def subtract(A,B):
    return A-B
def multiply(A,B):
    return A*B
def div(A,B):
    return A/B
print("Please the select the opertion.")
print("a.Add")
print("b.Subtract")
print("c.Multiply")
print("d.Div")
choice = input("Please enter a choice(a/b/c/d):")
num1 = float(input("Please enter a first number:"))
num2 = float(input("Please enter a second number:"))
if choice=='a':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='b':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=='c':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='d':
    print(num1,"/",num2,"=",div(num1,num2))
else:
    print("This is an invalid input")
   


