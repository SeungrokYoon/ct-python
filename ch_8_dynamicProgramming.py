#다이나믹 프로그래밍
#메모리 추가사용을 통한 수행 시간 압도적 감소

#1. 피보나치 수열
"""
원래라면 재귀를 사용하여 오래 걸렸을 작업이, O(N)으로 줄어든다
"""

def piboMain(n):
    cache = [0]*(n+1)

    def pibo(n):
        if n == 1 or n == 2:
            return 1
        if cache[n] !=0:
            return cache[n]
        cache[n] = pibo(n-1) + pibo(n-2)
        return cache[n]

    return pibo(n)

#2. 1로 만들기
"""
해당 문제는 바텀 업 방식으로, 반복문과 DP테이블을 사용하여, 이전 수행의 결과를 기록해 두고, 이를 사용하여 
다음 수행에 드는 시간을 줄인다.
탑다운으로 생각하면 오히려 오래 걸리는 문제.
"""
def toOne(n):
    dp_table = [0]*(n+1)
    for i in range(1, n+1):
        if i==1:
            dp_table[i] = 0
            continue
        if i==2:
            dp_table[i] = 1
            continue
        #여기에 걸리는 녀석들은 i가 3부터일때이다.
        if  i%5 ==0:
            #min을 i-1인덱스의 값과 함께 쓰는 것이 이 문제의 kick 이다!
            dp_table[i] = min(dp_table[i//5],dp_table[i-1])+1
        elif i%3 ==0:
            dp_table[i] = min(dp_table[i//3],dp_table[i-1])+1
        elif i%2 ==0:
            dp_table[i] = min(dp_table[i//2],dp_table[i-1])+1
        else:
            dp_table[i] = dp_table[i-1]+1
    return dp_table[n]

#정답 코드

def toOne_answer(n):
    d= [0]*30001
    for i in range(2, n+1):
        d[i] = d[i-1]+1
        if i%2 ==0:
            d[i] = min(d[i], d[i//2]+1)
        if i%3 ==0:
            d[i] = min(d[i],d[i//3]+1)
        if i%5 ==0:
            d[i] = min(d[i],d[i//5]+1)
    return d[n]

"""
내 코드와 정답 코드 둘 다 마지막 테이블의 값들이 일치. 
미리 +1을 해서 min 을 비교하는 것과, 비교하고 +1을 하는 것이 일치. 중요한건 바텀 업이라는 것! 중복되는 작업이 많다면, 바텀 업을 고민해보자. 
"""


#3. 개미 전사
"""
이 문제도 바텀 업일까....?
"""
import sys
def ant_warriors():
    input= sys.stdin.readline
    N = int(input())
    house = list(map(int, input().split()))
    robbing = [0]*100
    robbing[0] = house[0]
    robbing[1] = max(house[0],house[1])
    for i in range(2,N):
        robbing[i]= max(robbing[i-2]+house[i],robbing[i-1])
    print(robbing[N-1])

#4. 바닥 공사
"""
다이나믹 프로그래밍의 기초 예제인 타일링 문제 유형
"""
import sys
def tile():
    input= sys.stdin.readline
    n= int(input())
    case = [0]*1001
    case[1]=1
    case[2]=3
    for i in range(3,n+1):
        case[i] = (case[i-1]+2*case[i-2]) %796796
    return case[n]

#5. 효율적인 화폐 구성

import sys
def coins():
    #값 입력 받기
    input= sys.stdin.readline
    N,M = map(int, (input().rstrip().split()))
    #다이나믹 프로그래밍을 위해서 담아놓기
    coins=[]
    table = [10001]*(M+1)
    for _ in range(N):
        coins.append(int(input()))
    table[0] = 0
    coins.sort()

    #핵심 로직
    """
    coins에 담겨있는 녀석들로만 조합을 맞추면 된다.
    """
    for i in range(N):
        for j in range(coins[i], M+1):
            #여기서 j-coins[i] 는 list index out of range를 발생시키지 않는다.
            if table[j- coins[i]] != 10001:
                table[j] = min(table[j], table[j-coins[i]]+1)
    if table[M] == 10001:
        return -1
    return table[M]





if __name__ =='__main__':

    print(piboMain(100))
    print(toOne(26))
    print(ant_warriors())
    print(tile())
    print(coins())






