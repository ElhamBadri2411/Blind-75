class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
    

    def get(self, key: str, timestamp: int) -> str:
        #Binary Search
        
        values = self.store.get(key, [])
        if not values:
            return ""
        if timestamp >= values[-1][1]:
            return values[-1][0]
        if timestamp < values[0][1]:
            return ""
        
        
        l, r = 0, len(values) - 1
        print (values)
        while l < r:
            m = l + r // 2
            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] < timestamp:
                l = m + 1
            else:
                r = m - 1
                
        return values[l - 1][0]
                
            
            
        
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)