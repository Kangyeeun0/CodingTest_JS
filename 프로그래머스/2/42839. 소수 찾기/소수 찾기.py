from itertools import permutations

def solution(numbers):
    answer = 0
    primes=[]
    digits = str(numbers)
    result = set()
    
    
    def isPrime(n) :
        for i in range(2, int(n**0.5)+1) :
            if n%i == 0 :
                return False
        return True
    
    for length in range(1, len(digits) + 1) :
        #length가 개수
        for perm in permutations(digits, length) :
            num = int(''.join(perm))
            result.add(num)
    results = list(result)
    
    for j in range(len(results)) :
        if results[j] <=1 :
            continue
        elif isPrime(results[j]) :
            primes.append(results[j])
        
    return len(primes)