"""
题库：前n个回文素数
【问题描述】输入一个正整数n，输出前n个既是回文又是素数的数，要求每行输出10个数并以空格隔开
         回文素数：一种既是回文数又是素数的数字
        “回文数“是指正读反读都一样的数字，
【输入形式】一个正整数
【输出形式】每行输出10个回文素数，每个数占据6个字宽（即：以{:6}的方式输出）。
【样例输入】3
【样例输出】2 3 5
【样例输入】13
【样例输出】
    2     3     5     7    11   101   131   151   181   191
  313   353   373
"""

# 判断一个数是否是素数
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 判断一个数是否是回文数
def is_palindrome(num):
    return str(num) == str(num)[::-1]

def main():
    n = int(input())
    count = 0
    num = 2
    while count < n:
        if is_prime(num) and is_palindrome(num):
            print("{:6}".format(num), end=' ')
            count += 1
            if count % 10 == 0:  # 每行输出10个数
                print()  # 输出换行符
        num += 1

# 调用主函数
if __name__ == "__main__":
    main()
