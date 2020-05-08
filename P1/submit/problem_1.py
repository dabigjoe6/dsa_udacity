class Node:    
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
    def __repr__(self):
        return str(self.key) + " " + str(self.value)
        
class DoublyLinkedList:
    
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
        
    def add(self, new_node):
        new_node.next = self.head.next
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next.prev = new_node
    
    def remove(self, node):
        next_node = node.next
        prev_node = node.prev
        next_node.prev = prev_node
        prev_node.next = next_node
        node.next = None
        node.prev = None
        
    def getLastNode(self):
        return self.tail.prev
    
    def getKey(self, node):
        return node.key

class LRUCache:

    def __init__(self, capacity):
        self.linkedlist = DoublyLinkedList()
        self.capacity = capacity
        self.node_map = {}
        

    def get(self, key):
        result = -1
        node = self.node_map.get(key)
        if node:
            result = node.value
            self.linkedlist.remove(node)
            self.linkedlist.add(node)
        return result
    
        

    def put(self, key, value):
        node = self.node_map.get(key)
        if node:
            self.linkedlist.remove(node)
            node.value = value
            self.linkedlist.add(node)
        else:
            if len(self.node_map) == self.capacity:
                del self.node_map[self.linkedlist.getKey(self.linkedlist.getLastNode())]
                self.linkedlist.remove(self.linkedlist.getLastNode())
                
            new_node = Node(key, value)
            self.node_map[key] = new_node
            self.linkedlist.add(new_node)


our_cache = LRUCache(5)

print(our_cache.put(1, 1))
print(our_cache.put(2, 2))
print(our_cache.put(3, 3))
print(our_cache.put(4, 4))


print(our_cache.get(1))    # returns 1
print(our_cache.get(2))    # returns 2
print(our_cache.get(9))   # returns -1 because 9 is not present in the cache

print(our_cache.put(5, 5)) 
print(our_cache.put(6, 6))

print(our_cache.get(3)) 