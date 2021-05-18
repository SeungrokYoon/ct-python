"""
non comparison based sorting
Count Sort

우리가 흔히 연습해왔던 정렬 방식은 비교 기반의 정렬 알고리즘이었다.
그렇지만, 이번에 알아볼 Count Sort 라는 녀석은 신기한 방식으로 정렬을 하고,
최악의 경우에도 O(N+k)의 시간 복잡도를 유지하는 신기한 녀석이다. 겁나 간단하다.
동일한 값을 여러개 등장하며, 값들 간 간격이 넓지 않을 때 유용함.
계수 정렬의 공간 복잡도는 O(N+K)이다. 
"""
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0]*(max(array)+1) #1을 더하는 이유는 0이 있기 때문
for i in range(len(array)):
    count[array[i]] +=1
for i in range(len(count)):
    for j in range(count[i]):
        if i ==len(count)-1 and j == count[i]-1:
            print(i, end= ' ')
        else:
            print(i, end='->')
