n = int(input("请输入班级数："))
ans = 0
for i in range(n):
    print("请输入", i+1, "班的销售额（元）：")
    ans += int(input())
print("总销售额是：", ans, "元")
