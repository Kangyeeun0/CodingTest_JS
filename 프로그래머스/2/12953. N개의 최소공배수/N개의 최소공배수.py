def solution(arr):
    answer=arr[0]
    
    def gcd(a, b) :
        while(b!=0) :
            temp = b
            b = a%b
            a = temp
        return a
    
    for i in range(1, len(arr)) :
        b = arr[i]
        
        answer*=b/gcd(b,answer)
    
    return answer