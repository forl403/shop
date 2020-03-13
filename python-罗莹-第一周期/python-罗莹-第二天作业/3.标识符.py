
while True:
	inp = input("请输入要判断的字符(A、a,B、￥a,C、_12,D、$a@12,E、false,F、False)：")
	inp = inp.upper()
	print(" ")

	if inp == "A":
		print("a可以作为标识符")
		break
	elif inp == "B":
		print("￥a不能作为标识符")
		break
	elif inp == "C":
		print("_12可以作为标识符")
		break
	elif inp == "D":
		print("$a@12不能作为标识符")
		break
	elif inp == "E":
		print("false可以作为标识符")
		break
	elif inp == "F":
		print("False不能作为标识符")
		break
	else:
		print("请输入正确的选项\n")
		continue

