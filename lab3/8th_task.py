def spy_game(nums):
    list=[]
    for x in nums:
        if x == 0 or x == 7:
            list.append(x)
    if list[0] == list[1] == 0 and list[2] == 7:
        return True
    else:
        return False
     
n = int(input())
nums = []
for i in range(n):
    m = int(input())
    nums.append(m)
print(spy_game(nums))