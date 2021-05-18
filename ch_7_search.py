"""
재귀로 구현하는 이진탐색 알고리즘
-> 여기서는 return이 있다. 왜? base가 있어야 하니까.


"""
def binary_search(array,target, start,end):
    if start>end:
        return None
    mid =(start+end)//2
    if array[mid] ==target:
        return mid
    elif array[mid] >target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

target =7
array = [1,3,5,6,11,13,15,17,19]
result = binary_search(array, target, 0,len(array)-1)
if result == None:
    print("해당원소가 존재하지 않습니다")
else:
    print(result +1)

"""
반복문으로 구현하는 이진탐색 알고리즘 
한편, 여기서는 return 이 재귀가 들어갈 부분에서는 존재하지 않는다. 


"""
def binary_search_repetition(array, target, start, end):
    while start <=end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start = mid+1
    return None
array = [1,3,5,6,7,11,13,15,17,19]
result = binary_search_repetition(array, 7, 0,len(array)-1)
if result == None:
    print("해당원소가 존재하지 않습니다")
else:
    print(result +1, "번째 있음")


a= 3
print(a >>1 )

"""
빠르게 입력받기

"""
