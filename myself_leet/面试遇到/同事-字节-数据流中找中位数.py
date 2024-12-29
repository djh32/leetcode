# coding=utf-8
'''
删除多余空格

题目描述
实现一个函数，要求
输入："                   I         am         a         bytedancer.       "
输出："I am a bytedancer."
'''
# todo 待更新， 堆栈训练里面有原题

def remove_extra_spaces(s: str) -> str:  # gpt
    result = []
    in_space = False  # 标记当前是否在空格中

    for char in s:
        if char != ' ':
            result.append(char)  # 如果不是空格，直接添加
            in_space = False  # 进入非空格状态
        elif not in_space:  # 如果是空格且不在空格状态
            result.append(' ')  # 添加一个空格
            in_space = True  # 进入空格状态

    # 去掉开头和结尾的空格
    return ''.join(result).strip()


def remove_extra_spaces_without_strip(s: str) -> str:  # 自己写
    in_space_area = False
    res = []
    for c in s:
        if c != " ":
            res.append(c)
            in_space_area = False
        else:  # c == " "
            if in_space_area == False:
                res.append(" ")
            in_space_area = True
    if res[0] == " ": res = res[1:]
    if res[-1] == " ": res = res[:-1]
    return "".join(res)


# 示例
input_str = "      Hello      World!"
output_str = remove_extra_spaces_without_strip(input_str)
print(output_str)  # 输出: "Hello World!"
