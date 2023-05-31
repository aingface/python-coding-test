def solution(elements):
    #부분수열 합으로 만들 수 있는 종류 
    answer = []

    #부분 수열의 길이 i
    for i in range(1,len(elements)+1):
        #부분수열 sum 시작점 j
        for j in range(len(elements)):
            elements2=elements+elements[:-1]
            sum1=sum(elements2[j:j+i])

            answer.append(sum1)

    return len(set(answer))


'''
더 빠른 방법

elements[i]부터 시작해서 길이가 1~len(elements)인 부분수열을 구하는 방법
'''

# def solution(elements):
#     ll = len(elements)
#     res = set()

#     for i in range(ll):
#         ssum = elements[i]
#         res.add(ssum)
#         for j in range(i+1, i+ll):
#             ssum += elements[j%ll]
#             res.add(ssum)
#     return len(res)
