"""
6장 실전문제 2. 위에서 아래로

"""
def downward(numbers):
    result = sorted(numbers, reverse =True)


    return result

alist = [15,27,12]
print(downward(alist))

"""
6장 실전문제 3. 성적이 낮은 순서로 학생 출력하기

"""
def upwardStudent(blist):
    #list comprehenison 에서는 sorted 를 사용하는 것으로 하자고
    result= [i[0] for i in sorted(blist,key= lambda u: u[1])]
    return result

blist= [('홍길동',95), ('이순신',77)]
print(upwardStudent(blist))

"""
6장 실전문제 4. 두 배열의 원소 교체 

"""

def changes(n,k,clist,dlist):
    clist.sort()
    dlist.sort(reverse=True)
    for i in range(k):
        if clist[i] < dlist[i]:
            clist[i], dlist[i] = dlist[i], clist[i]
        else:#굳이 끝까지 k 번 안채워도 되는 것이 뽀인트!!!
            break
    return sum(clist)
clist= [1,2,5,4,3]
dlist= [5,5,6,6,5]
n=5
k=3
print(changes(n,k,clist,dlist))