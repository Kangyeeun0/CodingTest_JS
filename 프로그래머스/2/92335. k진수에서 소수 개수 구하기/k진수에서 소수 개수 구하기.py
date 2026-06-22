from collections import deque
def solution(n, k):
    answer = 0
    i=0
    change_num = ""
    target = ""
    
    #소수인지 판별하는 함수
    def isPrime(num) :
        if num == 1 :
            return False
        elif num == 2 :
            return True
        else :
            for i in range(2,int(num**(1/2))+1) :
                if num%i == 0:
                    return False
        return True
    
    #진수 변환
    while n >= k :
        change_num += str(n%k)
        n = n//k
        
    change_num+=str(n)
    str_n = change_num[::-1]
        
    
    while i<len(str_n):
        if str_n[i] != "0" :
            target += str_n[i]
            # print(target)
            
        else :
            if len(target) > 0 :
                # print(target)
                if isPrime(int(target)) :
                    answer+=1
                    
            target = ""
        i +=1
    
    if len(target) > 0 :
        if isPrime(int(target)) :
            answer+=1
    
                
        
        
        
        
    return answer