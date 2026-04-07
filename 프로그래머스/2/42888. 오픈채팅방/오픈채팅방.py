def solution(record):
    answer = []
    dic = dict()
    arr=[]
    
    for i in range(len(record)) :
        a = record[i].split(" ")
        # print(a)
        arr.append([a[0], a[1]])
        if a[0] != "Leave":
            dic[a[1]] = a[2]
        # print(dic)
    
    # print(arr)
    
    for j in range(len(arr)) :
        text, Id = arr[j]
        name = dic[Id]
        if text == 'Enter' :
            answer.append(name + "님이 들어왔습니다.")
        elif text == 'Leave' :
            answer.append(name + "님이 나갔습니다.")

    return answer