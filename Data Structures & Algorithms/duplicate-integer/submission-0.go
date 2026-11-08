func hasDuplicate(nums []int) bool {
    mm := make(map[int]int)
    for _, num := range(nums) {
        _, exists := mm[num]
        if exists {
            return true
        }
        mm[num] = num
    }
    return false
}
