func maxIceCream(costs []int, coins int) int {
	maxCost := 0

	for _, cost := range costs {
		if cost > maxCost {
			maxCost = cost
		}
	}

	freq := make([]int, maxCost+1)

	for _, cost := range costs {
		freq[cost]++
	}

	ans := 0

	for cost := 1; cost <= maxCost; cost++ {
		if freq[cost] == 0 {
			continue
		}

		canBuy := freq[cost]
		if coins/cost < canBuy {
			canBuy = coins / cost
		}

		ans += canBuy
		coins -= canBuy * cost

		if coins < cost {
			break
		}
	}

	return ans
}