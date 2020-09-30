revenue = int (input("Введите выручку: "))
cost = int(input("Введите издержки: "))
profit = revenue - cost  #Прибыль
if profit >= 0:
    if profit > 0:
        print(f"Прибыль составила: {profit}")
        print(f"Рентабельность: {profit / revenue}")
        staff = int(input("Ведите численность человек: "))
        print("Прибыль на одного человека персонала:", (profit / staff))
    elif profit == 0:
        print("Прибыль: 0")
else:
    print(f"Убыток: {profit}")