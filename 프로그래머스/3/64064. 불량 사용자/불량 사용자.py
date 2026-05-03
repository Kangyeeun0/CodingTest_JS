def solution(user_id, banned_id):
    answer = 0
    ban_list = []
   
    
    
    for i in range(len(banned_id)) :
        id_cnt = 0
        ban_id = banned_id[i]
        arr =[]
        for j in range(len(user_id)) :
            user = user_id[j]
            is_Same = True
            if len(ban_id) != len(user) :
                continue
            else :
                for k in range(len(user)) :
                    if user[k] == ban_id[k] or ban_id[k] == '*' :
                        continue
                    else :
                        is_Same=False
                        break
                if is_Same : 
                    arr.append(user)
        ban_list.append(arr)
        
        
    #DFS로 조합 찾기
    result = set()
    
    def dfs(index ,selected) :
        if index == len(ban_list) :
            #정렬해서 set에 추가(중복 제거)
            result.add(tuple(sorted(selected)))
            return
        
        for user in ban_list[index] :
            if user not in selected :
                dfs(index+1, selected + [user])
    dfs(0,[])
            
    return len(result)