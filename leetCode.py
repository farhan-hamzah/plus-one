nums = list(map(int, input().split()))
hasil = []
for i in range(len(nums)):
    if nums[i] == nums[-1]:
        hasil.append(nums[i]+1)
    else:
        hasil.append(nums[i])
print(hasil)
