from itertools import combinations

BUSs=[8,6,7,4,1,3,2,5]

def recur(start,BUS,cycle,visited):  
    next_BUS=BUSs[BUS-1]
    visited[BUS]=True

    if len(cycle)==0:
        cycle.append(start)
    
    cycle.append(BUS)

    if start==next_BUS:
        return set(cycle)


    return recur(start,next_BUS,cycle,visited)


def solution(BUSs):

    answer=0
    visited=[False]*(len(BUSs)+1)

    for i in range(1,len(BUSs)+1):
        if visited[i] == False:
            visited[i]=True
            next_BUS=BUSs[i-1]
            sub_cycle=recur(i,next_BUS,[],visited)
            case=len(list(combinations(sub_cycle,2)))
            answer+=case

    return answer


s=solution(BUSs)
print(s)
