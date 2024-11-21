first = int(input("Первое число: "))
second = int(input("Второе число: "))
third = int(input("Третее число: "))
if first == second == third:
    print('Числа равны:',3)
elif first == second or first == third or second == third:
    print('Только 2 числа равны:',2)
else:
    print('Никакие из чисел не равны:',0)