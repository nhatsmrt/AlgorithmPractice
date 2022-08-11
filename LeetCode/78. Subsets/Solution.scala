object Solution {
    // Time and Space Complexity: O(2^n)
    // Immutability changes EVERYTHING!

    def subsets(nums: Array[Int]): List[List[Int]] =
        backtrack(nums, 0, Nil, Nil)

    def backtrack(nums: Array[Int], cur: Int, partial: List[Int], ret: List[List[Int]]): List[List[Int]] = {
        if (cur == nums.length) {
           partial :: ret
        } else {
            val left = backtrack(nums, cur + 1, partial, ret)
            backtrack(nums, cur + 1, nums(cur) :: partial, left)
        }
    }
}
