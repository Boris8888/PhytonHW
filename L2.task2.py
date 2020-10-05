my_list = list(input('Ввод:'))  # Вводим список
num_el = int(len(my_list))  # Считаем количество символов
i = num_el-1
# Проверяем четность
a = num_el % 2
# Если не четное количество индексов, то последний не изменяем
if a > 0:
    i -= 1

while i >= 0:
    b = my_list.pop(i)
    my_list.insert(i-1, b)
    i -= 2
print(my_list)
