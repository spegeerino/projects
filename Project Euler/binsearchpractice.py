nums = list(range(10))
#want largest value of nums such that n^2 < 10
limit = 41
left = 0
right = len(nums)
while right >= left:
    mid = (left + right) // 2
    checksum = nums[mid] ** 2
    if checksum == limit:
        left = mid+1
        right = mid-1
    elif checksum > limit:
        right = mid - 1
    else:
        left = mid + 1
#left should store ans?
print("index:" + str(left-1))

    
#[0,1,2,3,4,5,6,7,8,9] left = 0, right = 10, mid = 5: search for 3, we're to the right, so we cut off right half (and one we just checked)
#[0,1,2,3] left = 0. right = 4, mid = 2; search for 3, we're to the left, so we cut off left half (but keep one we just checked):
#[2,3] left = 2, right = 4, mid = 3; we landed on 3, so we cut off left half:
#[3] left = 3, right = 4, mid = 3; we landed on 3, but nothing gets cut off

# search for 9
#[0,1,2,3,4,5,6,7,8,9] left = 0, right = 10, mid = 5; to the left, cut off left:
#[5,6,7,8,9] left = 5, right = 10, mid = 7; to the left, cut off left
#[7,8,9] left = 7, right = 10, mid = 8; to the left, cut off left
#[8,9] left = 8, right = 10, mid = 9; landed --> cut off left
#[9] left 9 right 10, mid 9

# search for 0
#[0,1,2,3,4,5,6,7,8,9] left = 0 right = 10 mid 5; to the right, cut right
#[0,1,2,3,4] left 0 right 4 mid 2; to the right, cut right
#[0,1] left 0 right 1; doesn't check

