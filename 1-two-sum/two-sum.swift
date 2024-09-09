class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var hash = [Int: Int]()
        for (index, n) in nums.enumerated() {
            if hash[target - n] != nil, let lower = hash[target - n] {
                return [lower, index]
            } else {
                hash[n] = index
            }
        }
        return []
    }
}