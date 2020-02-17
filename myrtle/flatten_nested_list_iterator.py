# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


def flatten(nestedList):
    for n in nestedList:
        if n.isInterger:
            yield n.getInteger()
        else:
            yield from flatten(n.getList())


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = list(flatten(nestedList))
        self.pos = 0

    def next(self) -> int:
        res = self.list[self.pos]
        self.pos += 1
        return res

    def hasNext(self) -> bool:
        return self.pos < len(self.list)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
