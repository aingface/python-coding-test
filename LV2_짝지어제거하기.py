
"""
s의 길이 n은 n<=1_000_000, O(N)해야한다
잘랐다 붙이고 하면 안됨 순차탐색 한번만 
"""

from collections import deque

def solution(s):

    deque_s=deque([])

    for char in s:
        #deque_s가 비었으면 char를 넣고 
        #안비었으면 deque_s[-1]을 비교해서 일치할 시 deque.pop(), 아니면 deque.append(char)  
        if len(deque_s)>0 and deque_s[-1] ==char:
            deque_s.pop()
        else:
            deque_s.append(char)
    
    
    if len(deque_s)==0:
        return 1

    return 0
    
print(solution("baabaa"))