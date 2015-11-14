def RemoveDuplicates(head):
    current = head
    if head == None:
        return
    temp = current.next
    while current != None and temp != None:
        if current.data == temp.data:
            current.next = temp.next
            temp = temp.next
        else:
            current = current.next
            temp = temp.next
    while head != None:
        return head
