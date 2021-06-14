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
print(piboMain(100))


#2. 1로 만들기
"""
해당 문제는 바텀 업 방식으로, 반복문과 DP테이블을 사용하여, 이전 수행의 결과를 기록해 두고, 이를 사용하여 
다음 수행에 드는 시간을 줄인다.
탑다운으로 생각하면 오히려 오래 걸리는 문제.
"""
def toOne(n):
    d= [0]*30001
    for i in range(2, n+1):
        d[i] = d[i-1]+1
        if i%2 ==0:
            d[i] = min(d[i],d[i//2]+1)
        if i%3 ==0:
            d[i] = min(d[i], d[i//3]+1)
        if i%5==0:
            d[i] = min(d[i], d[i//5]+1)
    return d[i]

print(toOne(26))


#3. 개미 전사
import sys
def ant_warrior():
    input = sys.stdin.readline
    n = int(input().rstrip())
    alist = list(map(int, input().rstrip().split()))

    #반복문을 사용한 바텀업 방식이 효율적일 듯 하다.
    #n번 창고를 털 때 까지의 최대값을 기록해 두자.
    dp_table = [0]*(n)
    dp_table[0]= alist[0]
    dp_table[1] = max(alist[0], alist[1])
    for i in range(2, n):
        dp_table[i] = max(dp_table[i-1], dp_table[i-2]+alist[i])
    print(dp_table[n-1])




    #아래 내 코드가 틀린 이유: 이 문제는 단순히 홀 짝 매커니즘이 아니다.
    # for i in range(1,n+1):
    #     if i-2<=0:
    #         storage[i] = alist[i]
    #     if i-2>0:
    #         storage[i] = storage[i-2]+alist[i]
    # print( max(storage[n-1], storage[n]))
    # return max(storage[n-1], storage[n])
ant_warrior()






