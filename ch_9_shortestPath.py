"""
import math
math.int 쓰지 말고,
정수라면 int(1e9)쓰고 실수 자료혀잉라면 1e9를 사용토록 하자.
"""
import sys
"""
1. 다익스트라 알고리즘.
(1) 쉬운버전
이미 알고리즘 수업에서 배웠던 개념이지만, 단순히 그 원리만 
구현해 보았을 뿐, 코딩테스트에 접목하여 공부한 적이 없다.
따라서 이번에는 단순한 구현에서 벗어나 효율적인 코딩테스트에 특화된 버전으로 연습해 보도록 하자. 
"""

input = sys.stdin.readline
INF = int(1e9)


def dijkstra():
    # 노드의 개수, 간선 개수 입력 받기
    n,m = map(int, input().split())
    # 시작 노드 번호 입력받기
    start= int(input())
    # 각 노드에 연겨로디어 있는 노드에 대한 정보를 담는 리스트를 만들기
    graph = [[] for i in range(n+1)]
    # 최단 거리 테이블
    distance = [INF]*(n+1)
    # visited
    visited =[False]*(n+1)
    # 그래프 생성-  인접 리스트가 자원이 덜 든다.
    for _ in range(m):
        a,b,w = map(int, input().split())     # a->b 로 가는 거리가 w
        graph[a].append((b, w))

    # 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
    def get_smallest_node():
        min_value = INF
        index=0
        for i in range(1,n+1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index

    # 핵심 로직
    def business(start):
        # 시작 노드는 거리를 0 으로 해둔다.
        distance[start] = 0
        visited[start] = True
        # 일단 한 바퀴 돌려준다.
        for j in graph[start]:
            distance[j[0]] = j[1] # distance[target] =weight

        for _ in range(n-1):
            now = get_smallest_node()
            visited[now] = True
            for j in graph[now]:
                cost = distance[now] +j[1]
                if cost < distance[j[0]]:
                    distance[j[0]] = cost
    business(start)
    return distance




"""
1. 다익스트라 알고리즘.
(2) 효율적인 버전 
 효율적인 코딩테스트에 특화된 버전으로 연습해 보도록 하자. 
핵심은 힙큐를 이용해서 진행하는 것임.

개선된 알고리즘에서는 visited를 사용하지 않는다. 
"""
import heapq


def dijkstra_heapq():
    # 1. 그래프 생성
    n, m = map(int, input().split())
    graph=[[] for i in range(n+1)]
    startNode = int(input())
    #disance의 역할은 시작 노드에서 각 노드까지 걸리는 최소거리를 기록하기 위함
    distance = [INF] * (n+1)
    for _ in range(m):
        a,b,w = map(int, input().split())
        graph[a].append((b,w))

    """
    여기서 핵심은 heqpq와 disatnce 를 따로 운용하는 것임. 
    가장 w가 작은 node 를 효율적인 알고리즘으로 뽑아내는 용도로만 heapq를 
    사용하고, 그 기록은 distance에 한다. 
    """
    def business(start):
        q = []
        # 첫번째 노드는 방문 표시 해 놓고, 힙에 넣어놓기.
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q: # heap_queue 가 빌 때 까지 아래의 작업을 반복한다.
            # heappop(q)으로 튀어나온 녀석은 가장 작은 weight를 0 번 인덱스에 가지고 있다.
            d, now = heapq.heappop(q)

            #heapq에서 나오긴 나왔는데, 이미 now까지 갱신된 거리보다 멀다면 굳이 볼 필요없잖아!


            if d > distance[now]:
                continue
            # 연결된 모든 정점들을 다 확인해본다. visited가 없으니 뭐.....
            for i in graph[now]:
                cost = i[1] + d
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    business(startNode)
    print(distance)
    return distance


print(dijkstra_heapq())
"""
입력 데이터
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

"""




















