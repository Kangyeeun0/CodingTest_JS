def solution(files):
    answer = []

    for file in files:
        start = 0

        while not file[start].isdigit():
            start += 1

        end = start

        while end < len(file) and file[end].isdigit() and end - start < 5:
            end += 1

        answer.append((file[:start], file[start:end], file[end:]))

    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))

    return ["".join(x) for x in answer]