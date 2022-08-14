2022-08-14,21点30

优化了一些运行.现在中等难度第一关基本都能赢.
更高难度因为图像更密,识别难度更大.
运行方法:
 小游戏/llkwqb/zzllk.exe
 然后选择中等难度运行.
 之后切到pycharm点击运行lianliankanwaigua3final.py即可.










"# LinkGame_AI_algorithm" 
连连看游戏ai

游戏 in 小游戏/llkwqb/zzllk.exe


run lianliankanwaigua3final.py
and run the game in 3 seconds. move the game window to the left top of the screen.
move your mouse out of the game window to make him not affect the AI.


there is still some bug:

附带2 demo mp4
洗牌之后需要考虑黑色空格. 需要继续优化代码

#================
# bug 汇总:
#   1.  看到主要是cv的问题没有做完美, flood迷宫算法没问题
#       cv问题是, 第一个maze 的右下角坐标有时候识别不出来. 考虑调节参数
#                 第二个是切割完小图之后,比较不出来两个相同图片,跟之前担心的一样,差一个像素位置偏差时候很麻烦.
#  2.有兴趣的哥们可以试着优化一下这2点. 先分享版本到这.有时间继续优化.
