import random

print("\t\t\t\t欢迎光临猜数字游戏厅\n")
print("温馨提示：您共有5次机会，请把握哦~~~\n")

i = 0
while True:
	if i < 5:
		num = int(input("请输入0~10之间任意一个整数；"))
		sysnum = random.randint(0,10)
		if num == sysnum:
			print(" ")
			print("系统出的数也是：%s"%(sysnum))
			print("您和系统居然是一条心，恭喜您猜对了，撒花~~~~\n")
			break
		else:
			print("对不起，你猜错了，系统是%s"%(sysnum))
			i += 1
	else:
		print("您的机会用完了，欢迎下次光临")
		break