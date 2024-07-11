class box:
    def __init__(self,data):
        self.data = data
        self.next = None

obj1 = box(51)
obj2 = box(52)
obj3 = box(53)
obj4 = box(54)
obj5 = box(55)
obj6 = box(56)
obj7 = box(57)
obj8 = box(58)
obj9 = box(59)
obj10 = box(60)


obj1.next = obj2
obj2.next = obj3
obj3.next = obj4
obj4.next = obj5
obj5.next = obj6
obj6.next = obj7
obj7.next = obj8
obj8.next = obj9
obj9.next = obj10
obj10.next = None
#print(print_linked_list(obj1))


#print function

def print_linked_list(curr):
    while curr != None:
        print(curr.data, end = "->")
        curr =curr.next

# Insert  at tailnode

def insertAtTailNode(head,ele):
    temp = box(ele)
    if head == None:
        return temp
    tail = head

    while tail.next != None:
        tail = tail.next
    tail.next = temp
    return head


#insert at beginning

def insertAtBeginning(head,ele):
    temp = box(ele)
    if head == None:
        return temp
    temp.next = head
    return temp 

def insertAtSpecificPosition(head, position, ele):
    if position == 0:
        return insertAtBeginning(head,ele)
    
    temp = box(ele)
    currentIndex = 0
    currentNode = head

    while currentIndex != position-1:
        currentIndex +=1
        currentNode = currentNode.next
    temp.next  =  currentNode.next
    currentNode.next = temp
    return head 
head = obj1
head = insertAtSpecificPosition(head,5,10)
print(print_linked_list(head))

#Tailnode execution
# head = None
# for ele in range(1,100):
#     head = insertAtTailNode(head,ele)
#print(print_linked_list(head))


#beginningnode execution
# head = None
# for ele in range(1,10):
#     head = insertAtBeginning(head , ele)
# print(print_linked_list(head))

def deletetailnode(head):
    curr = head
    if curr == None or curr.next == None:
        return None
    while curr.next.next != None:
        curr = curr.next
    curr.next = None
    return head
# head = obj1
# head = deletetailnode(head)
# print(print_linked_list(head))

def deleteheadnode(head):
    if head == None:
        return None
    secondNode = head.next
    head.next = None
    return secondNode
head = obj1
head = deleteheadnode(obj1)
print(print_linked_list(head))


















        
