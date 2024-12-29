# coding=utf-8
'''
输出给定数字下一个比它大的数字，比如输入：1234， 输出 1243。输入：12432，输出13224

31原题
https://www.nowcoder.com/discuss/353157765025701888

纯背记忆的题

'''
# note 31原题

def solution(nums):
    length = len(nums)
    l, r = length - 2, length - 1

    # 找到升序序列
    while l >= 0 and nums[l] >= nums[r]: #
        l -= 1
        r -= 1

    if l >= 0:
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
