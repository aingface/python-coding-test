"""
내가 푼 방법, 소거법으로 찾다보니 풀었지만 실전이었다면 이렇게 못풀었을 방법
"""

# import math 

# def solution(brown, yellow):
    
#     b_y=brown+yellow
    
#     sqrt_b_y=math.sqrt(b_y)

#     width=math.ceil(sqrt_b_y)
#     column=math.floor(sqrt_b_y)

#     while 1:
#         if width*column ==b_y and (width+column-2)*2==brown:
#             return [width,column]

#         elif width*column>=b_y:
#             column-=1

#         else:
#             width+=1

"""
노란색 격자의 둘레를 이용해 카펫의 가로 세로를 계산하는 방법
"""


def solution(brown, yellow):
    #세로인 i가 int(yellow**(1/2))이하인 이유는 카펫은 가로가 더 크거나 같기 때문
    for i in range(1, int(yellow**(1/2))+1):
        #만약 i가 노란 격자의 세로가 될 수 있다면  
        if yellow % i == 0:
            #만약 노란 격자의 (세로인 i + 가로 x)*2가 brown-4라면
            if 2*(i + yellow//i) == brown-4:
                return [yellow//i+2, i+2]


print(solution(10,2))