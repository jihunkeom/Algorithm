from itertools import product
def solution(users, emoticons):
    answer = []
    ratios = [40, 30, 20, 10]
    discounts = product(ratios, repeat=len(emoticons))
    for discount in discounts:
        user_cnt = 0
        rev = 0
        for user in users:
            user_buy = 0
            for i in range(len(emoticons)):
                if user[0] > discount[i]:
                    continue
                emo_price = emoticons[i]* (1-discount[i]/100)
                user_buy += emo_price
            if user_buy >= user[1]:
                user_cnt += 1
            else:
                rev += user_buy
        answer.append([user_cnt, rev])
    answer = sorted(answer, key=lambda x: (-x[0], -x[1]))[0]
    return answer