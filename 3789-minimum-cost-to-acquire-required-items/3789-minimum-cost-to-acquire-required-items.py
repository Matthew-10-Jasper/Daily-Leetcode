class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):

        common = min(need1, need2)

        return min(
            cost1 * need1 + cost2 * need2,
            common * costBoth +
            (need1 - common) * cost1 +
            (need2 - common) * cost2,
            max(need1, need2) * costBoth
        )