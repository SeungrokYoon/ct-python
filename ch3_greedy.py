"""
예제 3-1 거스릅돈 문제.
당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50 원, 10원 짜리
동전이 무한히 존재한다고 가정한다. 손님에게 거슬러 줘야 할 돈이 N 원일 때 거슬러줘야할 동전의 최소 개수를 구하라.
단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.
"""
def solution1(N):
    answer=0
    money =N
    lst= [500,100,50,10]
    for coin in lst:
        answer+= money//coin
        money = money%coin
    return answer

"""실전문제 2 큰수의 법칙.
"""

def solution2(N):
    answer=0
    alist, blist = N.split("\n")
    alist = list(map(int,alist.split()))
    blist = sorted(list(map(int, blist.split())), reverse=True)
    counter = 0
    limit = alist[2]
    pos = 0
    for _ in range(alist[1]):
        if counter < limit:
            answer += blist[pos]
            counter+= 1
        else:
            answer += blist[pos+1]
            counter = 0
    return answer

def solution2_1():
    answer=0
    n , m, k = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort()
    first = data[n-1]
    second = data[n-2]
    answer += (k*first+second)*(m//(k+1))
    answer += first*(m%(k+1))
    return answer


def solution3(N):
    #정보 입력
    n , m = map(int, input().split())
    answer = 0
    for _ in range(n):
        temp = list(map(int, input().split()))
        # if min(temp) > minNum:
        #     minNum = min(temp)
        answer = max(answer, min(temp))
    return answer

def solution4(N):
    answer = 0
    n, m = list(map(int, input().split()))
    while n != 1:
        if n%m !=0:
            n-=1
        else:
            n= n//m
        answer+=1
    return answer



if __name__ == '__main__':
    N1=1260
    N2 = "5 8 3\n2 4 5 4 6"
    N3 = 0
    N4 = 0
    # for i in range(1,5):
    #     print(eval("solution"+str(i)+"(N"+str(i)+")"))
    print(solution4(0))