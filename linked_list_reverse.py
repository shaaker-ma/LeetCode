class ListNode:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next
    
    def reverse(self, head):
        prev_node = None
        current_node = head
        while current_node:
            dummy = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = dummy
        return prev_node
    
    
# usage example
dum5 = ListNode(5)
dum4 = ListNode(4, dum5)
dum3 = ListNode(3, dum4)
dum2 = ListNode(2, dum3)
head = ListNode(1, dum2)
reversed_head = head.reverse(head)

# Function to print the linked list
def print_list(head):
    current_node = head
    while current_node:
        print(current_node.val, end=" -> ")
        current_node = current_node.next
    print("None")
print_list(reversed_head)