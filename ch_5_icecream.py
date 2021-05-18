
#프로그래머스 같은 곳에서는 def solution 안에서 작업해야 하기 때문에, global variable설정이 어렵다.
def solution(n,m, g):
    #변수와 데이터 입력구간
    graph=[]
    n,m= n,m
    for _ in range(n):
        graph.append(g[_])
        print(graph[_])



    # 본격적인 알고리즘 구간 inner function 으로 정의하기.#이렇게 nested function 으로 정의하면, outer function에 접근할 수 있다.
    def dfs(x, y):
        if (x <= -1) or (x >= n) or (y <= -1) or (y >= m):
            return False
        if graph[x][y] == 0:
            # 해당 노드 방문 처리
            graph[x][y] =1
            # 상, 하, 좌, 우 위치 모두 재귀호출
            dfs(x - 1, y)  # 얘네들이 하는건 재귀적으로 graph에 방문표시하는것 밖에 없음
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
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
    return result


graph2 =[
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
    ]
print(solution(len(graph2),len(graph2[0]),graph2))










