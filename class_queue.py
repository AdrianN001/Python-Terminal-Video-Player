class Queue:
    def __init__(self): 
        
        self.storage = []
    
    def push(self, value) -> None:
        self.storage.append(value)
    
    def get(self) -> tuple[any, bool]:
        try:
            value = self.storage[0]
            self.storage.pop(0)
            return value, True
        except IndexError:
            return [], False
    
    def length(self) -> int:
        return len(self.storage)