class Solution:
    def bestTower(
        self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        cx, cy = center
        best = -1
        check = None

        for x, y, q in towers:
            if abs(x - cx) + abs(y - cy) <= radius:
                if q > best:
                    best = q
                    check = (x, y)
                elif q == best:
                    if check is None or (x, y) < check:
                        check = (x, y)

        if check is None:
            return [-1, -1]
        return [check[0], check[1]]
