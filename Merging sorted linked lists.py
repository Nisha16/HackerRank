def MergeLists(headA, headB):
    if headA is None:
        return headB
    if headB is None:
        return headA

    # create dummy node to avoid additional checks in loop
    start = tail = Node() 
    while not (headA is None or headB is None):
        if headA.data < headB.data:
            # remember current low-node
            current = headA
            # follow ->next
            headA = headA.next
        else:
            # remember current low-node
            current = headB
            # follow ->next
            headB = headB.next

        # only mutate the node AFTER we have followed ->next
        tail.next = current          
        # and make sure we also advance the temp
        tail = tail.next

    tail.next = headA or headB

    # return tail of dummy node
    return start.next
