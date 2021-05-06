class IndexSelector(cq.Selector):
    def __init__(self, *indexes):
        self.indexes = indexes

    def filter(self, objectList):
        r = []
        for i in self.indexes:
            r.append(objectList[i - 1])
        return r
