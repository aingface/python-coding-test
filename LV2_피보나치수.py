def solution(n):
    #재귀를하면 계산 했던거 또해야하니깐 쓰지 않고 DP로 간다!
    answer = [0]*(n+1)
    answer[1]=1
    
    for i in range(2,n+1):
        answer[i]=answer[i-1]+answer[i-2]
    
  
    return answer[n]%1234567