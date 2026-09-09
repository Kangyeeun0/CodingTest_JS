def isPrime(num) :
        
    if num==0 or num == 1:
        return False
    elif num == 2 :
        return True
    for i in range(2, int(num**(1/2))+1) :
        if num%i == 0 :
            return False
    return True

def solution(numbers):
    answer = []
    arr = []
    for n in numbers :
        arr.append(n)
    visited = [False] * len(arr)
    print(arr)
    
    def dfs(num) :
        nonlocal answer
        
        if isPrime(int(num)) and int(num) not in answer:
            answer.append(int(num))
            
        if len(num) == len(arr) : 
            return
        
        for i in range(len(arr)) :
            if not visited[i] :
                visited[i] = True
                dfs(num+arr[i])
                visited[i] = False
        return
                
    for i in range(len(arr)) :
        visited[i]=True
        dfs(arr[i])
        visited[i]=False
                
    
    


    
    return len(answer)