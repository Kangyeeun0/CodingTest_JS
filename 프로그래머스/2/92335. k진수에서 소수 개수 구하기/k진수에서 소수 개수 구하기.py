def solution(n, k):
    answer = 0
    k_num = []
    
    #n을 k진수로 변경
    while n>=k :
        r=n%k
        k_num.append(r)
        n//=k
    k_num.append(n)
    k_num=k_num[::-1]
    
    num="".join(map(str,k_num))
    arr=num.split("0")
    arr=[x for x in arr if x!=""]
    print(arr)
    
    for i in range(len(arr)) :
        isPrime = True
        if arr[i] == '2':
            isPrime=True
        elif arr[i] == '1' :
            isPrime = False
        else:
            for j in range(2, int(int(arr[i])**0.5) + 1) :
                if int(arr[i]) % j == 0 :
                    isPrime = False
                    break

        if isPrime :
            answer+=1
    
    return answer