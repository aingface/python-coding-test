def solution(arr1, arr2):
    a=len(arr1)
    b=len(arr2[0])
    c=len(arr2) 
    
    #미리 만들어 놓는게 더 직관적이다
    answer=[[0]*b for _ in range (a)]

    #식을 한번 펜으로 써보면 일반화 식을 유추할 수 있다. 
    for i in range(a):
        for j in range(b):
            for k in range(c):
                answer[i][j]+=arr1[i][k]*arr2[k][j]

    return answer


print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))