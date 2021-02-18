"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        prime = [True for i in range(n + 1)]
        p = 2
        count = 0
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * 2, n + 1, p):
                    prime[i] = False

            p += 1
        prime[0] = False
        prime[1] = False
        for p in range(2, n + 1):
            if prime[p]:
                count += 1
                print(p)
        #return sum(prime)
        return count

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for j in range(i * i, n, i):
            primes[j] = False
        return sum(primes)


"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)


print(Solution.countPrimes(self=Solution,n=3))

