class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = []
        self.flattenList(nestedList)
        
    def flattenList(self, nestedList):
        for item in nestedList:
            if(not item.isInteger()):
                self.flattenList(item.getList())
            else:
                self.queue.append(item.getInteger())
                
    def next(self) -> int:
        return self.queue.pop(0)
    
    def hasNext(self) -> bool:
         return len(self.queue) > 0