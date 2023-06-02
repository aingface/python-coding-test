import math

def solution(progresses, speeds):
    answer=[]
    for p, s in zip(progresses, speeds):
        #answer[]가 비었거나 현재 보고있는 작업 완료 일이 이전 작업의 완료일보다 늦으면(더크면) 
        # answer[]에 [해당 작업의 개발 완료 일,한 번 배포할 떄 배포 가능한 작업 수== 1]를 추가
        left=math.ceil((100-p)/s)
        if len(answer)==0 or answer[-1][0]<left:  #-((p-100)//s)는 ceil 메소드 사용 안하기 위함
            answer.append([-((p-100)//s),1])
        #아니면 answer[]의 마지막인자의 [1]번 수에 1더해주기
        else:
            answer[-1][1]+=1
    #q에서 1번째(count)만 모아서 return
    return [left_dev_info[1] for left_dev_info in answer]


sol=solution([93, 30, 55],	[1, 30, 5])
# sol=solution([95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1])

print(sol)