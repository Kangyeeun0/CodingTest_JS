from collections import deque

def bfs(maps, start, target):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]

    q = deque()
    q.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y, dist = q.popleft()

        if maps[x][y] == target:
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < n
                and 0 <= ny < m
                and not visited[nx][ny]
                and maps[nx][ny] != 'X'
            ):
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))

    return -1


def solution(maps):
    start = lever = end = None

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)

    # S -> L
    dist1 = bfs(maps, start, 'L')
    if dist1 == -1:
        return -1

    # L -> E
    dist2 = bfs(maps, lever, 'E')
    if dist2 == -1:
        return -1

    return dist1 + dist2