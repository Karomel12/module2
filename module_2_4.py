numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    for n in numbers:
        is_prime = True
        if n == i or n == 1:
            if n == 1:
                continue
            continue
        if i % n == 0:
            is_prime = False
            not_primes.append(i)
            break
    else:
        if is_prime:
            primes.append(i)
        else:
            not_primes.append(i)
print('Четные:', primes)
print('Не четные:', not_primes)