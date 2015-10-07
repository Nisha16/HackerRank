N = int(raw_input())
array = list(map(int,raw_input().split(' ')))
negative = 0
positive = 0
zeros = 0
for i in range(N):
    if array[i] < 0:
        negative += 1        
    elif array[i] > 0:
        positive += 1
    else:
        zeros += 1
print '%.6f' % (positive/float(N))
print '%.6f' % (negative/float(N))
print '%.6f' % (zeros/float(N))
