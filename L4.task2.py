from random import randint

mi_list =[10, 20, 30, 40, 50, 40, 30, 20, 10]
new_list = []
new_list_1 = []
for i in mi_list:
    rand_num = randint(0, 100)
    new_list.append(rand_num)
print("Исходный список", new_list)
for i in range(0, len(new_list), 1):
        if new_list[i] > new_list[i - 1]:
            new_list_1.append(new_list[i])
print("Результат",new_list_1)
