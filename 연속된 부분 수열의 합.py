"""
두 포인터가 움직이면서 sum 값을 조정하는게 키 포인트.
제한 사항을 보면 5 ≤ sequence의 길이 ≤ 1,000,000 이기 때문에
O(n^2)인 경우 타임아웃! 2중 for loop 불가!

중요 변수
  start,end: 부분수열의 시작 인덱스와 끝 인덱스. 초기값 0,0
  minLen: 가장 짧은 연속된 부분 수열의 길이. 초기값 float('inf')
  sum: 부분 수열의 합. 초기값 sequence[0] 

풀이 방법:
  while문을 사용해서 start< len(sequence) 이고 end <len(sequence) 이고 start<=end 인 경우 실행 되게 한다    

  3가지 경우로 나눠보면

    1.sum이 k와 같은 경우
      - minLen > end-start+1 인 경우 minLen을 갱신
      - end에 1을 더해주고 인덱스 범위를 넘지 않았으면 sum+=sequence[end]

    2.sum이 k보다 작은 경우
      - end에 1을 더해주고 인덱스 범위를 넘지 않았으면 sum+=sequence[end]

    3.sum이 k보다 큰 경우
      - sum에서 sequence[start]를 빼주고 start에 1을 더해준다

"""


def solution(sequence, k):
    answer = []

    minLen=float('inf')
    start,end=0,0
    sum=sequence[0]
    sequenceLength=len(sequence)

    while(start < sequenceLength and end<sequenceLength and start <=end):
      if sum<=k:
        if sum==k and (end-start+1) < minLen:
          answer=[start,end]
          minLen=end-start+1 

        end+=1
        if end < sequenceLength:
          sum+=sequence[end]
      else:
       sum-=sequence[start]
       start+=1 
      
    return answer


print(solution([1, 2, 3, 4, 5], 6))