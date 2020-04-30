class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here

	lookup = {}

	node1 = llist_1.head
	node2 = llist_2.head

	union_list = LinkedList()

	while (node1 or node2):
		if node1:
			if not node1.value in lookup:
				lookup[node1.value] = ''
				union_list.append(node1.value)

			node1 = node1.next
		
		if node2:
			if not node2.value in lookup:
				lookup[node2.value] = ''
				union_list.append(node2.value)
			
			node2 = node2.next

	return union_list

def intersection(llist_1, llist_2):
    # Your Solution Here
	lookup_1 = {}
	lookup_2 = {}

	node1 = llist_1.head
	node2 = llist_2.head

	intersection_list = LinkedList()

	while (node1 or node2):
		if node1:
			if not node1.value in lookup_1:
				lookup_1[node1.value] = ''
			
			node1 = node1.next
		
		if node2:
			if not node2.value in lookup_2:
				lookup_2[node2.value] = ''
			
			node2 = node2.next

	for key in lookup_1:
		if key in lookup_2:
			intersection_list.append(key)

	return intersection_list

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))