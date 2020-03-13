mon = int(input("请输入一个月份："))
if mon in (3,4):
	print("%s月是春季"%(mon))
elif mon in (5,6,7,8):
	print("%s月是夏季"%(mon))
elif mon in (9,10):
	print("%s月是秋季"%(mon))
elif mon in (11,12,1,2):
	print("%s月是冬季"%(mon))