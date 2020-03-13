# 判断质数
num = int(input("输入一个大于2的整数："))
i = 2
while i < num:
	if num % i == 0:
		print("%s不是质数"%(num))
		break
	i += 1
else:
	print("%s是质数"%(num))