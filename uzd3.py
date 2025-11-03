# Summē skaitļus, kas dalās ar 3un nav lielāki par 100
summa = 0
x = 1
while x <= 100:
    if x % 3 == 0:
        summa += x
    x += 1
print("Summa:", summa)
