class Node:
    def __init__(self, key=int, value=int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity=int):
        self.capacity = capacity
        self.size = 0
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
        self.misses=0
        self.hits=0

    def add_value(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev    

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_value(node)

    def evict_from_tail(self):
        lru = self.tail.prev  # least recently used
        self.remove_node(lru)
        del self.cache[lru.key]
        return lru

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_to_head(node)
            self.hits+=1
            return node.value
        else:
            self.misses+=1
        return -1  # If key is not found
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
            self.hits+=1
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.add_value(new_node)
            self.size += 1
            self.misses+=1


            if self.size > self.capacity:
                self.evict_from_tail()
                self.size -= 1
    
    def missrate(self):
        total=self.hits+self.misses
        if total==0:
            return None
        else:
            return (self.misses/total)*100


# Initialize the cache with a capacity of 50
cache = LRUCache(50)
# cache.put(1,1)
# cache.put(2,2)
# cache.put(3,3)
# cache.get(2)
# print(cache.missrate())
# print(cache.cache.keys())

#Situation 1: Filling the cache with keys 0 to 49 (100% miss rate)

for i in range(50):
    cache.put(i, i)  # Fill the cache

print("\nThe Total Hits are:", 0)
print("The total misses are:", 50)
print("Cache Keys:", cache.cache.keys())

# Situation 2: Accessing keys alternately between odd (hits) and even (misses)

for i in range(100):
    if i%2!=0:
        cache.get(i)


print("\nThe Total Hits are:", cache.hits)
print("The Total Misses are:", cache.misses)
print("Cache Keys:", cache.cache.keys())
print()

# Situation 3: Inserting prime numbers from 0 to 100 (40% miss rate)
for i in range(100):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        cache.put(i,i)
print("\nThe Total Hits are:", cache.hits)
print("The Total Misses are:", cache.misses)
print("Cache Keys:", cache.cache.keys())
print()

# Final missrate
print("Final Miss rate:", cache.missrate())

