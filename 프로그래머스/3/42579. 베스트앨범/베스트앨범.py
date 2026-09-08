def solution(genres, plays):
    answer = []
    album = {}
    arr = []
    
    for i in range(len(genres)) :
        if genres[i] not in album :
            album[genres[i]] = [0, []]
        album[genres[i]][0] += plays[i]
        album[genres[i]][1].append([plays[i], i])
    
    
    for key, value in album.items() :
        arr.append([key, value])
     
    arr.sort(key = lambda x:(-x[1][0]))
    
    for j in range(len(arr)) :
        play = sorted(arr[j][1][1], key = lambda x:(-x[0],x[1]))
        # print(play)
        if len(play) < 2 :
            for k in range(len(play)) :
                answer.append(play[k][1])
        else :
            for k in range(2) :
                answer.append(play[k][1])
        
        

        
    return answer