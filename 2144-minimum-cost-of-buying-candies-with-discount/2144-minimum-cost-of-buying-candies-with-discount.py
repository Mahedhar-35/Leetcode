class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost=sorted(cost)
        cost=cost[::-1]
        return sum(cost) - sum(cost[2::3])        