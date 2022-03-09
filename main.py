zahl1 = int(input("Zahl 1: "))
Rechenzeichen = input("Rechenzeichen: ")
zahl2 = int(input("Zahl 2: "))

Ergebnis = 0

if Rechenzeichen == "+":
    Ergebnis = zahl1+zahl2

if Rechenzeichen == "-":
    Ergebnis = zahl1-zahl2

if Rechenzeichen == "*":
    Ergebnis = zahl1*zahl2

if Rechenzeichen == "/":
    Ergebnis = zahl1/zahl2

print(Ergebnis)