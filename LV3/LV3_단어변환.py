# hit과 target의 길이는 같다

"""
hit->cog
"hit" -> "hot" -> "dot" -> "dog" -> "cog"

해결 아이디어
1.현재 단어에서 한글자만 다른 것들을 targets에서 찾음. 이 단어들은 checked에 넣음. count+=1
2. target과 일치하는지 검사.
3. 1,2 반복
"""
from collections import deque

#BFS로 해결
def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append([begin, 0])
    cheked = [False] * len(words)

    #queue가 빌때까지 검사
    while queue:
        word, count = queue.popleft()
        if word == target:
            answer = count
            break
        # words에서 word와 한글자 다른 단어 찾기
        for i in range(len(words)):
            differ_count = 0
            word_to_check = words[i]
            # word_to_check가 이미 검사한 단어가 아니면
            if not cheked[i]:
                # 한글자만 다른지 검사
                for j in range(len(word)):
                    if word[j] != word_to_check[j]:
                        differ_count += 1

                if differ_count == 1:
                    queue.append((word_to_check, count + 1))
                    cheked[i] = True
    return answer


solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
