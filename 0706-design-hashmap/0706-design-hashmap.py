class MyHashMap(object):

    def __init__(self):
        self.dict = {}
        
    def put(self, key, value):
        
        self.dict[key] = value
        
    def get(self, key):

        if key in self.dict.keys():
            return self.dict[key]
        return -1
        
    def remove(self, key):

        if key in self.dict.keys():
            del self.dict[key]
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)