# 원형 큐
# (rear + 1) mod n을 인덱스로 사용 - 데이터를 저장하려는 위치
# front가 가리키는 자리는 항상 비워놓음
# (rear + 1) mod n == front : 원형 큐가 가득찬 상태
# front == rear : 공백상태

def enq(data):
    global rear, front
    if (rear + 1) % qsize == front:
        print('q is full')
        front = (front+1) % qsize
        cq[(rear + 1) % qsize] = data
        # front를 한 칸 밀고(front가 옮겨갈 자리에 있는 데이터는 가장 오래 전 데이터이므로 버림) 그 자리에 새로운 데이터를 저장
    rear = (rear+1) % qsize
    cq[rear] = data

def deq():
    global front
    if front == rear:
        print('q is empty')
    front = (front+1) % qsize
    return cq[front]

cq = [0] * 4
qsize = 4
front = 0
rear = 0
enq(1)
enq(2)
enq(3)
print(cq, front)
enq(4)
# enq(5)
# enq(6)

print(cq, front)
