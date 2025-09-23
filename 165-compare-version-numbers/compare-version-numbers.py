class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1, ver2 = version1.split("."), version2.split(".")
        x, y = len(ver1), len(ver2)
        mx = max(x, y)

        for i in range(mx):
            v1 = int(ver1[i]) if i < x else 0
            v2 = int(ver2[i]) if i < y else 0

            if v1 < v2:
                return -1
            if v1 > v2:
                return 1

        return 0
