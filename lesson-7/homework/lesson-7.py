#1
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if(n % i) == 0:
            return False
    return True

print(is_prime(4))
print(is_prime(7))

#2
def digit_sum(k):
    sum = 0
    for i in str(k):
        sum+=int(i)
    return sum

print(digit_sum(129))

#3
def is_power_print(n):
    k = 1
    while 2 ** k < n:
        print(2 ** k)
        k = k +1

print(is_power_print(10))
