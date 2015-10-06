string = raw_input()
sub_string = raw_input()
i=0
while string.find(sub_string)>-1:
   string=string[string.find(sub_string)+1:]
   i+=1
print i
