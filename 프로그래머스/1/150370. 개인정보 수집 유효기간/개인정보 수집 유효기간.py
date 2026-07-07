def solution(today, terms, privacies):
    answer = []
    dic = {}
    
    for i in range(len(terms)) :
        types, month = terms[i].split(" ")
        dic[types] = int(month)
        
    def convert(date) :
        y, m, d = date.split(".")
        
        return (int(y)*12*28 + int(m)*28 + int(d))
    
    today = convert(today)
    
    for i in range(len(privacies)) :
        date, privacy = privacies[i].split(" ")
        expire = convert(date) + dic[privacy] * 28
        # print(expire, today)
        
        if expire <= today :
            answer.append(i+1)
            
    
    return answer