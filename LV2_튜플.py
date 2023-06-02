def solution(s):
    answer = []

    # 중괄호와 쉼표를 기준으로 원소 분리
    elements = s.replace("{{", "").replace("}}", "").replace("},{"," ")
    # 정수로 변환된 리스트 생성
    list_str_s=list(map(str,elements.split(" ")))
    
    list_s=[list(map(int,v.split(","))) for v in list_str_s]
    
    # 원소의 길이 순으로 정렬
    sorted_s=sorted(list_s,key=len)

    #처음 순서 넣어주기
    answer.append(sorted_s[0][0])

    for i in range(1,len(sorted_s)):
        for element in sorted_s[i]:
            if element not in answer:
                answer.append(element)
    return answer


sol=solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
print(sol)