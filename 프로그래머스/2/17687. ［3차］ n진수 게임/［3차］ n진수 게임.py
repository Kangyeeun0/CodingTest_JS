def solution(n, t, m, p):
    answer = ''
    text = ''
    turn = 1
    
    def changeNum(num, k) :
        total = ""
        arr = ['A','B','C','D','E','F']
        while num >= k :
            r = num % k
            num= num//k
            if r >=10 :
                r = arr[r-10]
            total+=str(r)
        if num >=10 and k>10 :
                num = arr[num-10]
        total +=str(num)
        
        return total[::-1]
        
    # print(changeNum(15,16))
    for i in range(t*m) :
        num = changeNum(i, n)
        text+=num
    # print(text)    
    j=0
    while len(answer) < t : 
        if turn == p :
            answer+=text[j]
        if turn < m :
            turn+=1
        else :
            turn = 1
        j+=1
        
    return answer