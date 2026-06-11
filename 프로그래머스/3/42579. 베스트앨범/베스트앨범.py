def solution(genres, plays):
    answer = []
    dic = dict()
    # dic_set = dict()
    
    for i in range(len(genres)):
        dic.setdefault(genres[i], []).append([i, plays[i]])
        
    sorted_dic = sorted(dic.items(), key= lambda x: sum(play for _, play in x[1]),  reverse=True)
    # print(sorted_dic)
    
    for i in range(len(sorted_dic)) :
        one_set = sorted(sorted_dic[i][1], key= lambda x: (-x[1], x[0]))
        # print(one_set)
        for j in range(min(2, len(one_set))) :
            answer.append(one_set[j][0])
            

    return answer