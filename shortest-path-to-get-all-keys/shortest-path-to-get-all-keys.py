class Solution:
	def shortestPathAllKeys(self, grid: List[str]) -> int:

		keys = ['a','b','c','d','e','f']

		start , total_keys = [] , 0

		for i in range(len(grid)):
			for j in range(len(grid[0])):

				if grid[i][j] == '@':
					start = [i , j]

				if grid[i][j] in keys:
					total_keys = total_keys + 1

		queue = [(start[0] , start[1] , tuple() , 0)]

		directions = [(0, 1) , (0, -1) , (1, 0) , (-1, 0)]

		visited = set()

		while queue:

			x , y , current_keys, moves = queue.pop(0)

			if (x , y , current_keys) not in visited:

				visited.add((x , y , current_keys))

				if len(set(current_keys)) == total_keys:
					return moves

				for direction in directions:

					next_keys = set(current_keys)

					next_x , next_y = x + direction[0] , y + direction[1]

					if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and grid[next_x][next_y] != '#':

						if grid[next_x][next_y] in 'ABCDEF' and grid[next_x][next_y].lower() not in next_keys:
							continue

						if grid[next_x][next_y].islower() and grid[next_x][next_y] != '.':
							next_keys.add(grid[next_x][next_y])

						queue.append((next_x , next_y, tuple(next_keys) , moves + 1))

		return -1