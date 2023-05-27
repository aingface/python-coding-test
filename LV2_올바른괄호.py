from collections import deque 
 
def solution(s):    
    ss=deque(s)

    closed_count=0
    opened_count=0

    while(ss):
      char=ss.pop()
      if char=='(':
        closed_count-=1
      elif char==')':
        closed_count+=1

      if closed_count<0:
        return False


    if closed_count ==0 and opened_count==0:
      return True
    
    return False
        
    
      


    


print(solution("(())()"))