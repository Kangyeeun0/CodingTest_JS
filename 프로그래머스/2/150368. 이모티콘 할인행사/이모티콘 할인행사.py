def solution(users, emoticons):
    answer = [0, 0]  # [가입자 수, 매출]
    discounts = [10, 20, 30, 40]
    selected = []

    def dfs(idx):
        nonlocal answer

        # 모든 이모티콘의 할인율을 정한 경우
        if idx == len(emoticons):
            subscriber = 0
            sales = 0

            # 각 사용자 계산
            for need_discount, limit in users:
                total = 0

                for discount, price in zip(selected, emoticons):
                    if discount >= need_discount:
                        total += price * (100 - discount) // 100

                if total >= limit:
                    subscriber += 1
                else:
                    sales += total

            # 정답 갱신
            if subscriber > answer[0]:
                answer = [subscriber, sales]
            elif subscriber == answer[0] and sales > answer[1]:
                answer = [subscriber, sales]

            return

        # 현재 이모티콘 할인율 선택
        for discount in discounts:
            selected.append(discount)
            dfs(idx + 1)
            selected.pop()

    dfs(0)

    return answer