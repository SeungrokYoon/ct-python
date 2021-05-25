"""
7장 실전문제 2 - 부품 찾기

input

5
8 3 7 9 2
3
5 7 9
"""

import sys
input = sys.stdin.readline

#값 입력받기
N = int(input().rstrip())
store = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
customer = list(map(int, input().rstrip().split()))

#탐색
#접근방식1. sort()를 통한 정렬 후, 이진탐색
#접근방식2. 계수정렬을 통한 정렬


#재귀 2진 탐색 구현
def search1(store, low, high, part):
    #2진탐색
    mid = (low +high)//2
    if low >high:
        return None
    if store[mid] == part:
        return mid
    elif part > store[mid]:
        return search1(store, mid+1, high, part)
    else:
        return search1(store, low, mid-1, part)

#반복문 2진 탐색 구현
def search2(store, low, high, part):
    while low<=high:
        mid = (low+high) //2
        if store[mid] ==part:
            return mid
        elif part > store[mid]:
            low =mid+1
        else:
            high =  mid-1
    return None

#계수정렬을 통한 풀이
def search3(store,customer):
    largest = max(store)
    #최대값+1만큼의 자리를 만들어주기
    l = [0] * (largest+1)
    #리스트에 저장해주기.
    for i in store:
        l[i] +=1

    #찾기
    for part in customer:
        if l[part] !=0:
            print('yes', end = ' ')
        else:
            print('no', end = ' ')
    return



#확인
#search1
for part in customer:
    store.sort()
    if search1(store, 0, N-1 , part):
        print('yes',end =' ')
    else:
        print('no', end =' ')

#search2
for part in customer:
    store.sort()
    if search2(store, 0, N-1 , part):
        print('yes',end =' ')
    else:
        print('no', end =' ')

#search3
search3(store, customer)







