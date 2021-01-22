'''
3 10 50 60 100 100 200 300
45 50 600 600 400 450 500 543
11 120 120 230 50 40 60 440
35 56 67 90 67 80 500 600
'''

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    # print(x1, y1, p1, q1, x2, y2, p2, q2)

    result = 'a'
    if x1 > p2 or q1 < y2 or p1 < x2 or y1 > q2:
        result = 'd'
    elif x1 == p2:      # 윗변 겹칠 때
        if q1 == y2:
            result = 'c'
        else:
            result = 'b'
    elif q1 == y2:      # 오른쪽변 겹칠 때
        if p1 == x2:
            result = 'c'
        else:
            result = 'b'
    elif p1 == x2:      # 아랫변 겹칠 때
        if y1 == q2:
            result = 'c'
        else:
            result = 'b'
    elif y1 == q2:      # 왼쪽변 겹칠 때
        if x1 == p2:
            result = 'c'
        else:
            result = 'b'

    print(result)