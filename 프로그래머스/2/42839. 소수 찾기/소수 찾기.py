def solution(numbers):
    answer = 0
    arr_num = [n for n in numbers]
    prime = set()
    
    # 소수인지 판별 함수식 하나 필요
    def isPrime(num) :
        result = True
        if num == 0 or num == 1 :
            return False
        if num == 2 or num == 3 :
            return True
        for i in range(2, num//2+1) :
            if num%i == 0 :
                return False
        return True
            
    visited = [False] * len(arr_num)
    #숫자 위치 바꿔서 수 만드는 함수식 필요
    def dfs(n, cnt, prime) :
        num = n
        
        if cnt > 0 :
            # print(num)
            if isPrime(int(num)) :
                prime.add(int(num))
                # print(prime)
        
        
        for i in range(len(arr_num)) :
            if not visited[i] :
                num = n + arr_num[i]
                # print(num)
                visited[i] = True
                dfs(num, cnt+1, prime)
                visited[i] = False
            
    dfs("", 0, prime)
    
    return len(prime)