import sys

if __name__ == '__main__':
    input_num = sys.stdin.readline().strip()
    n = int(input_num)
    count = 9  # 个位数可以且肯定可以到达9个数
    flag = 0
    while n // 10:
        digit = n % 10
        count += (10 - digit - flag)
        flag = 1
        n = n // 10
        if n == 9:
            count -= 1


    print(count)
