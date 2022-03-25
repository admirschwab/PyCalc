number1 = int(input("Zahl 1: "))
arithmeticSign = input("Rechenzeichen: ")
number2 = int(input("Zahl 2: "))

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