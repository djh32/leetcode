#coding = utf-8



def bin_search(nums,val):
    l,r = 0, len(nums)
    while l < r:
        mid_idx = (l+r)//2
        if val > nums[mid_idx]:
            l = mid_idx+1
        elif val < nums[mid_idx]:
            r = mid_idx
        else:
            return mid_idx
    return r-1 # r-1是精髓，能找到比val小的。 [4] val = 4-9都是0的idx ，0-3是-1的idx

def find_small_nums(given,real):
    real = [int(x) for x in real]
    mark_need_max = False
    result = []
    for idx in range(len(real)):
        find_idx = bin_search(given,real[idx])
        if find_idx == -1 or mark_need_max == True:
            #直接用最大的padding少一位
            res = [given[-1] for _ in range(len(real) - idx -1)]
            result.extend(res)
            return result
        else:
            result.append(given[find_idx])

        if given[find_idx] < real[find_idx]: # 如果第一次出现不能匹配的数据以后，后面的直接用最大的拼接就行
            mark_need_max = True

    return result


print(find_small_nums([2,w9],"529"))
#print(bin_search([4],3))
#print(bin_search([5,5,5,6],6))












