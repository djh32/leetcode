# coding=utf-8
'''
用二分法在排序数组中找到绝对值最小的元素
[-54, -12, -6, -1, 1, 2, 3, 4, 6, 24]
'''
# note 不是原题
def find_abs_min(arr): # chatgpt解法
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if abs(arr[mid]) < abs(arr[mid + 1]):
            right = mid
        elif abs(arr[mid]) > abs(arr[mid + 1]):
            left = mid + 1
        else:
            return arr[mid]

    return arr[left]

# 示例输入
arr = [-10, -5, -2, 0, 3, 6, 9]
result = find_abs_min(arr)
print(result)


def abs_min_find(list):
    l,r = 0,len(list)-1
    tmp_result = float("inf")
    while l<r:
        m = l+(r-l)//2
        if abs(list[m]) < tmp_result:
            tmp_result = abs(list[m])
            r = m
        elif abs(list[m]) >= tmp_result:
            l = m+1
    return list[l]

st_list = [-54, -12, -6, -1,0, 1, 2, 3, 4, 6, 24]
st_list = [-2,-1,2]

print(abs_min_find(st_list))




