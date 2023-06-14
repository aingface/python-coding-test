def longestStrChain(words):
    # 단어 길이를 기준으로 단어들을 그룹화합니다.
    word_groups = {}
    for word in words:
        length = len(word)
        if length not in word_groups:
            word_groups[length] = []
        word_groups[length].append(word)

    #길이 순서대로 lengths 를 정렬 
    lengths=sorted(word_groups.keys())

    #단어별로 chain이 몇개인지 저장하는 dict
    chains_of_words={}


    #길이가 짧은 순서대로 
    for length in lengths:
        for word in word_groups[length]:      
            #단어 자체 하나도 길이가 1이다
            chains_of_words[word]=1

            #단어에서 i번째 한글자씩 없애서 predecessor 전부 찾기 
            for i in range(length):
                #슬라이싱은 표현 가능한 범위 까지만 리턴한다
                left=word[:i]
                right=word[i+1:]
                predecessor=left+right

                if predecessor in words:
                    chains_of_words[word]=max(chains_of_words[word],chains_of_words[predecessor]+1)


    return max(chains_of_words.values())







print(longestStrChain(["a","b","ba","bca","bda","bdca"]))