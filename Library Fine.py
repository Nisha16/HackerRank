Actual_Date = list(map(int,raw_input().split(' ')))
Expected_Date = list(map(int,raw_input().split(' ')))
if Actual_Date[0] - Expected_Date[0] > 0 and Actual_Date[1] - Expected_Date[1] == 0 and Actual_Date[2] - Expected_Date[2] == 0:
                     print 15 * (Actual_Date[0] - Expected_Date[0])
elif Actual_Date[1] - Expected_Date[1] > 0 and Actual_Date[2] - Expected_Date[2] == 0:
                     print 500 * (Actual_Date[1] - Expected_Date[1])
else:
                     print 10000
