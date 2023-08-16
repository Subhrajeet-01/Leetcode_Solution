class MyHashSet(object):

    def __init__(self):
        self.arr = set()
        

    def add(self,key):
        self.arr.add(key)
        
    def remove(self, key):

        self.arr.discard(key)

    def contains(self, key):

        if key in self.arr:
            return True 
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)