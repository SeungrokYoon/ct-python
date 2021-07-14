import sys
"""
그리디 알고리즘이었던 다익스트라 알고리즘과는  다르게, 
플로이드 워셜 알고리즘은 다이나믹 프로그래밍이다. 
하나의 거쳐갈 노드를 선택하고, 그 노드를 제외한 나머지 노드들 중, 2개를 선택하여 
점화식을 적용한다. 
"""
input = sys.stdin.readline
INF = int(1e9)
def floyd_warshall():
    # 인덱스 알기 쉽게  (n+1)*(n+1) 크기로 해준다.
    n = int(input())
    m = int(input())
    dp_table = [[INF]*(n+1) for _ in range(n+1)]
    # [n+1][n+1]위치 값은 0 으로 넣어준다. 자기 자신으로의 가중치는 0 으로 설정해주는 것
    for i in range(n+1):
        dp_table[i][i] = 0

    # 그래프 값 입력받기
    for _ in range(m):
        a,b,c = map(int, input().split())
        dp_table[a][b] = c

    # O(N**3)의 시행 시작
    # 여기서 포인트는 a,b가 같은 경우는 어차피 0 이 최소값이 되기 때문에 영향을 받지 않는다는 점!
    for k in range(1, n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                dp_table[a][b] = min(dp_table[a][b], dp_table[a][k]+dp_table[k][b])

    # 출력
    for i in range(1,n+1):
        print(dp_table[i][1:])
    return

print(floyd_warshall())
"""
예시입력
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
"""