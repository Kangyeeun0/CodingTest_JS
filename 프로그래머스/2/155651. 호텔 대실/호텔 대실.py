import heapq
def solution(book_time):
    answer = 0
    arr = []
    
    def changeTime(time) :
        hour, minute = time.split(":")
        return int(hour) * 60 + int(minute)
    
    for book in book_time :
        start, end = book
        start_min = changeTime(start)
        end_min = changeTime(end)
        arr.append([start_min,end_min])
        
    arr.sort(key = lambda x:x[0])
    room = []
    heapq.heapify(room)
    
    for i in range(len(arr)) :
        
#         if not room :
#             # room.append(arr[i][1])
#             answer+=1
        
        if not room or room[0] + 10  > arr[i][0] :
            answer+=1

        else :
            heapq.heappop(room)
        heapq.heappush(room, arr[i][1])
            
        
        
        
        
    return answer