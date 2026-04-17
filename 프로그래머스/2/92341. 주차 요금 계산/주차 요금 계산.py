import math

def solution(fees, records):
    answer= []
    # fees = [기본시간, 기본요금, 단위시간, 단위요금]
    basic_time, basic_fee, unit_time, unit_fee = fees
    
    # 1. 차량별 입출차 시간 저장
    parking_times = dict()
    
    for record in records:
        time, car_number, in_out = record.split(" ")
        h, m = time.split(":")
        min_time = int(h) * 60 + int(m)
        
        if car_number not in parking_times:
            parking_times[car_number] = []
        
        parking_times[car_number].append(min_time)
    
    # 2. 차량별 총 주차 시간 계산
    total_times = dict()
    
    for car_number, times in parking_times.items():
        # 출차 기록이 없으면 23:59 추가
        if len(times) % 2 == 1:
            times.append(23*60+59)
            
        total = 0
        for i in range(0, len(times), 2) :
            total += times[i+1]- times[i]
            
        if car_number not in total_times :
            total_times[car_number] = []
            
        total_times[car_number].append(total)

    sorted_cars = sorted(total_times.keys())
    
    
    for car_number in sorted_cars :
        t = total_times[car_number][0]
        total_fee =0
        if t <= basic_time :
            total_fee = basic_fee
        else :
            total_fee = basic_fee + unit_fee*(math.ceil((t-basic_time)/unit_time))
        answer.append(total_fee)
    
    return answer