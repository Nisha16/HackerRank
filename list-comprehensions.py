A,B,C,N = int(raw_input()), int(raw_input()), int(raw_input()), int(raw_input())
print [[x,y,z] for x in range(0,A+1) for y in range(0,B+1) for z in range(0,C+1) if x+y+z != N]
