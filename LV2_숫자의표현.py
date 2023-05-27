def solution(n):
    answer = 0
    
    #i부터 시작해서 1씩 추가해가며 n까지 검사
    for i in range(1,n+1):
        check=0
        for j in range(i,n+1):
            check+=j
            if check==n:
                answer+=1
                break
            elif check>n:
                break
                
    
    return answer