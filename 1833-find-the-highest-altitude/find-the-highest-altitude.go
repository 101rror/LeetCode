func largestAltitude(gain []int) int {
    pre := 0
    ans := 0

    for _, g := range gain {
        pre += g

        if pre > ans {
            ans = pre
        }
    }

    return ans
}