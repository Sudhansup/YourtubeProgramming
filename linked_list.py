class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_linked_list(num:int):
    firstNode = None

    prevnode = firstNode
    while num > 0:
        r = num %10
        x  = ListNode(r,None)
        if prevnode is not None:
            prevnode.next = x 
        else:
             prevnode = x
        num = int(num/10)        
    return firstNode

def traverse_and_print(firstNode:ListNode):
    data = 0
    strdata = ''
    currentNode = firstNode
    while currentNode is  not None:
        data = data*10 + currentNode.val
        strdata = strdata + "=>" + str(currentNode.val)

        currentNode = currentNode.next
    print(data, strdata)
    return data


traverse_and_print(get_linked_list(243))
        





