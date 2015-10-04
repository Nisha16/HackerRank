T1 = int(raw_input())
A = set(map(int,raw_input().strip().split(' ')))
T2 = int(raw_input())
B = set(map(int,raw_input().strip().split(' ')))
newlist = list(map(int, A.difference(B).union(B.difference(A))))
newlist1 = sorted(newlist)
for i in range(len(newlist1)):
    print newlist1[i]
