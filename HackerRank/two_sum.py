def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# Teste
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # [0, 1]