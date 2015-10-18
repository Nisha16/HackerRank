import math
N = int(raw_input())
for _ in range(N):
    first,second = raw_input().split(' ')
    count = 0
    for i in range(int(first),int(second)+1,1):
        #print 'first:', first
        if math.sqrt(i).is_integer():
            count += 1
    print count 
