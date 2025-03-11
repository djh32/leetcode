# coding=utf-8
from typing import List
import heapq
class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """

    def heapify(self, A):
        # write your code here
        # for i in range(len(A)):
        #     self.siftUp(A, i)

        for i in range(len(A) - 1, -1, -1):
            self.siftDown(A, i)

    def siftDown(self, A, k):

        if 2 * k + 1 >= len(A):
            return

        left, right = 2 * k + 1, 2 * k + 2

        next_idx = left

        if right < len(A) and A[right] < A[left]:
            next_idx = right

        if A[k] < A[next_idx]:
            return

        A[k], A[next_idx] = A[next_idx], A[k]
        self.siftDown(A, next_idx)

    def siftUp(self, A, k):

        if k <= 0:
            return

        parent = (k - 1) // 2
        if A[parent] >= A[k]:
            return

        A[parent], A[k] = A[k], A[parent]
        self.siftUp(A, parent)


"""
问题：
sift_up很简单是了解heap的入门。这题要是碰到了，就是要考你sift_down，所以，你要是不会写，就背，要背，就背这个最简洁的。

另外，你要能答的出为什么sift_up是O(nLogN)，而sift_down是O(N)。

另： 是sift_down，次优是sift_up。不是 shift_down， shift_up， 不是 bubble_up， 不是 percolate_up。

解答：
虽然理论上可以使用 sift_up 操作来构建堆，但实际上使用 sift_down 更为高效和常见。以下是一些原因：

效率：使用 sift_down 操作构建堆的时间复杂度为 O(N)，其中 N 是堆中的元素数量。而使用 sift_up 操作构建堆的时间复杂度为 O(NlogN)。
** 因为 sift_up 操作需要将每个元素逐个上滤到堆的合适位置，而 sift_down 操作可以通过从最后一个非叶子节点开始，逐个下滤元素，更快地构建堆。 **

实现简单：使用 sift_down 操作构建堆的实现通常更简单。sift_down 操作只需要比较和交换元素，而 sift_up 操作需要在每次上滤时比较和交换元素。因此，使用 sift_down 更容易实现和理解。

堆的性质：使用 sift_down 操作构建堆可以保证每个节点都被放置在正确的位置上，满足堆的性质。而使用 sift_up 操作构建堆可能会导致某些节点被放置在不正确的位置上，需要进行额外的操作来修复堆的性质。

综上所述，虽然可以使用 sift_up 操作来构建堆，但通常更常见和高效的做法是使用 sift_down 操作。它具有更好的时间复杂度和更简单的实现，同时可以保证堆的性质。
"""



"""题目解析： 这里最重要的是长度的判断以及index代表左右子节点的索引， 
如果需要heapify的长度是14共14元素，合法的index为[0,13],那么14//2 =7 range 从[0-6] 6*2 + 1 到13
如果需要heapify的长度是15共15元素，合法的index为[0,14],那么15//2 =7 range 从[0-6] 6*2 + 2 到14
因此里面对于右子节点需要判定是否存在,左节点则不用，因为整除一定包含左节点index表示了。 


而且sift down中,因为堆是满二叉树,所以倒数第一个非叶子节点的index 一定是 range(len(A)//2)[-1] 这个index
这是是实现细节
"""
class Solution2:

    def heapify(self, nums):

        for i in reversed(range((len(nums)) // 2)):
            self.sift_down(nums, i)

    def sift_down(self, nums, index): # 小根堆

        n = len(nums)
        while index * 2 + 1 < n:

            son_index = index * 2 + 1
            if son_index + 1 < n and nums[son_index] > nums[son_index + 1]:
                son_index = son_index + 1  # 左右子节点值小的和parent比较
            if nums[son_index] >= nums[index]:
                break
            nums[index], nums[son_index] = nums[son_index], nums[index]
            index = son_index

    def sift_down(self, nums, index): # 大根堆

        n = len(nums)
        while index * 2 + 1 < n:

            son_index = index * 2 + 1
            if son_index + 1 < n and nums[son_index] < nums[son_index + 1]:
                son_index = son_index + 1  # 左右子节点值大的和parent比较
            if nums[son_index] <= nums[index]:
                break
            nums[index], nums[son_index] = nums[son_index], nums[index]
            index = son_index

a = [1, 2, 5, 6, 2, 1, 4, 1, 2, 7, 8, 9, 10]
print(Solution2().heapify(a))
print(a)

# todo cp的别人的，看过以后自己后面实现一下。主要练习sift_down即可，因为只需要从最后一个非叶子节点考虑。