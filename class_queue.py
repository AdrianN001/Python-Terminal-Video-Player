class Queue:
    def __init__(self): 
        
        self.storage = []
    
    def push(self, value) -> None:
        self.storage.append(value)
    
    def get(self) -> int:
        try:
            value = self.storage[0]
            self.storage.pop(0)
            return value
        except IndexError:
            return -1