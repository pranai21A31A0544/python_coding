n=int(input())
nums=list(map(int, input().split()))[:n]
def insertionsort(nums):
    n= len(nums)
    lastEleIndex = 0
    for firEle in range(1, n):
        temp = nums[firEle]
        prevIndex = firEle - 1
        while prevIndex >= 0:
            if nums[prevIndex] > temp:
                nums[prevIndex + 1] = nums[prevIndex]
            else :
                break
            prevIndex -= 1
        nums[prevIndex - 1] = temp
print(insertionsort(nums))
print(nums)