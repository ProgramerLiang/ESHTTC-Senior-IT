metre = 3000
sec = int(input("请输入车辆通行时间（秒）:"))
v_ms = metre / sec
v_kmh = v_ms * 3.6
print("您的车速为:", '%.1f'%v_kmh, "千米/小时")
if v_kmh > 60:
    print("您已超速，请安全驾驶！")
else:
    print("正常行驶，祝您一路顺风！")