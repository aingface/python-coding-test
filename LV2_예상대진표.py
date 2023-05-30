import math

def solution(n,a,b):
    answer = 0

    while 1:
        #a의 번호와 b의 번호가 같을 때 break
        if a==b:
            break

        a=math.ceil(a/2)
        b=math.ceil(b/2)
        answer+=1


    return answer

solution(8,4,7)