class Node:
    def __init__ (self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} 
        
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        
        

    def get(self, key: int) -> int:
        #if it doesnt exist return -1
        if key not in self.cache:
            return -1
        else:
            #get the value of the node using the cache, 
            node = self.cache[key]
            #move it to the right (most recent )
            self.remove(node)
            self.add_to_right(node)
            
            return node.val
            
            
            

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #get the node, update it, move it to the right (most recent)
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add_to_right(node)
            
        else:
            #make a node,
            node = Node(key, value)
            self.cache[key] = node
            
            #add it to the right, 
            self.add_to_right(node)
            #if its over capacity -> remove the furthest left node
            if( len(self.cache) > self.capacity):
                node = self.left.next
                key = node.key
                self.cache.pop(key)
                self.remove(node)
                
        return None   
                
        
    def add_to_right(self, node): 
        prev = self.right.prev
        node.next = self.right
        node.prev = prev
        prev.next = node
        self.right.prev = node

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        nxt.prev = prev
        prev.next = nxt
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)