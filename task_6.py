dist = int(input("Дистанция за первый день: "))
standard = int(input("Обший результат не менее: "))
num_days = 1  # день
print(num_days, "-й день: ", dist)
while dist <= standard:
    num_days += 1
    dist = dist + (dist * 0.1)
    print(num_days, f"-й день: {dist:.2f}")
print(" Ответ, на ", num_days, f"-й день: {dist:.2f}")
