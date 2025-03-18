from random import choice, randint
lst = ["春暖花开","千军万马","白手起家","风和日丽",
"助人为乐","走马观花","杯水车薪","瓜田李下",
"春风化雨","水深火热","马到成功","揠苗助长",
"鸟语花香","一事无成","别有洞天","十全十美",
"三心二意","取长补短","一表人才","舍己为人",
"先来后到","南来北往","甜言蜜语","一鸣惊人",
"春华秋实","龙飞凤舞","川流不息","画龙点睛",
"惊涛骇浪","雨过天晴","五彩缤纷","五谷丰登",
"小题大做","漫不经心","纹丝不动","日积月累",
"一知半解","天高云淡","千变万化","万众一心"]
score = 5
print("====中华成语挑战赛====")
for i in range(8):
    print("当前分数:", score)
    quest = choice(lst)
    invis = int(randint(0, 3))
    ans = quest[invis]
    rep = str(input(quest[0:invis] + "__" +quest[invis+1:4]))
    if rep == ans:
        score += 2
        print("恭喜答对!")
    elif rep == '':
        print("跳过当前题目.")
    else:
        score -= 1
        print("答错了! 答案是:", ans)
    if score < 0:
        break
if score < 0:
    print("你没分了! 游戏结束.")
#elif score <= 8:
#    print("没机会了.")
else:
    print("恭喜你, 以 "+str(score)+"分 的好成绩通关! ")
