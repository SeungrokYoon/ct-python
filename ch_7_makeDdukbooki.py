"""
7장 실전문제 3 - 떡볶이 떡 만들기

핵심 개념 : 파라매트릭 서치(Parametric Search)

input
4 6
19 15 10 17

"""

import sys
input =sys.stdin.readline

N, M = map(int, input().rstrip().split())
ddoks = list(map(int, input().rstrip().split()))

R= max(ddoks)
L=0
while L<=R:
    mid = (L+R)//2
    #맞는 조건을 물어보기
    s= 0
    result = 0
    #떡을 자른 녀석들의 합이 s
    for ddok in ddoks:
        if ddok >=mid:
            s+= (ddok -mid)

    if s >= M:
        #너무 조금 잘랐다 좀 올리자
        #문제에서 적어도 M 만큼이라고 했으니, 지금 mid도 정답권에 들어 있음.
        #따라서 더 정답에 가까운 값이 나오기 전까지 result 에 저장해 놓는다.
        result = mid
        L = mid+1
    else:
        #너무 많이 잘랐다 좀 내리자
        R = mid-1




