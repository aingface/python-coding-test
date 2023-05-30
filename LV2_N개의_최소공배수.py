import math

def solution(arr):
    answer = 0
    
    arr.sort()
    
    lcm=arr[0]
    
    for i in range(1,len(arr)):
        lcm=lcm*arr[i]//math.gcd(lcm,arr[i])
        
    return lcm

solution([2,6,8,14])