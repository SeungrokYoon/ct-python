"""
union find algorithm 의
필요성을 느껴 이렇게 정리한다.

"""
#리스트 형태로 구현한 union set
class DisjointSet:
    def __init__(self,n):
        self.data = list(range(n))
        self.size =n
    def find(self,index):
        return self.data[index]


    def union(self,x,y):
        x,y = self.find(x), self.find(y)

        if x ==y:
            return
        for i in range(self.size):
            if self.find(i) ==y:
                self.data[i]=x
    @property
    def length(self):
        return len(set(self.data))

disjoint= DisjointSet(10)
disjoint.union(0,1)
disjoint.union(1,2)
disjoint.union(1,0)
disjoint.union(2,3)
disjoint.union(4,5)
disjoint.union(6,7)
disjoint.union(7,8)

print(disjoint.data)
print(disjoint.length)


#2. 트리구조를 사용하는 방식
