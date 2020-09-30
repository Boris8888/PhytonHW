us_num = 56238  # число для анализа
max_num = 0
while us_num > 0:
    rem_num = us_num // 10  # переход к следующей цифре
    rem_div_one = us_num % 10  # остаток первого деления
    rem_div_two = rem_num % 10  # остаток второго деления
    if rem_div_one > rem_div_two & rem_div_two != 0:
        us_num = rem_num
        if rem_div_one > max_num:
            max_num = rem_div_one
        else:
            max_num = max_num
    elif rem_div_one > max_num:
        max_num = rem_div_one
    else:
        max_num = max_num
        us_num = rem_num
print(max_num)

