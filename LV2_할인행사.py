from collections import Counter

#내 풀이
# def solution(want, number, discount):
#     answer = 0

#     #원하는 상품별로 몇개 있는지 dict
#     dict_want=dict(zip(want, number))
#     test=[]
#     #discount<=10만이니깐 N(O^2)는 안될것. 순차로 가자
#     for i in range(len(discount)):
#         iscorrect=True
#         check_ten_days=[]
#         if i+9<len(discount):
#             check_ten_days=discount[i:i+10]
#         else:
#             continue

#         dict_ten_days=dict(Counter(check_ten_days))
#         for key in dict_ten_days:  
#             if key not in dict_want or dict_want[key]!=dict_ten_days[key]:
#                 iscorrect=False
#                 break

#         if iscorrect:
#             test.append(i+1)
#             answer+=1

#     return answer

"""
마음에 든 풀이
dict는 비교할 수 있다
문제를 정확히 읽자
"""

from collections import Counter

def solution(want, number, discount):
    answer = 0

    #원하는 상품별로 몇개 있는지 dict
    dict_want=dict(zip(want, number))
    test=[]
    #discount<=10만이니깐 N(O^2)는 안될것. 순차로 가자
    for i in range(len(discount)-10+1):
        if dict_want==Counter(discount[i:i+10]):
            answer+=1


    return answer


solution(["banana", "apple", "rice", "pork", "pot"],	[3, 2, 2, 2, 1],	["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])