import math
from collections import Counter
def divide_str(str):
    result=[]
    for i in range(len(str)-1):
        element=""

        a=str[i]
        b=str[i+1]
        if a.isalpha() and b.isalpha():
            element=a+b
            result.append(element)
        else:
            continue
        
    return result

def solution(str1, str2):
    answer = 0
    
    str1=str1.lower()
    str2=str2.lower()

    devided_str1=divide_str(str1)
    devided_str2=divide_str(str2)

    #같은 원소도 중복되는 다중 집합의 경우 리스트의 원소 별로 개수를 알 수 있는 Counter를 활용
    Counter1=Counter(devided_str1)
    Counter2=Counter(devided_str2)

    #Counter.elements 는 원소만 반환. set으로 교/합집합 만들듯이 활용할 수 있다 
    intersection=list((Counter1 & Counter2).elements())
    union=list((Counter1 | Counter2).elements())

    # print("union: ",union)
    # print("intersection: ",intersection)

    len_intersection=len(intersection)
    len_union=len(union)
    
    if len_union==0:
        return 1*65536
    
    answer=math.floor((len(intersection)/len(union))*65536)   
                    
    return answer

solution("abab",  "baba")

             