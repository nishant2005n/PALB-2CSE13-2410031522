import math

n = 10
fact = math.factorial(n)

digits = [int(d) for d in str(fact)]
print("Digits of factorial:", digits)