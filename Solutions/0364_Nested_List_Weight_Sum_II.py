# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        if not nestedList:
            return 0
        
        num_list = []
        depth_list = []
        def helper(_nestedInteger, _depth):
            nonlocal num_list, depth_list
            if _nestedInteger.isInteger():
                val = _nestedInteger.getInteger()
                num_list.append(val)
                depth_list.append(_depth)
                return
            elif not _nestedInteger.getList():
                num_list.append(0)
                depth_list.append(_depth)
            
            for each_nestedInteger in _nestedInteger.getList():
                helper(each_nestedInteger, _depth + 1)
            
        for each_nestedList in nestedList:
            helper(each_nestedList, 1)
        
        if not num_list:
            return 0
        
        max_depth = max(depth_list)
        for index in range(len(depth_list)):
            depth_list[index] = max_depth - depth_list[index] + 1
        
        sol = 0
        
        for num, depth in zip(num_list, depth_list):
            sol += num * depth
            
        return sol