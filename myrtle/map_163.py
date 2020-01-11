import sys
import math


def init_g(n, m, g0, x, y, z):
    res = [None] * (n * m + 1)
    res[0] = g0  # 为了计算方便
    for i in range(1, n * m + 1):
        res[i] = (res[i-1] * x + y) % z
    return res


# init map and fill height
def init_map(n, m, g0, x, y, z):
    g_values = init_g(n, m, g0, x, y, z)
    res = [None] * n
    for i in range(1, n+1):
        col = [None] * m
        for j in range(1, m+1):
            index = (i-1)*m+j-1
            col[j-1] = g_values[index]

        res[i-1] = col
    return res


# find lowest in block
def find_lowest_in_block(map_dict, init_x, init_y, b, a):
    rows = map_dict[init_x: (init_x+b)]
    lowest = math.inf
    for col in rows:
        col_min = min(col[init_y:(init_y+a)])
        if col_min < lowest:
            lowest = col_min
    return lowest


if __name__ == '__main__':
    map_params = sys.stdin.readline().split()
    n, m, a, b = [int(x) for x in map_params]
    fun_params = sys.stdin.readline().split()
    g0, x, y, z = [int(x) for x in fun_params]

    height = init_map(n, m, g0, x, y, z)

    init_x = 0
    init_y = 0
    s = 0
    while (init_x + b) <= m:
        init_y = 0
        while (init_y + a) <= n:
            block_min = find_lowest_in_block(height, init_x, init_y, b, a)
            s += block_min
            print(f'({init_x}, {init_y}: min {block_min})')
            init_y += 1
        init_x += 1

    print(s)

