def findRange(num):
    answer=0
    max=num 
    min=num
    stringfied_num=str(num)
    
    #max 찾기
    for i in range(len(stringfied_num)):
        max_now_degit=stringfied_num[i]
        
        if max_now_degit=='9':
            continue
        else:
            max=int(stringfied_num.replace(max_now_degit,"9"))
            break;            
    
    #min 찾기
    for i in range(len(stringfied_num)):
        min_now_digit=stringfied_num[i]
        #첫번째 자리가 1이면 다음 자리로 continue
        if i==0:
            if min_now_digit=='1':
                continue
            else:
                min=int(stringfied_num.replace(min_now_digit,"1"))
                break
        #현재 검사하는 자리가 0이 아니면 0으로 바꾸기
        else:
            if min_now_digit !='0':
                #현재 검사하는 자리가 첫번째 자리값과 같지 않으면 0으로 바꾸기
                if stringfied_num[0]!=min_now_digit:
                    min=int(stringfied_num.replace(min_now_digit,"0"))
                    break
                else:
                    continue
            else:
                continue                 
    
    answer=max-min
    
    return answer

print(findRange(112233445))