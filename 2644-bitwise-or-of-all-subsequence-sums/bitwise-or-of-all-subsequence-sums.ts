function subsequenceSumOr(nums: number[]): number {
  let result = BigInt(0);
  let prefixSum = BigInt(0);

  for (const num of nums) {
    prefixSum += BigInt(num);

    result |= BigInt(num) | prefixSum;
  }

  return parseInt(result.toString());
};