class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        heap = list(range(n))
        heapq.heapify(heap)

        rooms = []
        dp = [0] * n

        for start, end in meetings:
            duration = end - start

            while rooms and rooms[0][0] <= start:
                _, room = heapq.heappop(rooms)
                heapq.heappush(heap, room)

            if heap:
                room = heapq.heappop(heap)
                heapq.heappush(rooms, (end, room))
            else:
                finish, room = heapq.heappop(rooms)
                heapq.heappush(rooms, (finish + duration, room))
            
            dp[room] += 1

        return dp.index(max(dp))