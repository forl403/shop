ming = input("请输入用户名：")
mi = int(input("请输入密码："))
name = "admin"
ser = 88888
if ming == name and mi == ser:
	print("输入正确")
elif ming != name:
	print("用户名不存在")
elif ming == name and mi != ser:
	print("密码错误")
