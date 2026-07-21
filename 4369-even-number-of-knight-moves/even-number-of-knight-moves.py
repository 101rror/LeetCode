class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        srt = (start[0] + start[1]) % 2
        tar = (target[0] + target[1]) % 2

        return srt == tar
