def encontrar_duplicadas(nums: list[int]) -> list[int]:
    return sorted([x for x in set(nums) if nums.count(x) > 1])

# Testes
print(encontrar_duplicadas([1,2,2,3,3,3]))  # [2,3]
print(encontrar_duplicadas([]))              # []
print(encontrar_duplicadas([5]))             # []