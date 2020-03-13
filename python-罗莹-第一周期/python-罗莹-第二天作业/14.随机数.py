import random

ran = random.randint(0,5)
if ran == 0:
	print("产生的数为:%s,进入战斗"%(ran))
elif ran == 1:
	print("产生的数为:%s,捡到宝箱"%(ran))
elif ran == 2:
	print("产生的数为:%s,捡到武器"%(ran))
elif ran == 3:
	print("产生的数为:%s,捡到弹药"%(ran))
elif ran == 4:
	print("产生的数为:%s,踩到陷阱"%(ran))
elif ran == 5:
	print("产生的数为:%s,无事件"%(ran))