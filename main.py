number1 = int(input("Number 1: "))
arithmeticSign = input("Arithmetic Sign: ")
number2 = int(input("Number 2: "))

Result = 0

if arithmeticSign == "+":
    Result = number1+number2

if arithmeticSign == "-":
    Result = number1-number2

if arithmeticSign == "*":
    Result = number1*number2

if arithmeticSign == "/":
    Result = number1/number2

print(Result)