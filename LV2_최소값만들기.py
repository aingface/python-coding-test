"""
풀이
- A는 오름차순, B는 내림차순으로 정렬 후 A와 B 리스트에서 같은 인덱스에 있는 원소를 곱해서 answer에 더한다
"""

def solution(A,B):
    answer = 0

    sorted_A=sorted(A)
    reversed_B=sorted(B,reverse=True)

    for i in range(len(A)):
        answer+=sorted_A[i]*reversed_B[i]
        

    return answer



print(solution([1, 4, 2],[5, 4, 4]))