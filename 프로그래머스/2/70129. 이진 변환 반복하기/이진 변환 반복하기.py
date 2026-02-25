def solution(s):
    answer = []
    changeNum = 0
    total = 0
    
    
    while s!= "1" :
        st=""
        num=s.count("1")
        changeNum += (len(s) - num)
        total+=1
        
        s = bin(num)[2:]
        
    return [total, changeNum]