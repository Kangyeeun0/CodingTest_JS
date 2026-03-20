def solution(arrayA, arrayB):
    answer = 0
    
    def gcd(a,b) :
        while b!=0 :
            r = a%b
            a=b
            b=r
        return a
    
    gcdValueA = arrayA[0]
    gcdValueB = arrayB[0]

    for i in range(1, len(arrayA)):
        gcdValueA = gcd(gcdValueA, arrayA[i])
        gcdValueB =gcd(gcdValueB, arrayB[i])
    
    
    for c in arrayB :
        if c % gcdValueA == 0 :
            gcdValueA = 0
            break
    for d in arrayA :
        if d % gcdValueB == 0 :
            gcdValueB = 0
            break
        
    return max(gcdValueA, gcdValueB)