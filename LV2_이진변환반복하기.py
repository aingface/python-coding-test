def solution(s):
    answer = []
    #이진 변환의 횟수 
    binarified_count=0
    # 변환 과정에서 제거된 모든 0의 개수
    zero_count=0

    while s!="1":
      #s에서 0제거하기
      no_zero_s=""
      for i in s:
         if i =="1":
            no_zero_s+=i
         elif i=="0":
            zero_count+=1

      s=no_zero_s

      length_of_s=len(s)

      binary_of_s=""
      #0제거된 s길이를 이진수로 변환
      while True:
        if length_of_s==1:
           binary_of_s+="1"
           break
        
        rest_of_s=length_of_s%2
        length_of_s=length_of_s//2

        if rest_of_s%2==0:
          binary_of_s+="0"  
                   
        elif rest_of_s%2==1:
          binary_of_s+="1"

      s=binary_of_s  
      binarified_count+=1

    return [binarified_count,zero_count]




print(solution("110010101001"))