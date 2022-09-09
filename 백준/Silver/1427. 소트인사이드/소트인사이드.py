nums = [int(_) for _ in input()]

nums = sorted(nums,reverse=True)
nums = [str(_) for _ in nums]
print(''.join(nums))