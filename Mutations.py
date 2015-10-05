input = list(raw_input())
index, char = raw_input().split(' ')
input[int(index)] = char
string = ''.join(input) 
print string
