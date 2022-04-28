""" #706. Design HashMap 
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

    MyHashMap() initializes the object with an empty map.
    void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
    int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
    void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

"""
import collections
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None 


class MyHash:
    def __init__(self, key=None, value=None):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        idx = key % self.size 
        if self.table[idx].value is None:
            self.table[idx] = ListNode(key, value)
            return 

        p = self.table[idx]
        while p:
            if p.key == key:
                p.value = value 
                return 
            if p.next is None:
                break 
            p = p.next 
        p.next = ListNode(key, value)
    
    def get(self, key: int) -> int:
        idx = key % self.size

        if self.table[idx].value is None:
            return -1 

        p = self.table[idx]
        while p:
            if p.key == key:
                return p.value 
            p = p.next 
        return -1 
    
    def remove(self, key: int) -> None:
        idx = key % self.size
        
        if self.table[idx].value is None:
            return 

        p = self.table[idx]
        if p.key == key:
            self.table[idx] = ListNode() if p.next is None else p.next
            return 
        
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next 
                return 
            prev, p = p, p.next