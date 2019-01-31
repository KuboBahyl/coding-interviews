# Linked List - check length
def linked_list_length(linkedList):
    temp_node = linkedList.head
    counter = 0
    while temp_node:
        temp_node = temp_node.next
        counter += 1

    return counter


linkedList = LinkedList()
linkedList.insert_list([1, 2, 3, 4, 5])
linked_list_length(linkedList)