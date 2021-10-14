minute = 0
sec = 0

num = int(input('Введите секунды '))

hour = num // 3600
minute = num % 3600 // 60
second = num % 3600 % 60 % 60

# print(hour)
# print(minute)
# print(second)
print(f"{hour:02}:{minute:02}:{second:02}")
