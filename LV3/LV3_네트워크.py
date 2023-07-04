from collections import deque

#가장 멀리있는 노드를 우선적으로 방문
def DFS(graph,v,visitted):
    #현재 노드를 방문처리
    visitted[v]=True

    for i in range(len(graph[v])):
        if not visitted[i] and graph[v][i]:
            DFS(graph,i,visitted)


#가장 가까이 있는 노드부터 탐색하는 알고리즘, 큐를 이용
def BFS(graph,start,visitted):
    queue=deque([start])
    visitted[start]=True

    while queue:
        left=queue.popleft()

        for i in range(len(graph[left])):
            if not visitted[i] and graph[left][i]:
                queue.append(i)
                visitted[i]= True




def solution(n, computers):
    visitted=[0]*n
    answer = 0
    
    for i in range(n):
        if not visitted[i]:
            # DFS(computers,i,visitted)
            BFS(computers,i,visitted)
            answer=answer+1
    
    return answer

solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]])