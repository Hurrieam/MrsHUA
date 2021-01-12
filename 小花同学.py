import os
import random
import time

os.system("color F0")

print("小花同学 Alpha")
print("by Hurrieam")
print("on 20200104")

while True:
    inp = str(input("\n你说：\n>>"))

    inp = inp.replace("吗", "")
    inp = inp.replace("?", "！")
    inp = inp.replace("？", "！")
    
    inp = inp.replace("你", "我")
    inp = inp.replace("谁", "Hurrieam开发的智能陪聊机器人小花")
    inp = inp.replace("要", "也要")

    time.sleep(random.random())

    print("\n小花同学说：\n>>" + inp)
