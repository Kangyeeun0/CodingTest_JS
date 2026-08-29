from collections import deque


def replace_alpha(storage, alpha, count):
    for i in range(len(storage)):
        for j in range(len(storage[0])):
            if storage[i][j] == alpha:
                storage[i][j] = '.'
                count -= 1

    return count


def fork_rain(storage, alpha, count):
    n = len(storage)
    m = len(storage[0])

    q = deque()
    remove_list = []

    visited = [[False] * m for _ in range(n)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 가장자리 검사
    for i in range(n):
        for j in range(m):

            if i == 0 or i == n - 1 or j == 0 or j == m - 1:

                if visited[i][j]:
                    continue

                # 가장자리 빈 공간이면 BFS 시작점
                if storage[i][j] == '.':
                    q.append([i, j])
                    visited[i][j] = True

                # 가장자리 target이면 제거 대상
                elif storage[i][j] == alpha:
                    remove_list.append([i, j])
                    visited[i][j] = True

    # 외부와 연결된 빈 공간 탐색
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:

                if storage[nx][ny] == '.':
                    q.append([nx, ny])
                    visited[nx][ny] = True

                elif storage[nx][ny] == alpha:
                    remove_list.append([nx, ny])
                    visited[nx][ny] = True

    # 한 번에 제거
    for x, y in remove_list:
        storage[x][y] = '.'
        count -= 1

    return count


def solution(storage, requests):
    storage = [list(row) for row in storage]

    count = len(storage) * len(storage[0])

    for request in requests:

        if len(request) == 1:
            count = fork_rain(storage, request, count)

        elif len(request) == 2:
            count = replace_alpha(storage, request[0], count)

    return count