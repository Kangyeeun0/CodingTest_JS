def solution(answers):
    answer = []
    n = len(answers)
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    dic = {1:0,2:0,3:0}
    
    for i in range(len(answers)) :
        if one[i%len(one)] == answers[i] :
            dic[1]+=1
        if two[i%len(two)] == answers[i] :
            dic[2] +=1
        if three[i%len(three)] == answers[i] :
            dic[3] +=1
            
    arr=list(dic.items())
    arr.sort(key = lambda x:x[1], reverse=True)
    max_v=arr[0][1]
    for i in range(len(arr)) :
        if max_v == arr[i][1] :
            answer.append(arr[i][0])
            
    
    
            
    
    
    return answer