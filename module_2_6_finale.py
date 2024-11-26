import random


def get_r_number():
    numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    r_number = random.choice(numbers)
    return r_number

def get_passcode(n):
    passnum = {}
    passnum.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645})
    passnum.update({10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867})
    passnum.update({14: 1611325212343114105968, 15: 1214114232133124115106978})
    passnum.update({16: 1317115262143531341251161079, 17: 11621531441351261171089})
    passnum.update({18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910})
    passnum.update({20: 13141911923282183731746416515614713812911})
    passcode = passnum.get(n)
    return passcode

n = get_r_number() #15
num1 = list(range(1,n))
num2 = list(range(1,n))
pairs = []
result = ''

for i in num1:
    for j in num2:
        n1 = i
        n2 = j
        if n1 >= n2:
            continue
        else:
            if n % (n1 + n2) == 0:
                pairs.append([n1,n2])
                result = result + str(n1) + str(n2)

print('Введите :', result, 'во вторую вставку')
result = input('Ввести сюда: ')
if int(result) == get_passcode(n):
    print('Путь открыт')
else:
    print('Вы неправильно ввели пароль, проигрыш')

