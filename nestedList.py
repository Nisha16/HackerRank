NoOfStudents = int(raw_input())
marksPhysics = [[raw_input(), float(raw_input())] for i in  xrange(NoOfStudents)]           
scores = sorted({s[1] for s in marksPhysics})
result = sorted(s[0] for s in marksPhysics if s[1] == scores[1])
print '\n'.join(result)
