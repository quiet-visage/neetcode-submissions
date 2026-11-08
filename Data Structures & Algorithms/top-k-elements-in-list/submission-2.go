import (
    "maps"
    "slices"
)

func topKFrequent(nums []int, k int) []int {
    freq := make(map[int]int)
    for _, n := range nums {
        freq[n] +=1
    }
    res := slices.Collect(maps.Keys(freq))
    sort.Slice(res, func(i,j int) bool {
        iF, okF := freq[res[i]]
        if !okF {
            fmt.Println("not found i ", i)
        }
        iJ, okJ := freq[res[j]]
        if !okJ {
            fmt.Println("not found j ", j)
        }
        fmt.Printf("if ij", iF, iJ)
        return  iF > iJ
    })
    return res[:k]
}
