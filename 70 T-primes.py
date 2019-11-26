n = int(input())
nums = [int(i) for i in input().split()]

def prime_list(n):
    '''use sieve method to create a boolean list, so that order of growth is O(1)'''
    prime_bool = [True for i in range(n+1)]
    prime_bool[0], prime_bool[1] = False, False
    i = 2
    while i ** 2 <= n:
        if prime_bool[i]:
            for j in range(2*i, n, i):
                prime_bool[j] = False  # sieve!
        i += 1
    return prime_bool

prime_bool_list = prime_list(10**6+1)
for num in nums:
    if num ** 0.5 == int(num**0.5) and prime_bool_list[int(num**0.5)]:
        print('YES')
    else:
        print('NO')

# not useful
def all_primes(n): 
    '''create a list of all primes <= N'''
    is_existing = [True for i in range(n+1)]
    num, primes = 2, []
    while num ** 2 <= n:
        if is_existing[num]:
            primes.append(num)
            for i in range(num**2, n+1, num):
                is_existing[i] = False  # sieve!
        num += 1
    return primes

def is_prime(n):
    if n <= 1 or int(n) != n:
        return False
    else:
        i = 2
        while i ** 2 <= n:
            if n % i == 0:
                return False
            i += 1
        return True