from random import randint
rand_num = randint(20, 241)

for i in range(20, rand_num, 1):
    if i % 20 == 0 or i % 21 == 0:
        print(i)