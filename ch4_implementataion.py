"""
이것이 코딩 테스트다 4장 구현 문제 풀이
"""

"""
예제 4-1 상하좌우
"""
import time

#1.내가 구현한 코드
def travelPlan():
    n=int(input("Enter a number: "))
    plans = [x.upper() for x in input().split()]
    x,y = 1,1

    for eachPlan in plans:
        if eachPlan.upper() == 'U':
            if x-1 >=1:
                x-=1
        elif eachPlan.upper() =='R':
            if y+1 <=n:
                y+=1
        elif eachPlan.upper() =='L':
            if y-1 >=1:
                y-=1

        elif eachPlan.upper() =='D':
            if x+1 <=n:
                x+=1
    return (x,y)


def travelPlan2():
    n = int(input())
    plans = [x.upper() for x in input().split()]
    x, y = 1, 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x+ dx[i]
                ny = y +dy[i]
        if nx<1 or ny<1 or nx>n or ny>n:
            continue
        x,y= nx, ny
    return (x,y)


"""
입력값 예시
5
r r r u d d
"""

"""
예제 4-2 시각
"""
def countThree():
    givenT = int(input())
    answer = 0
    for hour in range(givenT+1):
        if hour%10 ==3:
            answer+=3600
        else:
            minWithThree = (15) *60
            minWithNoThree = 45 *(15) # 10개 (30번대 숫자들) + 3 , 13, 23, 43 ,53
            answer += (minWithThree + minWithNoThree )
    return answer

"""
실전문제 왕실의 나이트 

"""
def findNight(position):
    input_data = input()
    row = int(input_data[1])
    column = int(ord(input_data[0])-int(ord('a')))+1
    steps= [(-2,-1),(-1,-2),(1,-2), (2,-1), (2,1), (1,2),(-1,2),(-2,1)]

    result =0
    for step in steps:
        next_row = row+ step[0]
        next_column = column +step[1]
        if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
            result+=1
    return result


"""
실전 문제 게임 개발
"""
s
def gameDevelopment():
    n,m = map(int, input("Enter map size: ").split())
    d= [[0]*m for _ in range(n)] #방문처리 리스트
    x,y, direction = map(int, input().split())


    d[x][y] = 1 #현재 좌표 방문 처리

    #전체 맵 정보를 입력받기
    array =[]
    for i in range(n):
      array.append(list(map(int, input().split())))


    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    #def turn _left 정의
    #시뮬레이션 시작
    count=1
    turn_time =0
    while True:
        turn_left()
        nx= x+dx[direction]
        ny= y+dy[direction]
        #방문처리 리스트와 바다 육지 어레이를 동시에 체크
        if d[nx][ny] ==0 and array[nx][ny] ==0:
            d[nx][ny] =1
            x= nx
            y =ny
            count+=1
            turn_time =0
            continue
        else:
            turn_time +=1
        if turn_time ==4:
            nx = x - dx[direction]
            ny = y-dy[direction]
            if array[nx][ny] ==0:
                x= nx
                y= ny
            else:
                break
            turn_time =0
    return count



def turn_left():
    global direction
    direction -=1
    if direction ==-1:
        direction =3





if __name__ == '__main__':
    # start_1 = time.time()
    # print(travelPlan())
    # print("Time spent for my code was ", time.time()-start_1)
    # start_2 = time.time()
    # print(travelPlan2())
    # print("Time spent for my code was ", time.time()-start_2)
    #
    # print(countThree())
    print(gameDevelopment())