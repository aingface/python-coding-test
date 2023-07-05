import math


def solution(time, gold, upgrade):
    answer = gold * (time // upgrade[0][1])
    total_grade = len(upgrade)
    # index+1 레벨 달성 후 골드와 남은 시간
    graph = [[0, time]]


    for upgrade_lv in range(1, total_grade):
        upgrade_cost = upgrade[upgrade_lv][0]
        time_cost = upgrade[upgrade_lv][1]

        # 업그레이드 후 남은 시간과 골드 구하기
        last_gold = graph[upgrade_lv - 1][0]
        last_time = graph[upgrade_lv - 1][1]

        #남은 골드가 업그레이드 비용보다 크거나 작은 경우 분기
        if last_gold<upgrade_cost:
            gold_count_to_upgrade = math.ceil(upgrade_cost / gold)
            last_gold = last_gold+gold*gold_count_to_upgrade-upgrade_cost
            last_time = last_time-upgrade[upgrade_lv-1][1]*gold_count_to_upgrade
        else:
            #남은 골드가 업그레이드 비용보다 같거나 크면 더 안캐도 된
            last_gold=last_gold-upgrade_cost다

        now_total=last_gold+gold*(last_time//time_cost)
        answer=max(answer,now_total)


    return answer

# print(solution(100, 200, [[0, 5], [1500, 3], [3000, 1]]))
# print(solution(49, 200, [[0, 5], [1500, 3], [1501, 1]]))
print(solution(11, 1000, [[0, 5], [100, 4], [200, 3]]))
