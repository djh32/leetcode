# coding=utf-8
'''
"一亿一千一百零一万一千一百零一"
返回 1 1101 1101

难点， 用亿 和  万 作为区分， 这道题不能超过 万亿 只能是 千亿 开始， 万亿就有问题了
难点是 0 怎么解释
'''


# note 状态机, 数字digit后面能是end，是unit 普通unit进行组合，万亿unit进行hold之后处理。 零就pass 0后面只能是数字digit unit后面可以是end,数字,0

def chinese_to_digits(chinese_info):
    chinese_digits = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}
    chinese_units = {'十': 10, '百': 100, '千': 1000, }
    chinese_upgrade_units = {'万': 10000, '亿': 100000000}

    final_res = 0
    res = 0
    i = 0
    end_i = len(chinese_info)
    while i < len(chinese_info):
        c_s = chinese_info[i]
        if c_s in chinese_digits:
            num = chinese_digits.get(c_s)
            if i + 1 == end_i or chinese_info[i + 1] in chinese_upgrade_units:  # 最后 or 万 亿
                res += num
                i += 1
                continue
            else:
                c_s_nxt = chinese_info[i + 1]  # 百
                num *= chinese_units.get(c_s_nxt)
                res += num
            i += 2
        elif c_s in chinese_upgrade_units:
            num = chinese_upgrade_units.get(c_s)
            final_res += res * num
            res = 0
            i += 1
        elif c_s == "零":
            i += 1
    return final_res + res


print(chinese_to_digits("八千九百万零三千一百零九"))
print(chinese_to_digits("一亿三百万零七千"))
