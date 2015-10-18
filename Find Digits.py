from collections import Counter
N = int(raw_input())
for _ in range(N):
    string = raw_input()
    #print 'string:' , string
    count = Counter(string)
    #print 'count:', count
    num = int(''.join(string))
    #print 'num:', num
    D = dict(count)
    #print 'dict:', D
    result = 0
    for k in D:
        if int(k) != 0 and num % int(k) == 0:
            #print 'D[k]:', D[k]
            result += int(D[k])
    print result
