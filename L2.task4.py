user_str = input("Введите предложение: ")
print(user_str)
user_str = user_str.split()
len_str = len(user_str)
i = 0
line = 1
while i < len_str:
    if len(user_str[i]) > 10:
        print(line, user_str[i][:10])
    else:
        print(line, user_str[i])
    i += 1
    line +=1

#print(user_str)