def solution(arr):
    dict={"BOOL":1, "SHORT":2, "FLOAT":4, "INT": 8, "LONG":16}
        
    answer=[]
    buffer=""
    
    #먼저
    first=dict[arr[0]]
    if first<8:
        buffer+='#'*first
    elif first==8:
        answer.append('#'*8)
    else:
        answer.append('#'*8)
        answer.append('#'*8)

    if len(arr)==1 and len(buffer)>0:
        answer.append(buffer+'.'*(8-len(buffer))) 

    for i in range(1,len(arr)):
        now=dict[arr[i]]
        prev=dict[arr[i-1]]        
        
        dots=0
        
        if len(buffer)>0:
            if now-prev>0:
                dots=now-prev    
            else: 
                dots=0

        temp=buffer+'.'*dots+'#'*now

        #현재 값을 버퍼에 합쳤을 때 길이가 8미만인 경우 
        if len(temp)<8: 
            buffer=temp
        #현재 값을 버퍼에 합쳤을 때 길이가 8인경우
        elif len(temp)==8: 
            buffer=temp
            answer.append(buffer)
            buffer=""

        #현재 값을 버퍼에 합쳤을 때 길이가 8을 초과한 경우, 현재 버퍼의 나머지 공간을 .으로 채우고 새로운 버퍼에 할당해야한다
        else:
            answer.append(buffer+'.'*(8-len(buffer))) 
            
            if now ==8:
                answer.append('#'*now)
                buffer=""
            elif now ==16:
                answer.append('#'*8)
                answer.append('#'*8)
                buffer=""
            else:
                buffer+='#'*now

        if i==len(arr)-1 and len(buffer)>0:
            answer.append(buffer+'.'*(8-len(buffer))) 

    if len(answer)>128//8:
        print('HALT')
        return "HALT"

    for v in answer:
        print(v)

    return answer


# solution(["INT","INT","BOOL","SHORT","LONG"])
# solution(["INT","SHORT","FLOAT","INT","BOOL"])
# solution(["FLOAT","SHORT","BOOL","BOOL","BOOL","INT"])
# solution(["BOOL","LONG","SHORT","LONG","BOOL","LONG","BOOL","LONG","SHORT","LONG","LONG"])
# solution(["FLOAT"])