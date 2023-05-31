def solution(citations):
    answer = 0
    citations.sort()
    
    for i in range(len(citations)):
        over_len=len(citations[i:])
        rest_inyong_count=citations[i]
        
        candidate=min(over_len, rest_inyong_count)
        
        answer=max(answer,candidate)
        
    
    return answer

solution([3, 0, 6, 1, 5])