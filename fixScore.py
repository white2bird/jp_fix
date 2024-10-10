# 原始加分
import re
origin_score_dict = {}
with open('origin.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        a = line.strip().split(" ")
        # print("-a")
        uid = a[3].strip()
        origin_score = a[2].strip()
        print('zincrby advertising_campaign_202410_vj_day_rank_JP_20241011 -' + origin_score + ' ' + uid)

print('\n')
print('\n')
with open('origin.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        a = line.strip().split(" ")
        # print("-a")
        uid = a[3].strip()
        origin_score = a[2].strip()
        print('zincrby advertising_campaign_202410_vj_day_time_rank_JP_20241011  -' + origin_score + ' ' + uid)

print('\n')
print('\n')
with open('score.txt') as score_f:
    scores_lines = score_f.readlines()

    for i in range(0, len(scores_lines), 2):
        score = re.findall(r'"(.*?)"', scores_lines[i + 1])[0]
        uid = re.findall(r'"(.*?)"', scores_lines[i])[0]

        print('zincrby advertising_campaign_202410_vj_day_rank_JP_20241011 ' + score + ' ' + uid)
        # print('zincrby advertising_campaign_202410_vj_day_time_rank_JP_20241011 ' + score + ' ' + uid)
print('\n')
with open('score.txt') as score_f:
    scores_lines = score_f.readlines()

    for i in range(0, len(scores_lines), 2):
        score = re.findall(r'"(.*?)"', scores_lines[i + 1])[0]
        uid = re.findall(r'"(.*?)"', scores_lines[i])[0]

        print('zincrby advertising_campaign_202410_vj_day_time_rank_JP_20241011 ' + score + ' ' + uid)





if __name__ == '__main__':
    pass