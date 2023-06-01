"""
규칙성 찾기 문제
if) index = 8, n = 4

(i // n, i % n) → (2, 0) → 3

 

if) index = 9, n = 4

(i // n, i % n) → (2, 1) → 3

 

if) index = 10, n = 4

(i // n, i % n) → (2, 2) → 3

여기서 조건을 유추해서 적용해본다
"""

def solution(n, left, right):
    answer = []

    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    
    return answer

print(solution(1,0,0))