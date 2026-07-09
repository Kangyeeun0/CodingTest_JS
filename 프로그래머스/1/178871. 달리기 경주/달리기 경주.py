def solution(players, callings):
    answer = []
    name = {}
    rank = {}
    
    for i in range(len(players)) :
        name[players[i]] = i+1
        rank[i+1] = players[i]
    
    
    for call_name in callings :
        cur_rank = name[call_name]
        front_person = rank[cur_rank - 1]
        rank[cur_rank], rank[cur_rank -1] = rank[cur_rank -1], rank[cur_rank]
        name[call_name], name[front_person] = name[front_person], name[call_name]
        
    # print(rank, name)   
    
    for [key, item] in rank.items() :
        answer.append(item)
        
        
        
    return answer