# Через list
user_month = int(input(" Введите номер месяца: "))
month = ['Лето', 'Осень', 'Зима', 'Весна']
# print("Вы выбрали: ", user_month[3])
if user_month > 12:
    print("Вы ввели не верное число.")
elif 3 <= user_month <= 5:
    print("Вы выбрали: ", month[3])
elif 6 <= user_month <= 8:
    print("Вы выбрали: ", month[0])
elif 9 <= user_month <= 11:
    print("Вы выбрали: ", month[1])
else:
    print("Вы выбрали: ", month[2])

# Через dict
user_month = int(input(" Введите номер месяца: "))
month = {'month_1': 'Лето', 'month_2': 'Осень', 'month_3': 'Зима', 'month_4': 'Весна'}
if user_month > 12:
    print("Вы ввели не верное число.")
elif 3 <= user_month <= 5:
    print("Вы выбрали: ", month['month_4'])
elif 6 <= user_month <= 8:
    print("Вы выбрали: ", month['month_1'])
elif 9 <= user_month <= 11:
    print("Вы выбрали: ", month['month_2'])
else:
    print("Вы выбрали: ", month['month_3'])
