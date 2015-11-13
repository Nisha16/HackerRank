def GetNode(head, position):
    current = head
    temp = head
    count = 0
    while current != None:
        current = current.next
        count += 1
    print "count:", count

    for i in range(count - position - 1):
        temp = temp.next
    return temp.data
