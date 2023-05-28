from collections import deque

def solution(people, limit):
    answer = 0
     #가장 무거운 사람 + 가장 가벼운 사람  
     #안되면 가장 무거운 사람 + 다음으로 가벼운 사람.. 

    people.sort()
    deque_people=deque(people)

    boat_limit=0
    boat_limit+=deque_people.pop()    
    
    while deque_people:
        if boat_limit+deque_people[0]>limit:
            answer+=1
            boat_limit=0
            boat_limit+=deque_people.pop()
       
        else:
            most_light_person=deque_people.popleft()
            boat_limit+=most_light_person


    if boat_limit>0 and not deque_people:
        answer+=1

    return answer

print(solution([70, 80, 50], 100))

"""
    투포인터를 활용한 방법
    가장무거운 사람+ 가장 가벼운사람 검사, limit 미만이면 += 그다음 가벼운사람.. 

  def solution(people, limit) :
    save_boat_count = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            save_boat_count += 1
        b -= 1
    return len(people) - save_boat_count
"""      