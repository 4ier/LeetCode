class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        factorValue = []
    	factorValue[0] = [equations[0][0], 1]
    	factorValue[1] = [equations[0][1], 1 / values[x]]
        for x in xrange(0,len(equations):
        	factorValue[0] = [equations[x][0], 1]
        	factorValue[1] = [equations[x][1], 1 / values[x]]

        