
func sortArrayByParity(nums []int) []int {
    evenPos := 0
    i :=0

    n := len(nums)
    for i<n {
        if nums[i]&1==0 {
            nums[i], nums[evenPos] = nums[evenPos], nums[i]
            evenPos+=1
            fmt.Println("true")
        }
        i+=1
    }
    return nums;
}