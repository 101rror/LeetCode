class Solution:
    def subarraysDivByK(self, A: List[int], k: int) -> int:
        psum = 0
        sums = {0 : 1}
        count = 0

        for num in A:
            psum += num
            key = psum % k

            if key in sums:
                count += sums[key]
                sums[key] += 1
                continue
            sums[key] = 1

        return count