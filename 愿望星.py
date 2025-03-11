s = 0
for i in range(12):
    #print(i+1, "月获得的愿望星是：")
    s += int(input(str(i+1) + "月获得的愿望星是："))
print("去年小明一共获得愿望星是", s, "颗")
print("平均每个月获得的愿望星是：", round((s / 12.0), 1), "颗")
