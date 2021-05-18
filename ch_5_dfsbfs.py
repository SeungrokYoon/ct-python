"""
1. DFS 구현
"""
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end =' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph =[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9

dfs(graph, 1, visited)
"""
1-1. DFS 구현 실전예제
1) 인접리스트로 DFS 구현하기.
"""

#0번 인덱스가 빈 리스트인 이유는 0번 노드가 있다고 생각하지만, 그 어디의 다른 노드와도 간선이 없는 경우를 산정.
    #이렇게 설정해 놓는 이유는
    #노드들의 번호와 graph 내에서의 index를 일치시키는 것이 편리하기 떄
graph2 = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
        ]

#빈 노드까지 포함해서
visited2 = [False]*(9)

def dfs2(graph, v, visited):
    #v번 노드부터 시작한다.
    print(v, end= ' ' )
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs2(graph, i, visited)
print("\ndfs2 test")
dfs2(graph2, 1, visited2)


"""
2. BFS 구현
"""
#내코드

from collections import deque
def bfs(graph, node, visited):
    queue =deque([])
    queue.append(node)
    visited[node] = True
    level=0
    while len(queue) != 0:
        next = queue.popleft()
        print(next, end = '->')
        for i in graph[next]:
            if not visited[i]:
                queue.append(i)
                visited[i] =True

#교재코드
def dfs_book(graph, node, visited):
    queue = deque([node])
    visited[node] =True
    while queue:
        next= queue.popleft()
        print(next, end=' ')
        for i in graph[next]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


print("\nbfs 테스트")

visited = [False]*(9)
bfs(graph, 1, visited)
print("")

"""
Exercise 1 음료수 얼려먹기 
"""
def make_icecream(g):
    graph = []
    #변수와 데이터 입력구간

    n, m = map(int, input().split())
    visited = [[False]*m for _ in range(n)]
    for _ in range(n):
        graph.append(g[_])

    #본격적인 알고리즘 구간 inner function 으로 정의하기.
    def dfs(x,y):
        if x<=-1 or x>=n or y<=-1 or y>=m:
            return False
        if graph[x][y] ==0 :
            #해당 노드 방문 처리
            graph[x][y] =1
            #상, 하, 좌, 우 위치 모두 재귀호출
            dfs(x-1,y) #얘네들이 하는건 재귀적으로 graph에 방문표시하는것 밖에 없음
            dfs(x, y-1)
            dfs(x+1,y)
            dfs(x, y+1)
            return True
            """
            True 를 하는 이유: graph[x][y] == 0이어서. 오직 해당 그래프 값이 0일 때 True를 리턴한다. 이 경우
            상하좌우로 dfs가 퍼져나가면서 1을 퍼트린다. 결국 하나의 좌표가 True를 리턴하지만, 
            다음 실행에서는 인접한 0의 값 좌표 들은 True가 되지 못한다.
            """
        return False
    result=0
    for i in range(n):
        for j in range(m):
            #현재 위치에서 dfs수행
            if dfs(i,j) ==True:
                result +=1
    print(result)


graph =[
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
    ]
make_icecream(graph)



from collections import deque
def escape_maze(maze,s):
    maze= maze
    s=s
    x = 0
    y = 0
    #큐 정의
    #상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    def bfs(x,y):
        queue = deque()
        queue.append((x, y))
        while queue:
            x,y = queue.popleft()
            print(x,y)
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or ny<0 or nx>=s[0] or ny >=s[1]:
                    continue
                if maze[nx][ny] ==0:
                    continue
                if maze[nx][ny] ==1:
                    maze[nx][ny] = maze[x][y] +1
                    queue.append((nx,ny))
        return maze[s[0]-1][s[1]-1]
    answer = bfs(x,y)
    return answer





s = [5,6]
maze= [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
    ]
print(escape_maze(maze,s))


















