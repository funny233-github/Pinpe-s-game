#····················
#000F2DA7F项目
#····················
#编码=UTF–8
#语言=Python 3.9.7
#依赖库=time,sys,colorama
#版本=试玩版
import time
import sys
from colorama import Fore,Back,Style
#––变量––
key=0
paper=0
picture=0
#––函数––
def over():
    #游戏失败
    print('\033[2J')#清屏
    print('\033[0;1H')
    print(
Back.RED
+'非最终结局')
    print(Style.RESET_ALL+'你可以重进游戏，重新来过')
    sys.exit(0)
def end(word):
    #结局
    print('\033[2J')#清屏
    print('\033[0;1H')
    print(Back.WHITE+Fore.BLACK+'达成结局–'+word)
    print(Style.RESET_ALL+'''制作=Pinpe
技术支持=抑彡芜柒玖''')
    sys.exit(0)
#––游戏––
#启动
print('\033[?25l=开始冷启动=')
print('初始化启动程序...')
time.sleep(4)
print(
Fore.GREEN
+'\033[2;18H完成')
print(Style.RESET_ALL+'加载自检程序...')
time.sleep(4)
print(
Fore.GREEN
+'\033[3;16H完成')
print(Style.RESET_ALL+'初始化自检程序...')
time.sleep(3)
print(
Fore.GREEN
+'\033[4;18H完成')
print(Style.RESET_ALL+'准备自检...')
time.sleep(6)
print(
Fore.GREEN
+'\033[5;12H完成') 
print(Style.RESET_ALL+'开始自检...')
time.sleep(10)
print(
Fore.GREEN
+'\033[6;12H完成')
print(Style.RESET_ALL+'加载系统...')
time.sleep(20)
print(
Fore.GREEN
+'\033[7;12H完成')
print(Style.RESET_ALL+'=冷启动完成=')
time.sleep(1)
print('\033[2J')#清屏
time.sleep(1)
print('\033[0;1H')
#硬盘
print('你迷迷糊糊的醒来了')
time.sleep(2)
print('这里看起来像个图书馆，有很多书籍')
time.sleep(2)
print('但是你什么都不记得了，大脑中一片空白')
time.sleep(2)
print('你艰难的爬起来，你想要做点什么')
time.sleep(2)
while True:
    print('·'*20)
    print(Style.BRIGHT+'A '+Style.RESET_ALL+'翻看书籍')
    print(Style.BRIGHT+'B '+Style.RESET_ALL+'找到出口')
    print(Style.BRIGHT+'C '+Style.RESET_ALL+'搜刮物品')
    print('·'*20)
    select=input('硬盘>')
    if select=='A':
        time.sleep(2)
        print('这里所有的书都没有标注书名，只有编号，好像还是十六进制的')
        time.sleep(2)
        print('比如"FFFA4C"、"FAC004F"之类的')
        time.sleep(2)
        print('而且有些书上面都写满了十六进制，有些书上面好像写了汇编，其他书干脆就全是二进制了')
        time.sleep(2)
        print('你一本也读不懂')
        time.sleep(2)
    elif select=='B':
        if key==0:
            time.sleep(2)
            print('走了好久，终于找到了一扇门')
            time.sleep(2)
            print('不知道是不是出口')
            time.sleep(2)
            print('但是门被锁上了，你手上没有钥匙')
            time.sleep(2)
            print('你彻底绝望了')
            time.sleep(2)
            over()
        else:
            #内存
            time.sleep(2)
            print('走了好久，终于找到了一扇门')
            time.sleep(2)
            print('你用钥匙打开了门')
            time.sleep(2)
            print('映入眼帘的是一条走廊，望不到底')
            time.sleep(2)
            print('你看了一些门牌号，也都是十六进制的')
            time.sleep(2)
            print('很多房间都是锁着的，但有些还是能打开')
            time.sleep(2)
            while True:
                print('·'*20)
                print(Style.BRIGHT+'FB '+Style.RESET_ALL+'打开FB号门')
                print(Style.BRIGHT+'EF '+Style.RESET_ALL+'打开EF号门')
                print(Style.BRIGHT+'E3 '+Style.RESET_ALL+'打开E3号门')
                print(Style.BRIGHT+'D9 '+Style.RESET_ALL+'打开D9号门')
                print('·'*20)
                select=input('内存>')
                if select=='FB':
                    time.sleep(2)
                    print('里面什么都没有')
                    time.sleep(2)
                    print('是一片虚无，没有颜色，没有声音，没有形状')
                    time.sleep(2)
                    print('连维度也没有')
                    time.sleep(2)
                    print('但是你还是进去了')
                    time.sleep(2)
                    over()
                elif select=='EF':
                    time.sleep(2)
                    print('里面有一张照片')
                    time.sleep(2)
                    print('是一张自拍照，可是人物看起来在一个玩偶里面')
                    time.sleep(2)
                    print('挺可爱的')
                    time.sleep(2)
                    print('你把这张照片收着了')
                    picture=1
                    time.sleep(2)
                elif select=='E3':
                    if paper==0:
                        time.sleep(2)
                        print('你来到了一个有着很多控制台的房间')
                        time.sleep(2)
                        print('但好像没有权限')
                        time.sleep(2)
                    else:
                        #CPU
                        time.sleep(2)
                        print('你来到了一个有着很多控制台的房间')
                        time.sleep(2)
                        print('你发现有一个可以刷卡的地方')
                        time.sleep(2)
                        print('手里正好有一张卡片')
                        time.sleep(2)
                        print('你尝试刷了一下')
                        time.sleep(2)
                        print('"嘀~"一声，正前方的大屏幕上出现了八个字:')
                        time.sleep(2)
                        print('"管理员权限已转移"')
                        time.sleep(2)
                        end('未完待续')
                elif select=='D9':
                    time.sleep(2)
                    print('里面有一张卡片')
                    time.sleep(2)
                    print('上面也写满了16进制')
                    time.sleep(2)
                    print('收着吧，万一有时候要用呢...')
                    paper=1
                    time.sleep(2)
    elif select=='C':
        time.sleep(2)
        print('你找来找去，只找到了一个钥匙，不知道干什么用的')
        key=1
        time.sleep(2)
