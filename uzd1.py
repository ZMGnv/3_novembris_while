# Sasummē ievadītos skaitļus. 0 norāda, ka darbs jābeidz.
summa = 0
x = int(input("Ievadi skaitli (0 lai beigtu): "))
while x != 0:
    summa += x
    x = int(input("Ievadi skaitli (0 lai beigtu): "))
print("Summa:", summa)