
"""
6장
QuickSort Implementation

"""

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >=end:#원소가 1개인 경우 종료
        return
    left = start+1
    right = end
    pivot= start
    while left<=right:
        while left<=end and array[left] <=array[pivot]:
            left+=1
        while right >start and array[right] >=array[pivot]: #여기서 주의 right >=start 가 아닌 right>start
            right-=1
        if left>right:
            array[pivot], array[right] = array[right] , array[pivot]
        else:
            array[left] , array[right] = array[right], array[left]
    quick_sort(array,start, right-1)
    quick_sort(array,right+1,end)

quick_sort(array, 0, len(array)-1)
print(array)


"""파이썬의 장점을 살린 퀵소트 """
array2= [5,7,9,0,3,1,6,2,4,8]
def quick_sort_python(array):
    if len(array)<=1:
        return array
    pivot = array[0]
    tail =array[1:]
    left_side = [x for x in tail if x<=pivot]
    right_side = [x for x in tail if x>pivot]
    return quick_sort_python(left_side) + [pivot] + quick_sort_python(right_side)
print(quick_sort_python(array2))



