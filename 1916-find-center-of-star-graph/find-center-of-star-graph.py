class Solution:
    def findCenter(self, e: List[List[int]]) -> int:
	    if e[0][0] == e[1][0] or e[0][0] == e[1][1]:
		    return e[0][0]

	    return e[0][1]