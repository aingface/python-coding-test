def test(s):
    # Write your code here
    answer=""
    while("AWS" in s):
        s=s.replace("AWS","")
    
    answer=s

    if len(s)<=0:
        answer= -1
        
    return answer


print(test("AAWSWS"))