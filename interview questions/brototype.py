array = [1, 3, 9, 5, 67, 2, 8, 4, 4, 7, 0, 148, 23, 23, 67, 67, 67, 0, 148]
non_prime = []
prime = []
for i in array:
    flag = 0
    if i <= 1:
        flag = 1
    else:
        if i > 2:
            for j in range(2, int(i**0.5+1)):
                if j != i and i % j == 0:
                    flag = 1
                    break
    if flag == 1:
        non_prime.append(i)
for i in array:
    if i not in non_prime:
        prime.append(i)
print("prime numbers are:", prime)
print("non prime numbers are:", non_prime)
small1 = min(prime)
prime.remove(small1)
small2 = min(prime)
prime.append(small1)
if small2 < 7:
    for i in range(len(prime)):
        if prime[i] > 7 and prime.count(prime[i]) > 1:
            for j in range(i + 1, len(prime)):
                if prime[i] == prime[j]:
                    prime[j] = 0
print("prime numbers are:", prime)
print("non prime numbers are:", non_prime)
ans_list = prime + non_prime
print(sum(ans_list))
