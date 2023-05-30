def solution(n):
    dp=[0]*(n+1)
    dp[0]=1 #아무것도 못하는 경우 1(억지인듯)
    dp[1]=1 #한칸만 뛰는 경우 1
    
    if n==1:
        return 1

    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]

    return dp[n]%1234567

print(solution(2000)) 