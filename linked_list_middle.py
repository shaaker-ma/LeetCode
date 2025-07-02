
class ListNode:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next
    
    def print(head):
        current_node = head
        while current_node:
            print(current_node.val)
            current_node = current_node.next
        
    def middle_node(head):
        count = 0
        current_node = head
        while current_node:
            current_node = current_node.next
            count+=1
        middle = count//2
        current_node = head
        res = []
        for i in range(middle):
            current_node = current_node.next
        while current_node:
            res.append(current_node.val)
            current_node = current_node.next
        return res
    
    def middle_node_optimized(head):
        one_step = head
        two_steps = head
        while two_steps or two_steps.next:
            one_step = one_step.next
            two_steps = two_steps.next.next
        return one_step


dum5 = ListNode(5)
dum4 = ListNode(4, dum5)
dum3 = ListNode(3, dum4)
dum2 = ListNode(2, dum3)
head = ListNode(1, dum2)

head.print()
print(head.middle_node())