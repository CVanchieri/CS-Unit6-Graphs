"""
Example 1:
0           3
|           |
1 --- 2     4

Example 2:
o           4
|           |
1 --- 2 --- 3
"""
class Solution:
    def numberOfComponents(self, n, edges):



sol = Solution()
assert sol.numberOfComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2
assert sol.numberOfComponents(5, [[[0, 1], [1, 2], [2, 3], [3, 4]]]) == 1