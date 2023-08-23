# Queue
# 큐의 연산 과정

from collections import deque
q = deque()
# deque와 그 메서드인 append(), leftpop() 사용

queue2 = []
# append(), pop() 사용
# queue2.append(1)
# queue2.append(2)
# queue2.append(3)
# print(queue2.pop(0))
# print(queue2.pop(0))
# print(queue2.pop(0))


# front, rear 등 인덱스 변수 사용
queue = [0]*100
front = -1
rear = -1


#enQueue(a)
rear += 1
queue[rear] = 'a'
rear += 1
queue[rear] = 'b'
# print(queue)

#deQueue(a)
front += 1
temp = queue[front]
queue[front] = 0

#enQueue(c) : 큐에 새로운 원소를 삽입
rear += 1  # 새로운 원소를 삽입할 자리
queue[rear] = 'c'  # 그 위치에 해당 원소 저장
# print(queue)

#deQueue(b), deQueue(c)
front += 1  #
queue[front] = 0
front += 1
queue[front] = 0
# print(queue)
# print(front, rear)  # front, rear가 같아짐(큐가 빈 상태)


#
def enq(data):
    global rear
    if rear == qsize - 1:  # 큐가 다 찬 경우
        print('q is full')
    else:
        rear += 1
        q[rear] = data


def deq():
    global front
    if front == rear:
        is_empty()
    else:
        front += 1
        return q[front]


def is_empty():
    return front == rear

qsize = 3
q = [0] * 3
rear = -1
front = -1
# enq(1)
# enq(2)
# enq(3)


while front != rear:  # 큐가 비어있지 않으면
    front += 1
    print(q[front])

# 연습문제2
# 엔터를 칠 때마다 큐에 있는 사람 수, 현재 일인당 나눠주는 사탕의 수, 현재까지 나눠준 사탕의 수를 출력

