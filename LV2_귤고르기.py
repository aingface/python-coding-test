from collections import Counter

#Counter는 클래스 객체를 반환한다. 그래서 리스트나 딕셔너리로 변환해 사용할 수 있다.


# def solution(k, tangerine):
#     answer = 0
    
#     counter=list(Counter(tangerine).items())

#     counter.sort(key=lambda x:x[1],reverse=True)

#     for i in counter:
#         k-=i[1]
#         answer+=1
#         if k<=0:
#             break


#     return answer





# """
# 하지만 파이썬이 익숙하지 않다면 from collections import Counter가 생각나지
# 않을 수도 있다.. 그러면 아래와 같이라도 풀어야한다

# """

# def solution(k, tangerine):
#     answer = 0
#     #무게가 다른 귤들 개수를 담는 배열 l, index가 귤의 무게이다
#     l = [0 for i in range(max(tangerine))]
#     for i in range(len(tangerine)):
#         l[tangerine[i]-1] += 1
 
#     l.sort(reverse = True)

#     #answer<k일 경우에 개수가 많은 귤부터 answer에 합친다. 
#     index = 0
#     while answer<k:
#         answer += l[index]
#         index += 1
#     return index


solution(6,[1, 3, 2, 5, 4, 5, 2, 3])