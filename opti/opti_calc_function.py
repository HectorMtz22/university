from fractions import Fraction 
n = int(input("Enter number of variables: "))
coefficients = 0
var = 0 
value = 0
for i in range(n):
    coefficients = Fraction(input(f"Enter coefficient {i}: "))
    var = Fraction(input("Enter value of variable"))
    value += (coefficients * var)

print("The value is:", value)