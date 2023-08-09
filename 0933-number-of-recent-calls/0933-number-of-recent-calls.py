class RecentCounter(object):

    def __init__(self):
        self.array = []
        
    def ping(self, t):
        self.array.append(t)
        while self.array[0] < t-3000:
            self.array.pop(0)
        return len(self.array)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)