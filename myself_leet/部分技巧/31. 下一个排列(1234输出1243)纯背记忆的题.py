# coding=utf-8
'''
输出给定数字下一个比它大的数字，比如输入：1234， 输出 1243。输入：12432，输出13224
31原题
纯背记忆的题

'''


def solution(nums):
    length = len(nums)
    l, r = length - 2, length - 1

    # 找到升序序列
    while l >= 0 and nums[l] >= nums[r]: # 这里需要有 nums[l] >= nums[r] 否则无法判断[5,1,1] 这种结果
        l -= 1
        r -= 1

    if l >= 0:  # 如果<=0 的时候说明序列整体是降序， 只需要转换即可找到最小的 4321 => 1234
        # 从后往前找到第一个比L大的数字，进行交换， 找到的是“大的里面最小的”
        for i in range(r, length)[::-1]:
            if nums[i] > nums[l]:
                nums[i], nums[l] = nums[l], nums[i]
                break
    # 此时从 r 到 length 严格递减， 这里reverse就行
    l, r = r, length - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    return nums


print(solution([5, 1, 1]))
