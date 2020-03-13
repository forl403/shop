num1 = float(input("请输入第一个数："))
num2 = float(input("请输入第二个数："))
way = input("请输入运算符(+，-，*，/，%，//，**)：")
print("\n")
if way == "+":
	print("%s + %s = %s"%(num1,num2,num1+num2))
elif way == "-":
	print("%s - %s = %s"%(num1,num2,num1-num2))
elif way == "*":
	print("%s x %s = %s"%(num1,num2,num1*num2))
elif way == "/":
	print("%s / %s = %s"%(num1,num2,num1/num2))
else:
	print("请输入正确的运算符：")