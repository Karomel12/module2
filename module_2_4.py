numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
    for n in numbers:
        if i % n == 0 and i > n:
            primes.append(i)                            # 3 / 1, 3 / 2
            continue
        else:
            not_primes.append(i)
            break
    numbers.pop(0)

print('Четные:', primes)
print('Не четные:', not_primes)