num = input('Введите целое положительное число ')

i =0
max_num = 0

while i < len(num):
    temp = int(num[i])
    if temp > max_num:
        max_num = temp
    i += 1

print('Самая большая цифра ', max_num)
