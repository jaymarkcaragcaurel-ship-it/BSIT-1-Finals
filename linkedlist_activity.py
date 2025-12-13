
class CreateNode:
    
    def __init__(self, data):
        self.data = data
        self.next_linked_node = None


class CreateLinkedList:

    def __init__(self):
        self.Head = None
    
    def insert_to_end(self, data):
        new_node = CreateNode(data)

        if self.Head == None:
            self.Head = new_node
            return
        
        current_node = self.Head
        while current_node.next_linked_node != None:
            current_node = current_node.next_linked_node
        
        current_node.next_linked_node = new_node

    #Task 2
    def delete_node(self, key):
        CurrentNode = self.Head
        PreviousNode = None

        if CurrentNode == None: return

        if CurrentNode.data == key:
            self.Head = CurrentNode.next_linked_node
            return
        
        while CurrentNode != None:

            if CurrentNode.data == key:
                print("Found the node, now deleting...")
                PreviousNode.next_linked_node = CurrentNode.next_linked_node
                return
            
            PreviousNode = CurrentNode
            CurrentNode = CurrentNode.next_linked_node

    #Task 3
    def traverse(self):
        CurrentNode = self.Head

        while CurrentNode != None:
            print(CurrentNode.data, end=" -> ")
            CurrentNode = CurrentNode.next_linked_node

        print("None")

LinkedList = CreateLinkedList()

print("Inserting values: 10, 20, 30, 40")
LinkedList.insert_to_end(10)
LinkedList.insert_to_end(20)
LinkedList.insert_to_end(30)
LinkedList.insert_to_end(40)

print("Current LinkedList:")
LinkedList.traverse()

print(" ")
print("Deleting 20...")
LinkedList.delete_node(20)

print(" ")
print("Current LinkedList...")
LinkedList.traverse()
