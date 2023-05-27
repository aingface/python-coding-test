#n>=1 을 만족하는 자연수
def count_one_of_binary(n):
    count=0
    
    check_n=n
    while check_n>1:
        if check_n%2==1:
            count+=1
        check_n=check_n//2       
    
    return count 

def solution(n):
    answer = 0
    
    num=n
    
    one_of_n_binary=count_one_of_binary(num)
    
    while num<=1_000_000:
        check_next=count_one_of_binary(num+1)
        
        if one_of_n_binary==check_next:
            answer= num+1
            break
        else:
            num+=1
              
    return answer


print(solution(15))