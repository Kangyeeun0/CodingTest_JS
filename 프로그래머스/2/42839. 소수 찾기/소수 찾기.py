def solution(numbers):
    answer = 0
    number_arr = [k for k in numbers]
    visited = [False] * len(number_arr)
    prime_set = set()
    
    def isPrime(num) :
        if num == 0 or num == 1 :
            return False
        elif num == 2 or num == 3 :
            return True 
        else :
            for i in range(2, num//2+1) :
                if num % i == 0 :
                    return False
        return True
        
    
    def generateNum(num) :
        nonlocal answer
        
        if isPrime(int(num)) and int(num) not in prime_set :
            answer+=1
            prime_set.add(int(num))
        
        
        for i in range(len(number_arr)) :
            if not visited[i] :
                visited[i] = True
                generateNum(num+number_arr[i])
                visited[i] = False
                

    for i in range(len(number_arr)) :
        if not visited[i] :
            visited[i] = True
            generateNum(number_arr[i])
            visited[i] = False            
            
   

    return answer