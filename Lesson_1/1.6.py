a = int(input("Результат первого дня в км: "))
b = int(input("Желаемый результат в км? "))
i = 1
while a < b:
        a = a*1.1
        i += 1
print(f"На {i}-й день спортсмен достиг результата — не менее {b} км.")