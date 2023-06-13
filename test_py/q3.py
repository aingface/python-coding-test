def maxLength(a, k):
    answer=0
    maxLen=0
    start,end=0,0
    sum=a[0] # 길이가 1 이상이라서 

    while start<len(a) and end<len(a) and start<=end:
        #sum이 k보다 작거나 같은 경우
        if sum <= k:
            #가장 긴 부분수열 길이인지 검사
            maxLen=max(end-start+1,maxLen)
            end+=1
            if end<len(a):
                sum+=a[end]

        else:
        #sum이 k보다 큰 경우 
            sum-=a[start]
            maxLen-=1
            start+=1

    
    return maxLen

input=[74, 659, 931, 273, 545, 879, 924, 710, 441, 166, 493, 43, 988, 504, 328, 730, 841, 613, 304, 170, 710, 158, 561, 934, 100, 279, 817, 336, 98, 827, 513, 268, 811, 634, 980, 150, 580, 822, 968, 673, 394, 337, 486, 746, 229, 92, 195, 358, 2, 154, 709, 945, 669, 491, 125, 197, 531, 904, 723, 667, 550]
input1=[3,1,2,1]
input2=[1,2,3,4,5,6,7,8,9,10]

print(maxLength(input2,55))