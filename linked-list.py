class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class linkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def print_ll(self):
        if self.head is None:
            return "Linked list is empty"
        
        linked_list_str = ""
        while self.head:
            linked_list_str += self.head.data + "-->"
            self.head= self.head.next
        return linked_list_str

ll = linkedList()
ll.insert_at_begining("84")
ll.insert_at_begining("9")
ll.insert_at_begining("0")
print(ll.print_ll())