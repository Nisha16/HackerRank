input = int(raw_input())
L = []
for input in range(input):
    args = raw_input().strip().split(' ')
    if args[0] == 'print':
        print L
    elif len(args) == 3:
        getattr(L,args[0])(int(args[1]), int(args[2]))
    elif len(args) == 2: 
        getattr(L,args[0])(int(args[1]))
    else:
        getattr(L,args[0])()
