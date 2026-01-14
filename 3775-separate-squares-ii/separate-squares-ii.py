class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))

        events.sort()
        xs = []
        prey = events[0][0]
        total = 0
        areas = []

        def union_len(arr):
            arr.sort()
            ans = cur = 0
            end = -(10**30)
            for a, b in arr:
                if a > end:
                    ans += b - a
                    end = b
                elif b > end:
                    ans += b - end
                    end = b

            return ans

        for y, typ, x1, x2 in events:
            if y > prey and xs:
                h = y - prey
                w = union_len(xs)
                areas.append((prey, h, w))
                total += h * w
            if typ == 1:
                xs.append((x1, x2))
            else:
                xs.remove((x1, x2))
            prey = y

        half = total / 2
        acc = 0
        for y, h, w in areas:
            if acc + h * w >= half:
                return y + (half - acc) / w
            acc += h * w

        return 0.0
