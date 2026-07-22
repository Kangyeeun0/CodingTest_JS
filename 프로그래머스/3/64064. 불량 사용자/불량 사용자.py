def solution(user_id, banned_id):
    answer = []

    def isSame(user1, user2) :
        if len(user1) == len(user2) :
            for i in range(len(user1)) :
                if user2[i] == '*' :
                    continue
                elif user1[i] == user2[i] :
                    continue
                else :
                    return False
        else :
            return False
        
        return True
    
    
    for i in range(len(banned_id)) :
        arr=[]
        for j in range(len(user_id)) :
            if isSame(user_id[j], banned_id[i]) :
                arr.append(user_id[j])
                
        answer.append(arr)
        
    visited = set()
    result = set()

    def dfs(idx):
        nonlocal visited
        if idx == len(answer):
            result.add(tuple(sorted(visited))) 
            return

        for user in answer[idx]:
            if user not in visited:
                visited.add(user)
                dfs(idx + 1)
                visited.remove(user)
        
                
    dfs(0)
    # print(result)
        
    return len(result)