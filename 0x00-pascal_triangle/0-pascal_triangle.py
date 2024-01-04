'''Pascal's triangle'''


def pascal_triangle(n):
    '''Returns a list of lists of integers representing Pascals triangle of n'''
    if n <= 0:
        return []

    tri = [[1]]

    for _ in range(1, n):
        pre = tri[-1]
        cur = [pre[0]]

        for i in range(1, len(pre)):
            cur.append(pre[i - 1] + pre[i])

        cur.append(pre[-1])
        tri.append(cur)

    return tri
