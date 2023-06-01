'''
headgear는 총 2개 있으니, 스파이에게는 총 3가지의 경우의 수가 있다.
1번을 입는다.
2번을 입는다.
headgear를 아무것도 입지 않는다.
eyewear는 총 1개 있으니, 스파이에게는 총 2가지의 경우의 수가 있다.
1번을 입는다.
eyewear를 입지 않는다.
그렇다면 총 3 x 2 가지의 경우의 수 인 6가지가 존재하고, 이 중 한 가지는 headgear도 입지 않고 eyewear도 입지 않은 경우가 되기 때문에 이 경우를 제외하 5가지가 정답이 되게 된다.
이를 컴퓨터 프로그램으로 짜서 컴퓨터에게 일을 시키기 위한 방법은 두 가지가 떠오른다.
'''

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    # reduce함수(함수, 반복할 데이터, 초기값). 초기 값 설정 하면 x는 초깃값, 아니면 반복데이터에서 순서대로 x,y 
    
    
    answer = reduce(lambda x, y: x*(y+1), cnt.values(),1) - 1   

    return answer


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))