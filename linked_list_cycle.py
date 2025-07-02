class ListNode:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next
    
    def hasCycle(self, head):
        visited = set()
        current_node = head
        no_cycles = True
        while current_node and no_cycles:
            if current_node not in visited:
                visited.add(current_node)
                current_node = current_node.next
            else:
                no_cycles = False
                return True
        return False
    
    def hasCycle_optimized(self, head):
        one_step, two_step = head, head
        while two_step and two_step.next:
            one_step = one_step.next
            two_step = two_step.next.next
            if(one_step == two_step):
                return True 
        return False
    
# Example usage
dum5 = ListNode(5)
dum4 = ListNode(4, dum5)
dum3 = ListNode(3, dum4)
dum2 = ListNode(2, dum3)
head = ListNode(1, dum2)
dum5.next = dum3  # Creating a cycle for testing
print(head.hasCycle(head))  # Should return True
print(head.hasCycle_optimized(head))  # Should return True