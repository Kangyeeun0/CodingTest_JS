import heapq

def solution(operations):
    min_q = []
    max_q = []
    count = {}

    for operation in operations:
        command, num = operation.split()
        num = int(num)

        if command == "I":
            heapq.heappush(min_q, num)
            heapq.heappush(max_q, -num)
            count[num] = count.get(num, 0) + 1

        elif command == "D":
            if not count:
                continue

            if num == 1:
                while max_q and count.get(-max_q[0], 0) == 0:
                    heapq.heappop(max_q)

                if max_q:
                    value = -heapq.heappop(max_q)
                    count[value] -= 1

                    if count[value] == 0:
                        del count[value]

            else:
                while min_q and count.get(min_q[0], 0) == 0:
                    heapq.heappop(min_q)

                if min_q:
                    value = heapq.heappop(min_q)
                    count[value] -= 1

                    if count[value] == 0:
                        del count[value]

    while min_q and count.get(min_q[0], 0) == 0:
        heapq.heappop(min_q)

    while max_q and count.get(-max_q[0], 0) == 0:
        heapq.heappop(max_q)

    if not count:
        return [0, 0]

    return [-max_q[0], min_q[0]]