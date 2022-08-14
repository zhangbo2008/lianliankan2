import mouse
import numpy as np
zuoshangjiao= [205, 184]
youxiajiao =[813, 1034]
if 1:# 非第一次的getmaze就不要再算zuoshangjiao,youxiajiao, 仍然使用第一次的zuoshangjia youxiajia


    print('getmaze2里面的',zuoshangjiao,youxiajiao)
    mouse.move(1,1)
    print()
    import pyautogui
    import cv2

    img = pyautogui.screenshot()  # x,y,w,h
    # img.save('screenshot.png')
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

    screen=img[:1200,:1300]
    global debug_screen

    if 1: # 使用保存好的图片调试用
        screen=cv2.imread('99999.png')[:1200,:1300]
        debug_screen = screen
    cv2.imwrite('tmp.png',screen) # 图像切割.
    # print(screen)
    #===========找到游戏操作的图版的左上和右下. 图版的含义是你一堆littlepic拼起来的区域.
    # littlepic是 那些小图片. 目标就是小图片一样的都点一下.


    # # 找到第一个像素点他的 左边50全是黑.
    # flag=0
    # width,height,channel=screen.shape
    # for i in range(width-littlepic[1]):
    #     if flag==1:
    #         break
    #     for j in range(50,height//2):
    #         tmp=screen[i,j-50:j]
    #         if np.all(tmp==0)  and tmp.shape[0]==50 and np.all(screen[i:i+7,j:j+7]!=0):
    #             print(i,j)
    #             flag=1
    #             cv2.imwrite('tmp2.png', screen[:i+10,:j+10])  # 图像切割.
    #             break
    #
    #
    # print(1111111111)
    #
    # #==========同理找到右下角.
    #
    # # 找到第一个像素点他的 左边50全是黑.
    # flag=0
    # width,height,channel=screen.shape
    # for i in range(width-littlepic[1],0,-1):
    #     if flag==1:
    #         break
    #     for j in range(height-littlepic[0],50,-1):
    #         tmp=screen[i,j:j+35]
    #         if np.all(tmp==0)  and tmp.shape[0]==35 and np.all(screen[i-7:i,j-7:j]!=0):
    #             print(i,j)
    #             flag=1
    #             cv2.imwrite('tmp3.png', screen[:i-10,:j-10])  # 图像切割.
    #             break


    print('zuojiao',zuoshangjiao,'youxiajiao',youxiajiao)


    tmp4=screen[zuoshangjiao[0]:youxiajiao[0],zuoshangjiao[1]:youxiajiao[1]]

    cv2.imwrite('tmp4.png',screen[zuoshangjiao[0]:youxiajiao[0],zuoshangjiao[1]:youxiajiao[1]])
    tmp4 = cv2.cvtColor(tmp4, cv2.COLOR_BGR2GRAY)
    #cv2.THRESH_OTSU 可以优化阈值的选择.
    ret,thresh1 = cv2.threshold(tmp4,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)



    cv2.imwrite('tmp5.png',thresh1)  # 图像切割.
    tmppic=thresh1
    #======找到所有的水平数值的切割.
    #============找到水平的横线. 都是0的一行

    hang=[]
    for i in range(thresh1.shape[0]):
        if np.all(thresh1[i,:]==0):
          hang.append(i)


    #=========进行像素合并. 找间断的,然后取中值

    hang_after_fix=[]

    savelist=[]

    for i,j in enumerate(hang):
        if i==0:
            savelist.append(j)
            continue
        if j-hang[i-1]==1:
            savelist.append(j)
        else:
            hang_after_fix.append(sum(savelist)/len(savelist))
            savelist=[]
            savelist.append(j)
        #======最后一行别忘了
        if i==len(hang)-1:
            hang_after_fix.append(sum(savelist) / len(savelist))
            savelist = []
    print(hang_after_fix)













    lie=[]
    for i in range(thresh1.shape[1]):
        if np.all(thresh1[:,i]==0):
          lie.append(i)


    #=========进行像素合并. 找间断的,然后取中值

    lie_after_fix=[]

    savelist=[]

    for i,j in enumerate(lie):
        if i==0:
            savelist.append(j)
            continue
        if j-lie[i-1]==1:
            savelist.append(j)
        else:
            lie_after_fix.append(sum(savelist)/len(savelist))
            savelist=[]
            savelist.append(j)
        #======最后一行别忘了
        if i==len(lie)-1:
            lie_after_fix.append(sum(savelist) / len(savelist))
            savelist = []
    print(lie_after_fix)

    #索引int化.
    hang_after_fix=[int(i) for i in hang_after_fix]
    lie_after_fix=[int(i) for i in lie_after_fix]



    #==============下面进行切割小图, 然后存下来,debug用

    dic_all_pic={}
    qipansize=len(hang_after_fix)-1,len(lie_after_fix)-1
    # tmppic 是 棋盘
    for i in range(len(hang_after_fix)-1):
        for j in range(len(lie_after_fix)-1):
            tmp=tmppic[hang_after_fix[i]:hang_after_fix[i+1],lie_after_fix[j]:lie_after_fix[j+1]]
            # cv2.imwrite(f'fordebug/{i}_{j}.png',tmp)
            dic_all_pic[f'{i}_{j}']=tmp


    #=======下面对切割完的进行比较和编码


    print(1)
    #========每个相同的小图之间可能差一些黑色框.所以把矩阵周围一圈黑色都去除.
    for i,j in dic_all_pic.items():
        hang_del,lie_del=[],[]
        for i1 in range(j.shape[0]):
            if np.all(j[i1,:]==0):
                hang_del.append(i1)
        for i1 in range(j.shape[1]):
            if np.all(j[:,i1]==0):
                lie_del.append(i1)
        j=np.delete(j,hang_del,0)
        j=np.delete(j,lie_del,1)
        dic_all_pic[i]=j






    #==========编码
    all_pic=list(dic_all_pic.values())




    # ==========修剪小图片的shape .有时候会差像素.可能因为二值化.都按照最小的切割试试
    xmin = min([i.shape[0] for i in all_pic])
    ymin = min([i.shape[1] for i in all_pic])
#---------再减一个像素.
    all_pic=[i[1:xmin-1,1:ymin-1] for i in all_pic]





    #========save little pic for debug
    # shutil.rmtree('fordebug')
    # import os
    # os.mkdir('fordebug',)
    # for i in dic_all_pic:
    #     cv2.imwrite(f'fordebug/{i}.png',dic_all_pic[i])

    all_pic_del_dup=[] # 记录的是索引
#================================这个地方需要优化比较算法!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for i in range(len(all_pic)):
        print(f'当前计算的索引是第{i//qipansize[1]}行图片,{i%qipansize[1]}列的图片',)
        dex=[i//qipansize[1],i%qipansize[1]]
        for j in ((all_pic_del_dup)):

            #  有时候切分会差几个像素!
            if np.sum(all_pic[i]!=all_pic[j])<5:#两个图片相同

                all_pic_del_dup.append(j)
                break
        else: # 如果不走break时候才走else. for-else结构非常实用.
          all_pic_del_dup.append(i)

    all_pic_del_dup=np.array(all_pic_del_dup)
    all_pic_del_dup.resize(qipansize)
    print(1)








    print(1)


    #==================下面解这个矩阵.


    # 首先最外一圈补 -1 ,对角线不用补. 不允许走斜线.但是矩阵缺位置更难描述.所以还是都补上

    #=========使用图片的maze
    maze=all_pic_del_dup+1

    # print(1)
    maze2=np.ones([maze.shape[0]+2,maze.shape[1]+2])*0
    maze2[1:-1,1:-1]=maze
    # print(1)
    maze=maze2
    maze=[list(i) for i in maze]
    print("下面打印图片给的maze",maze)          #========以上就是获取maze的代码
    with open('maze.txt','w') as f:
        for i in maze:
            f.write(str(i)+'\n')

    print(maze)
