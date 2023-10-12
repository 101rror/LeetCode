#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        p, q = 0, mountain_arr.length() - 1

        while(p < q):
            m = (p + q) // 2
            if(mountain_arr.get(m) < mountain_arr.get(m + 1)):
                p = m + 1
            else:
                q = m

        peak = p

        if(mountain_arr.get(peak) == target):
            return peak
        if(mountain_arr.get(peak) < target):
            return -1

        l, r = 0, peak
        while(l <= r):
            mid = (l + r) // 2

            if(mountain_arr.get(mid) < target):
                l = mid + 1
            elif(mountain_arr.get(mid) > target):
                r = mid - 1
            else:
                return mid

        l, r = peak, mountain_arr.length() - 1

        while(l <= r):
            mid = (l + r) // 2

            if(mountain_arr.get(mid) > target):
                l = mid + 1
            elif(mountain_arr.get(mid) < target):
                r = mid - 1
            else:
                return mid

        return -1