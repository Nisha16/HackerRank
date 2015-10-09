Test_case = int(raw_input())
for x in range(Test_case):
    N,K = (raw_input().split(' '))
    Time = list(map(int,raw_input().split(' ')))
    count = 0
    for i in range(int(N)):
        if Time[i] <= 0:
            count += 1
        else:
            pass
    if (count >= int(K)):
        print 'NO'
    else:
        print 'YES'
