## 힙 쓰는 법 공부 ... Again ...

import heapq
def solution(book_time):
    
    answer = 0
    arr_min = []
    rooms = []
    
    def change_min(time) :
        h, m = time.split(':')
        return int(h)*60 + int(m)
        
    for i in range(len(book_time)) :
        start= change_min(book_time[i][0])
        end = change_min(book_time[i][1])
        arr_min.append([start,end])
    
    arr_min.sort(key=lambda x: x[0], reverse = False)
    
    ##
    print(arr_min)
    heapq.heappush(rooms, arr_min[0][1]+10)
    
    for start, end in arr_min[1:] :
        if rooms[0] <= start :
            heapq.heappop(rooms)
        heapq.heappush(rooms, end+10)
    
    return len(rooms)
    