import math

def solution(fees, records):
    answer = []
    
    tmp_dict = {}
    parking_dict = {}
    
    for record in records:
        time, car, in_out = record.split()
        if in_out == "IN":
            tmp_dict[car] = time
        elif in_out == "OUT":
            park_time = int(time.split(":")[0]) - int(tmp_dict[car].split(":")[0])
            park_time *= 60
            park_time += int(time.split(":")[-1]) - int(tmp_dict[car].split(":")[-1])
            if car in parking_dict.keys():
                parking_dict[car] += park_time
            else:
                parking_dict[car] = park_time
                
            del tmp_dict[car]
    
    for car in tmp_dict.keys():
        park_time = 23 - int(tmp_dict[car].split(":")[0])
        park_time *= 60
        park_time += 59 - int(tmp_dict[car].split(":")[-1])
        if car in parking_dict.keys():
            parking_dict[car] += park_time
        else:
            parking_dict[car] = park_time
            
    car_order = sorted(list(parking_dict.keys()))
    
    for car in car_order:
        park_time = parking_dict[car]
        if park_time < fees[0]:
            answer.append(fees[1])
        else:
            tmp = fees[1]
            park_time -= fees[0]
            tmp += math.ceil(park_time / fees[2]) * fees[3]
            answer.append(tmp)
    
    return answer