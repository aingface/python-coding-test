from collections import deque
"""
1.여는 괄호면 stack에 넣는다
2.닫는 괄호면 s에서 뽑은 괄호 v와 stacK[-1]이 서로 짝인지 확인해야한다.
3.서로 짝인지 확인하는 방법은 dict를 만들어서 알 수 있다. 
"""


def solution(s):
    answer = 0
    pair={'[':']', '{':'}', '(':')'}

    for i in range(len(s)):
        a=s[i:]
        b=s[:i]
        circulated_s=deque(a+b)    
        stack=deque([])
        iscorrect=True
        for v in circulated_s:
            #여는 괄호면 스택에 append 
            if v in ['[','{','(']:
                stack.append(v)
            #스택이 비었거나 v가 스택 top의 짝이 아니면 break
            elif not stack or v != pair[stack[-1]]:
                iscorrect=False
                break
            #v가 스택 top의 짝이면 정답 개수 1 추가
            else:
                stack.pop()

        
        if len(stack)==0 and iscorrect==True:
            answer+=1
        
    return answer

solution("[]()")
