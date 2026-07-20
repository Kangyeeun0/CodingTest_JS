def solution(genres, plays):
    answer = []
    genre_dic = {}
    total_dic = {}
    
    for i in range(len(genres)) :
        total_dic[genres[i]] = total_dic.get(genres[i], 0) + plays[i]
        if genres[i] not in genre_dic :
            genre_dic[genres[i]] = []
        genre_dic[genres[i]].append([plays[i], i])
        
    # print(genre_dic, total_dic)
    
    total = sorted(total_dic.items(),key = lambda x:x[1], reverse= True)
    # print(total)
    
    for i in range(len(total)) :
        max_genre = total[i][0]
        genre_list = sorted(genre_dic[max_genre], key = lambda x:x[0], reverse =True)
        
        for j in range(min(2, len(genre_list))) :
            answer.append(genre_list[j][1])
        
            
            
    return answer