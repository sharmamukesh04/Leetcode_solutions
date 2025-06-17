func moveZeroes(nums []int)  {
    zero_index := 0
    curr_index := 0

    count_nonzero := 0
    for curr_index < len(nums) {
        if nums[curr_index] != 0 {
            if curr_index != zero_index {
                nums[zero_index] = nums[curr_index]
            }
            zero_index++
            count_nonzero++
        } 
        curr_index++
    }

    end := len(nums)-1

    count_zero := end-count_nonzero+1

    for count_zero > 0 {
        nums[end] = 0
        end--
        count_zero--
    }
}

// 7 0 0 0 6

// 