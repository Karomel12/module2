first = int(input("Первое число: "))
second = int(input("Второе число: "))
third = int(input("Третее число: "))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)