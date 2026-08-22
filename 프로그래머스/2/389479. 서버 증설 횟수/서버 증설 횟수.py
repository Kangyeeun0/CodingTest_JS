from collections import deque
def solution(players, m, k):
    answer = 0
    players = deque(players)
    total_server = 0
    server = deque()
    # j=0

    
    while players :
        player = players.popleft()
        # 존재하는 서버들의 시간 -1
        for i in range(len(server)) :
            server[i] -= 1
        while server and server[0] == 0 :
            server.popleft()
            total_server -=1
        
        if player >= m :
            # 필요한 총 서버 개수
            server_cnt = player // m
            
            
            
            # 이미 있는 서버 개수가 필요한 서버 개수보다 많으면 새로 만들기
            if total_server < server_cnt :
                need_cnt = server_cnt-total_server
                total_server += need_cnt
                answer += need_cnt
                # print(j, need_cnt)
                for i in range(need_cnt) :
                    server.append(k)
            
        
        # print(j, total_server)    
        # j+=1
        
            
            
            
    
    return answer