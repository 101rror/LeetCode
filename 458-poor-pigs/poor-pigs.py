class Solution:
    def poorPigs(self, buckets: int, a: int, b: int) -> int:
        res = (b // a) + 1

        count = math.ceil(math.log2(buckets) / math.log2(res))
        
        return count 