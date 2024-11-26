numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
    for n in numbers:
        if i % n == 1 or i > n:
            primes.append(i)                            # 3 / 1, 3 / 2
            numbers.pop(0)
            continue
        else:
            not_primes.append(i)
            numbers.pop(0)
            break

print('Четные:', primes)
print('Не четные:', not_primes)
