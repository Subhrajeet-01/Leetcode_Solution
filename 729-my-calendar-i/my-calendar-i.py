class MyCalendar:

    def __init__(self):
        self.arr = [] 

    def book(self, start: int, end: int) -> bool:
        
        for existingStart, existingEnd in self.arr:
            if start < existingEnd and end > existingStart:
                return False

        self.arr.append((start, end))
        return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)