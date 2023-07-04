"""
재귀를 이용한 풀이
- 순서대로 모든 원소마다 +/-인 경우를 확인해야한다.
- 길이가 0이면 target과 같은지 비교하고 카운트를 의미하는 값을 반환한다.
"""
def recur(numbers,sum,target):
	if len(numbers)==0:
		if sum==target:
			return 1
		else:
			return 0

	return recur(numbers[1:],sum+numbers[0], target)+ recur(numbers[1:],sum-numbers[0], target)


def solution(numbers, target):
	answer = recur(numbers,0,target)
	return answer