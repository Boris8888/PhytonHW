my_list = [7, 5, 3, 3, 2]
len_str = len(my_list)
i = 0
user_num = int(input("Введите число: "))
while True:
    if user_num > my_list[0]:
        my_list.insert(0, user_num)
        print(my_list)
        break
    elif user_num < my_list[len_str - 1]:
        my_list.append(user_num)
        print(my_list)
        break
    elif user_num == my_list[i]:
        my_list.insert(i + 1, user_num)
        print(my_list)
        break
    else:
        i += 1