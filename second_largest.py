N = int(raw_input())
A = list(map(int,raw_input().strip().split(' ')))[:N]
max_num = max(A)
while max(A) == max_num:
    A.remove(max_num)
print max(A)
