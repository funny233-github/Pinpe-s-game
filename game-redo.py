"""
文件结构
普通结构: 下一个地址,文本,延时
选项表结构: -2,optionList,子选项地址1,.....
清除屏幕 : 下一个地址，clearScreen,延时
"""
import time
file = open("opera.txt",mode="r")
read = file.readlines()
index = 0
for i in range(len(read)):
    read[i] = read[i][0:-1].split("[4839308270]")
while index != -1:
    match read[index][1]:
        case "clearScreen":
            print('\033[2J]')
            # time.sleep(int(read[index][-1]))
            time.sleep(0.5)
            index = int(read[index][0])

        case "optionList":
            print('*'*20)
            for text in read[index][2:]:
                print(read[int(text)][1])
            print('*'*20)

            getoption = int(input())+1
            optionIndex = int(read[index][getoption])
            index = int(read[optionIndex][0]) 

        case _:
            print(read[index][1])
            # time.sleep(int(read[index][-1]))
            time.sleep(0.5)
            index = int(read[index][0])
