#음악 제목, 재생 시작되고 끝난 시각, 악보
#조건 일치하는 곡이 여러 개면 라디오에서 재생된 시간이 제일 긴 음악 반환
def solution(m, musicinfos):
    answer = ''
    m = list(m)
    arr = []
    
    def changeMin(time) :
        hour, minute = time.split(":")
        
        return int(hour) * 60 + int(minute)
    
    def changeShop(melodie) :
        m_arr =[]
        for i in range(len(melodie)) :
            if melodie[i] == '#' :
                m_arr[-1] = m_arr[-1].lower()
            else :
                m_arr.append(melodie[i])    
        
        
        return "".join(m_arr)
    

    m = changeShop(m)
    i=1
    for musicinfo in musicinfos :
        start, end, name, melodie = musicinfo.split(",")
        total_time = changeMin(end)-changeMin(start)
        # print(total_time)
        melodie=list(melodie)

        melodie = changeShop(melodie)
        
        if len(melodie) > total_time :
            melodie = melodie[0:total_time]
        else :
            melodie = melodie*(total_time//len(melodie)+1)
            melodie = melodie[0:total_time]
        
        if m in melodie :
            arr.append([melodie,i, name])
        i+=1
    
    arr.sort(key = lambda x:(-len(x[0]), x[1]))
    
    if arr :
        return arr[0][2]
            
            
            
        
    return "(None)"